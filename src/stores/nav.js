import { defineStore } from 'pinia'

export const useNavStore = defineStore('nav', {
  state: () => ({
    navItems: [],
    currentSection: '',
    mainSection: '',
    navMenuLocale: ''
  }),
  actions: {
    setNavItems (navItems) {
      this.navItems = navItems
    },
    setCurrentSection (currentSection) {
      this.currentSection = currentSection
    },
    setMainSection (mainSection) {
      this.mainSection = mainSection
    },
    setNavMenuLocale (navMenuLocale) {
      this.navMenuLocale = navMenuLocale
    }
  }
})
