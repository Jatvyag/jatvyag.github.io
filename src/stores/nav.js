import { defineStore } from 'pinia'
import { ref } from 'vue'

export const useNavStore = defineStore('nav', () => {
  /**
   * @typedef {Object} NavItem
   * @property {number} navItemId - the id of the navigation item
   * @property {string} translateKey - the i18n key of the section title
   * @property {string} translatedLabel - the label from the MD or iFrame itself
   * @property {string} idLink - the container id of the heading
   * @property {ref} sectionRef - the ref of the section
   * @property {Array<string>} faIcon - FontAwesome icon name
   * @property {boolean} isDisabled - the marker for disabled sections
   * @property {string} navType - the type of the section
   */

  const navItems = ref([]) /** @type {NavItem[]} */
  const currentSectionTitle = ref(null)
  const navMenuLocale = ref('')

  const setNavItems = (items) => (navItems.value = items)
  const setCurrentSectionTitle = (section) => (currentSectionTitle.value = section)
  const setNavMenuLocale = (locale) => (navMenuLocale.value = locale)

  return {
    navItems,
    currentSectionTitle,
    navMenuLocale,
    setNavItems,
    setCurrentSectionTitle,
    setNavMenuLocale
  }
})
