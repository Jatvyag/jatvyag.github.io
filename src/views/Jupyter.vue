<template>
  <main class="blog">
    <section
      id="Jupyter"
      class="jupyter-section"
    >
      <div class="iframe-wrapper">
        <iframe
          ref="jupyter-notebook"
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
import { ref, onMounted, onUnmounted, watch, nextTick, useTemplateRef } from 'vue'
import { useI18n } from 'vue-i18n'
import { useNavStore } from '@/stores/nav'

const nav = useNavStore()
const { locale } = useI18n()

const iframe = useTemplateRef('jupyter-notebook')

const props = defineProps({
  postUrl: {
    type: String,
    required: true
  }
})

const theme = ref(sessionStorage.getItem('theme') || 'dark')
const iframeSrc = ref(`/notebooks/${locale.value}/${props.postUrl}`)

let observer = null

const iframeDoc = ref(null)

function getIframe () {
  iframeDoc.value = iframe.value?.contentDocument || iframe.value?.contentWindow?.document
}

function makeUniqueNavItems (headings) {
  const result = []
  headings.forEach(h => {
    const id = h.id
    const text = h.textContent?.replace('¶', '').trim() || 'untitled'
    result.push({
      key: text,
      link: `#${id}`,
      faIcon: ['fas', 'house'],
      disabled: false,
      type: 'jupyter'
    })
  })
  return result
}

function extractHeadings () {
  if (!iframeDoc.value) return
  const headings = iframeDoc.value.querySelectorAll('h1[id], h2[id]')
  const items = makeUniqueNavItems(headings)
  nav.setNavItems(items)
}

function observeSections () {
  if (observer) observer.disconnect()
  if (!iframeDoc.value) return

  observer = new IntersectionObserver((entries) => {
    for (const entry of entries) {
      if (entry.isIntersecting) {
        const headingText = entry.target.textContent?.replace('¶', '').trim() || 'untitled'
        nav.setCurrentSection(headingText)
      }
    }
  }, {
    root: iframeDoc.value, // Use iframe document as root
    rootMargin: '0px',
    threshold: 0.3
  })

  const targets = iframeDoc.value.querySelectorAll('h1[id], h2[id]')
  targets.forEach(target => observer.observe(target))
}

function setupIframeListeners () {
  if (!iframe.value) return

  iframe.value.addEventListener('load', () => {
    getIframe()
    extractHeadings()
    observeSections()
  })
}

function scrollToFirstHeading () {
  if (!iframeDoc.value) return
  const first = nav.navItems[0]
  if (!first) return

  const el = iframeDoc.value.getElementById(first.link.replace('#', ''))
  if (el) el.scrollIntoView({ behavior: 'smooth' })
}

function onThemeChange (e) {
  theme.value = e.detail.theme
}

onMounted(() => {
  nav.setMainSection('Jupyter')

  getIframe()
  setupIframeListeners()

  window.addEventListener('theme-changed', onThemeChange)
})

onUnmounted(() => {
  if (observer) {
    observer.disconnect()
    observer = null
  }
  window.removeEventListener('theme-changed', onThemeChange)
})

watch([() => locale.value, () => props.postUrl], ([newLang, newUrl]) => {
  iframeSrc.value = `/notebooks/${newLang}/${newUrl}`

  // Wait next tick to ensure iframe reloads then re-setup
  nextTick(() => {
    getIframe()
    if (iframe.value?.contentDocument) {
      extractHeadings()
      observeSections()
    } else {
      setupIframeListeners()
    }
  })
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
  border-radius: 10px;
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
