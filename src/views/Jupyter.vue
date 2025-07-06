<script setup>
import { ref, onMounted, onUnmounted, nextTick, watch } from 'vue'
import JupyterPage from '../sections/JupyterPage.vue'

const emit = defineEmits([
  'update:mainSection', 
  'update:navMenuComponent',
  'update:currentSection',
  'update:navItems',
  'update:navMenuLangPage'
])

const navItems = [
  { key: 'home', link: '#home', faIcon: ['fas', 'house'], disabled: true }
]

const navMenuLangPage = 'navMenu.blog'

const currentSection = ref('')

function getLinkByKey(key) {
  const item = navItems.find(i => i.key === key)
  return item?.link || ''
}

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

onMounted(async () => {
  emit('update:mainSection', getLinkByKey('home'))
  emit('update:navItems', navItems)
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


</script>

<template>
  <main class="blog">
    <JupyterPage 
      :sectionLink="getLinkByKey('home')" 
    />
  </main>
</template>

<style scoped>
main.blog {
  display: flex;
  flex-flow: column;
  align-items: center;
}
</style>
