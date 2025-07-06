<script setup>
import { ref, onMounted, onUnmounted, onBeforeUnmount, watch, nextTick } from 'vue'

const emit = defineEmits([
  'update:mainSection', 
  'update:navMenuComponent',
  'update:currentSection',
  'update:navItems',
  'update:navMenuLangPage'
])

let jupyterNavItems = []

const navMenuLangPage = ''
const currentSection = ref('')

// Utility to get link by key
function getLinkByKey(key) {
  const item = jupyterNavItems.find(i => i.key === key)
  return item?.link || ''
}

// Intersection observer for main page sections
let observer = null
function observeSections() {
  observer = new IntersectionObserver((entries) => {
    for (const entry of entries) {
      if (entry.isIntersecting) {
        currentSection.value = entry.target.id
      }
    }
  }, {
    rootMargin: '0px',
    threshold: 0.3,
  })
  document.querySelectorAll('main section[id]').forEach(section => {
    observer.observe(section)
  })
}

// Emit startup values
onMounted(async () => {
  emit('update:mainSection', getLinkByKey('home'))
  emit('update:navItems', jupyterNavItems)
  emit('update:currentSection', currentSection.value)
  emit('update:navMenuLangPage', navMenuLangPage)
  await nextTick()
  observeSections()
})

onUnmounted(() => {
  if (observer) observer.disconnect()
})

watch(currentSection, (newVal) => {
  emit('update:currentSection', newVal)
})

// Jupyter-specific logic
const theme = ref(sessionStorage.getItem('theme') || 'dark')
const iframeSrc = ref(`/notebooks/${theme.value}/analyse_tv.html`)

function extractHeadingsFromIframe(iframeEl) {
  try {
    const doc = iframeEl.contentDocument || iframeEl.contentWindow?.document
    if (!doc) return
    const headings = doc.querySelectorAll('h2')
    const result = []
    headings.forEach(h2 => {
      const id = h2.id
      const text = h2.textContent?.replace('¶', '').trim() || 'untitled'
      const item = {
        key: text,
        link: `#${id}`,
        faIcon: ['fas', 'house'],
        disabled: false,
        type: "jupyter"
      }
      result.push(item)
    })
    emit('update:navItems', [...jupyterNavItems, ...result])
  } catch (err) {
    console.error('Failed to access iframe contents:', err)
  }
}

function onThemeChange(e) {
  theme.value = e.detail.theme
}

watch(theme, (newTheme) => {
  iframeSrc.value = `/notebooks/${newTheme}/analyse_tv.html`
})

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

<template>
  <main class="blog">
    <section :id="getLinkByKey('home').replace('#', '')" class="jupyter-section">
      <h1 class="blog">Jupyter Notebook</h1>
      <iframe 
        :src="iframeSrc" 
        frameborder="0" 
        sandbox="allow-same-origin allow-scripts allow-popups allow-forms"
        title="Jupyter Notebook"
      />
    </section>
  </main>
</template>

<style scoped>
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
  border-radius: var(--border-radius);
  width: 100%; 
  height: 70vh; 
}

.blog {
  margin-bottom: 1rem;
}
</style>
