<template>
  <main class="blog">
    <section
      id="Jupyter"
      class="jupyter-section"
    >
      <div class="iframe-wrapper">
        <iframe
          ref="iframeRef"
          :src="iframeSrc"
          frameborder="0"
          sandbox="allow-same-origin allow-scripts allow-popups allow-forms"
          title="Jupyter Notebook"
          @load="onIframeLoad"
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
import { ref, onMounted, onUnmounted, watch } from 'vue'
import { useI18n } from 'vue-i18n'
import { useNavStore, useJupyterStore } from '@/stores'

const { locale } = useI18n()

// Props
const props = defineProps({
  postUrl: {
    type: String,
    required: true
  }
})

// Stores
const navStore = useNavStore()
const jupyterStore = useJupyterStore()

// Refs
const iframeRef = ref(null)
const iframeDoc = ref(null)
const theme = ref(sessionStorage.getItem('theme') || 'dark')
const iframeSrc = ref(`/notebooks/${locale.value}/${props.postUrl}`)

/**
 * Make items for navigation side-menu
 * @param {NodeList} headings - Array of headings
 * @returns {Array} - Array of nav items
 */
function makeUniqueNavItems (headings) {
  const uniqueNavItems = []
  headings.forEach(h => {
    const id = h.id
    const text = h.textContent?.replace('¶', '').trim() || 'untitled'
    uniqueNavItems.push({
      key: text,
      link: `#${id}`,
      faIcon: ['fas', 'house'],
      disabled: false,
      type: 'jupyter'
    })
  })
  return uniqueNavItems
}

// Observer for sections
let observer = null

/**
 * Observe sections
 * @param {HTMLDocument} observedDoc - Document to observe
 */
function observeSections (observedDoc) {
  if (observer) observer.disconnect()

  observer = new IntersectionObserver((entries) => {
    for (const entry of entries) {
      if (entry.isIntersecting) {
        const headingText = entry.target.textContent?.replace('¶', '').trim() || 'untitled'
        navStore.setCurrentSection(headingText)
      }
    }
  }, {
    root: observedDoc,
    rootMargin: '0px',
    threshold: 0.3
  })

  const targets = observedDoc.querySelectorAll('h1[id], h2[id]')
  targets.forEach(target => observer.observe(target))
}

/**
 * Store iframe document, navigation items
 * and observe sections
 */
function onIframeLoad () {
  iframeDoc.value =
    iframeRef.value?.contentDocument ||
    iframeRef.value?.contentWindow?.document
  const headings = iframeDoc.value.querySelectorAll('h1[id], h2[id]')
  const items = makeUniqueNavItems(headings)
  navStore.setMainSection(items[0].key)
  observeSections(iframeDoc.value)
  // Set nav items to store
  navStore.setNavItems(items)
  // Set iframe document to store
  jupyterStore.iframeDoc = iframeDoc.value
}

/**
 * Scroll to first heading
 */
function scrollToFirstHeading () {
  if (!iframeDoc.value) return
  const first = navStore.navItems[0]
  if (!first) return

  const el = iframeDoc.value.getElementById(first.link.replace('#', ''))
  if (el) el.scrollIntoView({ behavior: 'smooth' })
}

function onThemeChange (e) {
  theme.value = e.detail.theme
}

onMounted(() => {
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
