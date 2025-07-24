<template>
  <main
    ref="mainEl"
    class="about"
  >
    <About
      :section-link="getLinkByKey('about')"
      :next-section="getLinkByKey('skills')"
    />
    <Skills
      :section-link="getLinkByKey('skills')"
      :next-section="getLinkByKey('achievements')"
    />
    <Achievements
      :section-link="getLinkByKey('achievements')"
      :next-section="getLinkByKey('contacts')"
    />
    <Contacts
      :section-link="getLinkByKey('contacts')"
    />
  </main>
</template>

<script setup>
import { useTemplateRef, onMounted, onUnmounted } from 'vue'
import { useNavStore } from '@/stores/nav'
import About from '@/sections/About.vue'
import Skills from '@/sections/Skills.vue'
import Achievements from '@/sections/Achievements.vue'
import Contacts from '@/sections/Contacts.vue'

const main = useTemplateRef('mainEl')
const nav = useNavStore()

nav.setNavItems([
  { key: 'about', link: '#about', faIcon: ['fas', 'bars'], type: 'main_menu', disabled: false },
  { key: 'skills', link: '#skills', faIcon: ['fas', 'bars-progress'], type: 'main_menu', disabled: false },
  { key: 'achievements', link: '#achievements', faIcon: ['fas', 'award'], type: 'main_menu', disabled: false },
  { key: 'contacts', link: '#contacts', faIcon: ['fas', 'envelope-open-text'], type: 'main_menu', disabled: false }
])
nav.setCurrentSection('about')
nav.setMainSection(getLinkByKey('about'))
nav.setNavMenuLocale('navMenu.main')

function getLinkByKey (key) {
  const item = nav.navItems.find(i => i.key === key)
  return item?.link || ''
}

let observer = null

function observeSections () {
  if (observer) observer.disconnect()
  if (!main.value) return
  observer = new IntersectionObserver((entries) => {
    for (const entry of entries) {
      if (entry.isIntersecting) {
        nav.setCurrentSection(entry.target.id)
      }
    }
  }, {
    rootMargin: '0px',
    threshold: 0.3
  })
  main.value.querySelectorAll('section[id]').forEach(section => {
    observer.observe(section)
  })
}

onMounted(() => {
  nav.setMainSection(getLinkByKey('about'))
  observeSections()
})

onUnmounted(() => {
  if (observer) {
    observer.disconnect()
    observer = null
  }
})
</script>

<style scoped>
main.about {
  display: flex;
  flex-flow: column;
  align-items: center;
}
</style>
