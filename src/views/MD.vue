<template>
  <div class="md">
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
import { useRoute } from 'vue-router'
import { useI18n } from 'vue-i18n'
import { useNavStore } from '@/stores/nav'
import MarkdownIt from 'markdown-it'
import markdownItAnchor from 'markdown-it-anchor'
import { slugify as translit } from 'transliteration'

const md = new MarkdownIt().use(markdownItAnchor, {
  permalink: false,
  slugify: s => translit(s.trim().toLowerCase())
})

let observer = null
const markdownRef = ref(null)
const nav = useNavStore()

const { locale } = useI18n()
const route = useRoute()

const htmlContent = ref('')

const markdownFiles = import.meta.glob('../assets/posts/**/**/*.md', { query: '?raw', import: 'default' })

function makeUniqueNavItems (headings) {
  const result = []
  headings.forEach(h => {
    const id = h.id
    const text = h.textContent?.replace('¶', '').trim() || 'untitled'
    result.push({
      key: text,
      link: `#${id}`,
      faIcon: ['fas', 'heading'],
      disabled: false,
      type: 'md'
    })
  })
  return result
}

function extractMarkdownHeadings () {
  if (!markdownRef.value) return
  const headings = markdownRef.value.querySelectorAll('h1[id], h2[id]')
  const items = makeUniqueNavItems(headings)
  nav.setNavItems(items)
}

function observeHeaders () {
  if (observer) observer.disconnect()
  if (!markdownRef.value) return
  observer = new IntersectionObserver((entries) => {
    for (const entry of entries) {
      if (entry.isIntersecting) {
        const headingText = entry.target.textContent?.replace('¶', '').trim() || 'untitled'
        nav.setCurrentSection(headingText)
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
    if (nav.navItems.length) {
      nav.setMainSection(nav.navItems[0].link)
      nav.setCurrentSection(nav.navItems[0].key)
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
}

.md-content {
  max-width: 80%;
  margin: 0rem 0rem 1rem 0rem;
  padding: 0rem 2rem 2rem 2rem;
  border-radius: 10px;
  background-color: var(--card-bg);
  box-shadow: var(--card-box-shadow);
}
</style>
