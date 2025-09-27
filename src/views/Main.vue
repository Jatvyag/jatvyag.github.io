<template>
  <main
    ref="mainEl"
    class="about"
  >
    <About
      :section-link="sectionRefs.about"
      :next-section="sectionRefs.skills"
    />
    <Skills
      :section-link="sectionRefs.skills"
      :next-section="sectionRefs.achievements"
    />
    <Achievements
      :section-link="sectionRefs.achievements"
      :next-section="sectionRefs.contacts"
    />
    <Contacts
      :section-link="sectionRefs.contacts"
    />
  </main>
</template>

<script setup>
import { ref, onMounted, onUnmounted } from 'vue'
import { useNavStore } from '@/stores/nav'
import { NavItemEnumTypes } from '@/constants'
import About from '@/sections/About.vue'
import Skills from '@/sections/Skills.vue'
import Achievements from '@/sections/Achievements.vue'
import Contacts from '@/sections/Contacts.vue'

// Section keys
const sectionKeys = ['about', 'skills', 'achievements', 'contacts']

// Generate refs dynamically
const sectionRefs = Object.fromEntries(
  sectionKeys.map(key => [key, ref(null)])
)

// Stores
const navStore = useNavStore()

// Getters
const {
  setNavItems,
  setCurrentSectionTitle,
  setNavMenuLocale
} = navStore

// Generate navigation items
setNavItems([
  {
    navItemId: 1,
    translateKey: 'about',
    sectionRef: sectionRefs.about,
    faIcon: ['fas', 'bars'],
    isDisabled: false,
    navType: NavItemEnumTypes.MAIN
  },
  {
    navItemId: 2,
    translateKey: 'skills',
    sectionRef: sectionRefs.skills,
    faIcon: ['fas', 'bars-progress'],
    isDisabled: false,
    navType: NavItemEnumTypes.MAIN
  },
  {
    navItemId: 3,
    translateKey: 'achievements',
    sectionRef: sectionRefs.achievements,
    faIcon: ['fas', 'award'],
    isDisabled: false,
    navType: NavItemEnumTypes.MAIN
  },
  {
    navItemId: 4,
    translateKey: 'contacts',
    sectionRef: sectionRefs.contacts,
    faIcon: ['fas', 'envelope-open-text'],
    isDisabled: false,
    navType: NavItemEnumTypes.MAIN
  }
])

setCurrentSectionTitle('about')

setNavMenuLocale('navMenu.main')

let observer = null

/**
 * Observes sections
 */
function observeSections () {
  if (observer) observer.disconnect()

  observer = new IntersectionObserver((entries) => {
    for (const entry of entries) {
      if (entry.isIntersecting) {
        // Updates the setCurrentSectionTitle in your navigation store
        setCurrentSectionTitle(entry.target.dataset.translateKey)
      }
    }
  }, {
    rootMargin: '0px',
    threshold: 0.3
  })

  // Observe each section by Vue's ref
  sectionKeys.forEach(key => {
    const el = sectionRefs[key].value
    if (el) {
      // Add an attribute so we know which section triggered
      el.dataset.translateKey = key
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
