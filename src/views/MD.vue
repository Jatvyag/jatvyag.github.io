<template>
  <div
    ref="markdownTopRef"
    class="md"
  >
    <!-- eslint-disable vue/no-v-html -->
    <div
      ref="markdownRef"
      class="md-content"
      v-html="htmlContent"
    />
    <!-- eslint-enable vue/no-v-html -->
  </div>
</template>

<script setup>
import { ref, watchEffect, nextTick, onUnmounted } from 'vue'
import { storeToRefs } from 'pinia'
import { useRoute } from 'vue-router'
import { useI18n } from 'vue-i18n'
import { useNavStore } from '@/stores/nav'
import { NavItemEnumTypes } from '@/constants'
import MarkdownIt from 'markdown-it'
import markdownItAnchor from 'markdown-it-anchor'
import { slugify as translit } from 'transliteration'

const md = new MarkdownIt().use(markdownItAnchor, {
  permalink: false,
  slugify: s => translit(s.trim().toLowerCase())
})

// Add classes to h1/h2
const defaultRender = md.renderer.rules.heading_open || function (tokens, idx, options, env, self) {
  return self.renderToken(tokens, idx, options)
}

md.renderer.rules.heading_open = function (tokens, idx, options, env, self) {
  const token = tokens[idx]
  if (token.tag === 'h1') {
    token.attrJoin('class', 'md-heading-h1')
  } else if (token.tag === 'h2') {
    token.attrJoin('class', 'md-heading-h2')
  }
  return defaultRender(tokens, idx, options, env, self)
}

const { locale } = useI18n()

const route = useRoute()

// Stores
const navStore = useNavStore()

// Refs
const { navItems } = storeToRefs(navStore)
const markdownTopRef = ref(null)
const markdownRef = ref(null)
const htmlContent = ref('')

// Getters
const {
  setNavItems,
  setCurrentSectionTitle
} = navStore

// Files
const markdownFiles = import.meta.glob('../assets/posts/**/**/*.md', { query: '?raw', import: 'default' })

/**
 * Creates navigation items from Markdown headings
 * @param headings {NodeList} - List of headings
 * @returns {Array} - Array of navigation items
 */
function makeUniqueNavItems (headings) {
  const mDNavItems = []
  headings.forEach((heading, index) => {
    const headingId = heading.id
    const text = heading.textContent?.replace('¶', '').trim() || 'untitled'
    mDNavItems.push({
      navItemId: index,
      translatedLabel: text,
      idLink: `#${headingId}`,
      faIcon: ['fas', 'heading'],
      isDisabled: false,
      navType: NavItemEnumTypes.MD
    })
  })
  return mDNavItems
}

/**
 * Extracts Markdown headings and creates navigation items
 */
function extractMarkdownHeadings () {
  if (!markdownRef.value) return
  const headings = markdownRef.value.querySelectorAll('h1[id], h2[id]')
  const items = makeUniqueNavItems(headings)
  setNavItems(items)
}

let observer = null

/**
 * Observes Markdown headings while scrolling
 */
function observeHeaders () {
  if (observer) observer.disconnect()
  if (!markdownRef.value) return
  observer = new IntersectionObserver((entries) => {
    for (const entry of entries) {
      if (entry.isIntersecting) {
        const headingText = entry.target.textContent?.replace('¶', '').trim() || 'untitled'
        setCurrentSectionTitle(headingText)
      }
    }
  }, {
    rootMargin: '-40% 0px -50% 0px',
    threshold: 0.1
  })
  markdownRef.value.querySelectorAll('h1[id], h2[id]').forEach(header => {
    observer.observe(header)
  })
}

watchEffect(async () => {
  htmlContent.value = ''
  const path = `../assets/posts/${locale.value}/${route.params.postUrl}`
  const loader = markdownFiles[path]
  if (loader) {
    const rawMd = await loader()
    htmlContent.value = md.render(rawMd)
    // Wait for DOM update after v-html renders content
    await nextTick()
    extractMarkdownHeadings()
    if (navItems.value.length) {
      setCurrentSectionTitle(navItems.value[0].translatedLabel)
    }
    observeHeaders()
  }
})

onUnmounted(() => {
  if (observer) {
    observer.disconnect()
    observer = null
  }
})
</script>

<style lang="scss" scoped>
.md {
  display: flex;
  justify-content: center;
  margin-top: 4rem;

  .md-content {
    max-width: 80%;
    margin: 0rem 0rem 1rem 0rem;
    padding: 0rem 2rem 2rem 2rem;
    border-radius: 10px;
    background-color: var(--card-bg);
    box-shadow: var(--card-shadow);

    :deep(.md-heading-h1) {
      font-size: 2rem;
    }

    :deep(.md-heading-h2) {
      font-size: 1.5rem;
    }
  }
}
</style>
