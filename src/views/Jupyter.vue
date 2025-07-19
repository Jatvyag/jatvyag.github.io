<template>
  <main class="blog">
    <section
      :id="getLinkByKey('home').replace('#', '')"
      class="jupyter-section"
    >
      <div class="iframe-wrapper">
        <iframe
          :src="iframeSrc"
          frameborder="0"
          sandbox="allow-same-origin allow-scripts allow-popups allow-forms"
          title="Jupyter Notebook"
        />
        <font-awesome-icon
          :icon="['fas', 'chevron-up']"
          class="chevron up iframe"
          @click="scrollToFirstHeading"
        />
      </div>
    </section>
  </main>
</template>

<script setup>
import { ref, onMounted, onUnmounted, onBeforeUnmount, watch, nextTick } from 'vue'
import { useI18n } from 'vue-i18n'
const { locale } = useI18n()

const props = defineProps({
  post_url: {
    type: String,
    required: true
  }
})

const emit = defineEmits([
  'update:mainSection',
  'update:navMenuComponent',
  'update:currentSection',
  'update:navItems',
  'update:navMenuLangPage'
])

const navMenuLangPage = ''
const currentSection = ref('')

// Utility to get link by key
function getLinkByKey (key) {
  const item = jupyterNavItems.value.find(i => i.key === key)
  return item?.link || ''
}

// Intersection observer for main page sections
let observer = null
function observeSections () {
  observer = new IntersectionObserver((entries) => {
    for (const entry of entries) {
      if (entry.isIntersecting) {
        currentSection.value = entry.target.id
      }
    }
  }, {
    rootMargin: '0px',
    threshold: 0.3
  })
  document.querySelectorAll('main section[id]').forEach(section => {
    observer.observe(section)
  })
}

// Emit startup values
onMounted(async () => {
  emit('update:mainSection', getLinkByKey('home'))
  emit('update:navItems', jupyterNavItems.value)
  emit('update:currentSection', currentSection.value)
  emit('update:navMenuLangPage', navMenuLangPage)
  await nextTick()
  observeSections()
})

onUnmounted(() => {
  if (observer) observer.disconnect()
})

watch(
  [() => locale.value, () => props.post_url, () => currentSection.value],
  ([newLang, newUrl, newSection]) => {
    iframeSrc.value = `/notebooks/${newLang}/${newUrl}`
    emit('update:currentSection', newSection)
  }
)

// Jupyter-specific logic
const theme = ref(sessionStorage.getItem('theme') || 'dark')
const iframeSrc = ref(`/notebooks/${locale.value}/${props.post_url}`)
const jupyterNavItems = ref([])

function extractHeadingsFromIframe (iframeEl) {
  try {
    const doc = iframeEl.contentDocument || iframeEl.contentWindow?.document
    if (!doc) return
    const headings = doc.querySelectorAll('h2')
    const result = []
    headings.forEach(h2 => {
      const id = h2.id
      const text = h2.textContent?.replace('¶', '').trim() || 'untitled'
      result.push({
        key: text,
        link: `#${id}`,
        faIcon: ['fas', 'house'],
        disabled: false,
        type: 'jupyter'
      })
    })
    jupyterNavItems.value = result
    emit('update:navItems', result)
  } catch (err) {
    console.error('Failed to extract headings:', err)
  }
}

function scrollToFirstHeading () {
  const iframe = document.querySelector('iframe')
  const iframeDoc = iframe?.contentDocument || iframe?.contentWindow?.document
  const first = jupyterNavItems.value[0]
  if (first && iframeDoc) {
    const el = iframeDoc.getElementById(first.link.replace('#', ''))
    if (el) el.scrollIntoView({ behavior: 'smooth' })
  }
}

function onThemeChange (e) {
  theme.value = e.detail.theme
}

let hasExtracted = false

onMounted(() => {
  window.addEventListener('theme-changed', onThemeChange)
  const iframe = document.querySelector('iframe')
  iframe.addEventListener('load', () => {
    if (!hasExtracted) {
      extractHeadingsFromIframe(iframe)
      hasExtracted = true
    }
  })
})

onBeforeUnmount(() => {
  window.removeEventListener('theme-changed', onThemeChange)
})
</script>

<style lang="scss" scoped>
main.blog {
  display: flex;
  flex-flow: column;
  align-items: center;
}

.jupyter-section {
  width: 100%;
  max-width: 80%;
  padding: 2rem;
}

iframe {
  border-radius: $border-radius;
  width: 100%;
  height: 80vh;
}

.blog {
  padding-bottom: 1rem;
}

.iframe-wrapper {
  display: flex;
  margin-top: 2rem;
}

.chevron.up.iframe {
  font-size: 2rem;
  margin-bottom: 0rem;
  padding-left: 0.5rem;
}

@media (max-width: 600px) {
    .iframe-wrapper {
      flex-direction: column;
    }
}
</style>
