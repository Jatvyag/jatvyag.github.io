<template>
  <main class="blog">
    <section
      ref="JupyterTopRef"
      class="jupyter-section"
    >
      <div class="iframe-wrapper">
        <iframe
          ref="iframeRef"
          :src="iframeSrc"
          frameborder="0"
          sandbox="allow-same-origin allow-scripts"
          title="Jupyter Notebook"
          @load="onIframeLoad"
        />
        <font-awesome-icon
          :icon="['fas', 'chevron-up']"
          class="chevron up iframe"
          @click="scrollToIframeTop"
        />
      </div>
    </section>
  </main>
</template>

<script setup>
import { computed } from 'vue'
import { storeToRefs } from 'pinia'
import { useI18n } from 'vue-i18n'
import { useNavStore, useJupyterStore } from '@/stores'
import { NavItemEnumTypes } from '@/constants'

const { locale } = useI18n()

const { postUrl } = defineProps({
  postUrl: {
    type: String,
    required: true
  }
})

// Stores
const navStore = useNavStore()
const jupyterStore = useJupyterStore()

// Refs
const {
  iframeDoc,
  iframeRef
} = storeToRefs(jupyterStore)

const {
  navItems
} = storeToRefs(navStore)

// Getters
const {
  setCurrentSectionTitle,
  setNavItems
} = navStore

// Iframe source
const iframeSrc = computed(() => `/notebooks/${locale.value}/${postUrl}`)

/**
 * Make items for navigation side-menu from iframe headings
 * @param {NodeList} headings - Array of headings
 * @returns {Array} - Array of nav items
 */
function makeUniqueNavItems (headings) {
  const uniqueNavItems = []
  headings.forEach((heading, index) => {
    const headingId = heading.id
    const text = heading.textContent?.replace('¶', '').trim() || 'untitled'
    uniqueNavItems.push({
      navItemId: index,
      translatedLabel: text,
      idLink: `#${headingId}`,
      faIcon: ['fas', 'house'],
      isDisabled: false,
      navType: NavItemEnumTypes.JUPYTER
    })
  })
  return uniqueNavItems
}

// Observer for iframe sections
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
        setCurrentSectionTitle(headingText)
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
 * Handles the iframe `load` event.
 * - Stores the iframe's document reference in `iframeDoc`.
 * - Extracts heading elements (`h1[id]`, `h2[id]`) and converts them into unique nav items.
 * - Sets the main navigation section and nav items in the `navStore`.
 * - Starts observing sections in the iframe for scroll/visibility updates.
 */
function onIframeLoad () {
  iframeDoc.value =
    iframeRef.value?.contentDocument ||
    iframeRef.value?.contentWindow?.document
  const headings = iframeDoc.value.querySelectorAll('h1[id], h2[id]')
  const items = makeUniqueNavItems(headings)
  observeSections(iframeDoc.value)
  setNavItems(items)
}

/**
 * Smoothly scrolls the iframe content to the first heading element.
 *
 * Does nothing if:
 * - The iframe document is not yet loaded.
 * - No nav items are available in the store.
 */
function scrollToIframeTop () {
  if (!iframeDoc.value) return
  const first = navItems.value[0]
  if (!first) return
  const el = iframeDoc.value.getElementById(first.idLink.replace('#', ''))
  if (el) el.scrollIntoView({ behavior: 'smooth' })
}
</script>

<style lang="scss" scoped>
main.blog {
  display: flex;
  flex-flow: column;
  align-items: center;

  .jupyter-section {
    width: 100%;
    max-width: 80%;
    padding: 2.5rem;
  }

  .iframe-wrapper {
    display: flex;
    margin-top: 2rem;

    @media (max-width: 600px) {
      // Move chevron to the bottom
      flex-direction: column;
    }
  }

  iframe {
    border-radius: 10px;
    width: 100%;
    height: 80vh;
  }

  .chevron.up.iframe {
    font-size: 2rem;
    margin-bottom: 0rem;
    padding-left: 0.5rem;
  }
}
</style>
