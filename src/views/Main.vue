<template>
  <main class="about">
    <About 
      :sectionLink="getLinkByKey('about')" 
      :nextSection="getLinkByKey('skills')"
    />
    <Skills 
      :sectionLink="getLinkByKey('skills')" 
      :navMenuLangPage="navMenuLangPage" 
      :nextSection="getLinkByKey('achievements')"
    />
    <Achievements 
      :sectionLink="getLinkByKey('achievements')" 
      :navMenuLangPage="navMenuLangPage" 
      :nextSection="getLinkByKey('contacts')"
    />
    <Contacts 
      :sectionLink="getLinkByKey('contacts')" 
      :navMenuLangPage="navMenuLangPage" 
    />
  </main>
</template>

<script setup>
import { ref, onMounted, onUnmounted, nextTick, watch } from 'vue'
import About from '@/sections/About.vue'
import Skills from '@/sections/Skills.vue'
import Achievements from '@/sections/Achievements.vue'
import Contacts from '@/sections/Contacts.vue'

const emit = defineEmits([
  'update:mainSection', 
  'update:navMenuComponent',
  'update:currentSection',
  'update:navItems',
  'update:navMenuLangPage'
])

const navItems = [
  { key: 'about', link: '#about', faIcon: ['fas', 'bars'], type: "main_manu", disabled: false },
  { key: 'skills', link: '#skills', faIcon: ['fas', 'bars-progress'], type: "main_manu", disabled: false },
  { key: 'achievements', link: '#achievements', faIcon: ['fas', 'award'], type: "main_manu", disabled: false },
  { key: 'contacts', link: '#contacts', faIcon: ['fas', 'envelope-open-text'], type: "main_manu", disabled: false },
]

const navMenuLangPage = 'navMenu.main'

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
  emit('update:mainSection', getLinkByKey('about'))
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

<style scoped>
main.about {
  display: flex;
  flex-flow: column;
  align-items: center;
}
</style>
