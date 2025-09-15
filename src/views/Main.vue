<template>
  <main
    ref="mainEl"
    class="about"
  >
    <About
      :section-link="getMainSectionByKey('about')"
      :next-section="getMainSectionByKey('skills')"
    />
    <Skills
      :section-link="getMainSectionByKey('skills')"
      :next-section="getMainSectionByKey('achievements')"
    />
    <Achievements
      :section-link="getMainSectionByKey('achievements')"
      :next-section="getMainSectionByKey('contacts')"
    />
    <Contacts
      :section-link="getMainSectionByKey('contacts')"
    />
  </main>
</template>

<script setup>
import { ref, onMounted, onUnmounted } from 'vue'
import { useNavStore } from '@/stores/nav'
import About from '@/sections/About.vue'
import Skills from '@/sections/Skills.vue'
import Achievements from '@/sections/Achievements.vue'
import Contacts from '@/sections/Contacts.vue'

// Section keys
const sectionKeys = ['about', 'skills', 'achievements', 'contacts']

// Generate refs dynamically
const sectionRef = Object.fromEntries(
  sectionKeys.map(key => [key, ref(null)])
)

const navStore = useNavStore()
navStore.setNavItems([
  { key: 'about', link: sectionRef.about, faIcon: ['fas', 'bars'], type: 'main_menu', disabled: false },
  { key: 'skills', link: sectionRef.skills, faIcon: ['fas', 'bars-progress'], type: 'main_menu', disabled: false },
  { key: 'achievements', link: sectionRef.achievements, faIcon: ['fas', 'award'], type: 'main_menu', disabled: false },
  { key: 'contacts', link: sectionRef.contacts, faIcon: ['fas', 'envelope-open-text'], type: 'main_menu', disabled: false }
])
navStore.setCurrentSection('about')
navStore.setMainSection(getMainSectionByKey('about'))
navStore.setNavMenuLocale('navMenu.main')

function getMainSectionByKey (key) {
  return sectionRef[key] || null
}

let observer = null

function observeSections () {
  if (observer) observer.disconnect()

  observer = new IntersectionObserver((entries) => {
    for (const entry of entries) {
      if (entry.isIntersecting) {
        // Updates the currentSection in your navigation store
        navStore.setCurrentSection(entry.target.dataset.key)
      }
    }
  }, {
    rootMargin: '0px',
    threshold: 0.3
  })

  // Observe each section by Vue's ref
  sectionKeys.forEach(key => {
    const el = sectionRef[key].value
    if (el) {
      // Add an attribute so we know which section triggered
      el.dataset.key = key
      // Start observing this element for intersection changes
      observer.observe(el)
    }
  })
}

onMounted(() => {
  observeSections()
})

onUnmounted(() => {
  if (observer) {
    observer.disconnect()
    observer = null
  }
})
</script>

<style lang="scss" scoped>
main.about {
  display: flex;
  flex-flow: column;
  align-items: center;
}
</style>
