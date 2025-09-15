import { defineStore } from 'pinia'
import { ref } from 'vue'

export const useNavStore = defineStore('nav', () => {
  const navItems = ref([])
  const currentSection = ref(null)
  const mainSection = ref(null)
  const navMenuLocale = ref('')

  const setNavItems = (items) => (navItems.value = items)
  const setCurrentSection = (section) => (currentSection.value = section)
  const setMainSection = (section) => (mainSection.value = section)
  const setNavMenuLocale = (locale) => (navMenuLocale.value = locale)

  return {
    navItems,
    currentSection,
    mainSection,
    navMenuLocale,
    setNavItems,
    setCurrentSection,
    setMainSection,
    setNavMenuLocale
  }
})
