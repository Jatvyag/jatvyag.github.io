<template>
  <div class="nav-wrapper">
    <!--  Main menu button  -->
    <button
      class="menu-btn"
      :disabled="isDisabledMenuBtn"
      @click="toggleMenu"
    >
      <img
        v-if="isJupyterMD"
        :src="jupyterMDIcon"
        class="jupyter-md-icon"
      >
      <font-awesome-icon
        v-else
        :icon="currentIcon"
      />
      <span class="page-title">{{ currentTitle }}</span>
    </button>
    <!-- Backdrop -->
    <div
      v-if="isOpen"
      class="backdrop"
      @click="toggleMenu"
    />
    <!-- Side Menu -->
    <div
      class="side-menu"
      :class="{ open: isOpen }"
    >
      <!-- Items of side menu -->
      <ul>
        <li
          v-for="item in navItems"
          :key="item.navItemId"
          :class="{ active: isActiveMenuItem(item), disabled: item.isDisabled }"
          @click="handleNavigation(item)"
        >
          <!-- Icons of side menu -->
          <template v-if="!isJupyterMD">
            <font-awesome-icon
              v-if="item.faIcon"
              :icon="item.faIcon"
            />
          </template>
          <!-- Label of side menu -->
          <span>
            {{ sideMenuLabel(item) }}
          </span>
        </li>
      </ul>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, nextTick } from 'vue'
import { storeToRefs } from 'pinia'
import { useI18n } from 'vue-i18n'
import { useNavStore, useJupyterStore } from '@/stores'
import { NavItemEnumTypes } from '@/constants'

const { t } = useI18n()

// Stores
const navStore = useNavStore()
const jupyterStore = useJupyterStore()

// Refs
const { iframeDoc } = storeToRefs(jupyterStore)
const {
  navItems,
  currentSectionTitle,
  navMenuLocale
} = storeToRefs(navStore)

// Getters
const { setCurrentSectionTitle } = navStore

// The type of the first navigation item
const firstNavItemType = computed(() => {
  return navItems.value[0]?.navType
})

// The toggle menu functionality
const isOpen = ref(false)

function toggleMenu () {
  isOpen.value = !isOpen.value
}

function isActiveMenuItem (item) {
  if ([NavItemEnumTypes.MD, NavItemEnumTypes.JUPYTER].includes(item.navType)) {
    return item.translatedLabel === currentSectionTitle.value
  } else {
    return item.translateKey === currentSectionTitle.value
  }
}

function handleNavigation (item) {
  if (item.isDisabled) return
  nextTick(() => {
    let activeLink = null
    if (item.navType === NavItemEnumTypes.JUPYTER) {
      if (iframeDoc.value) {
        activeLink = iframeDoc.value.querySelector(item.idLink)
      }
      setCurrentSectionTitle(item.translateKey)
    } else if (item.navType === NavItemEnumTypes.MD) {
      activeLink = document.querySelector(item.idLink)
      setCurrentSectionTitle(item.translatedLabel)
    } else {
      activeLink = item.sectionRef
      setCurrentSectionTitle(item.translatedLabel)
    }
    if (activeLink) {
      activeLink.scrollIntoView({ behavior: 'smooth' })
      isOpen.value = false
    }
  })
}

const jupyterMDIcon = computed(() => {
  if (firstNavItemType.value === NavItemEnumTypes.MD) {
    return new URL('@/assets/icons/markdown.svg', import.meta.url).href
  }
  if (firstNavItemType.value === NavItemEnumTypes.JUPYTER) {
    return new URL('@/assets/icons/jupyter.svg', import.meta.url).href
  }
  // No need for icon if it is not 'md' or 'jupyter' type
  return ''
})

function sideMenuLabel (item) {
  // Returns the item key of label
  if ([NavItemEnumTypes.MD, NavItemEnumTypes.JUPYTER].includes(item.navType)) {
    return item.translatedLabel
  } else {
    // If it is not 'md' or 'jupyter' type, then it is from i18n
    return t(`${navMenuLocale.value}.${item.translateKey}`)
  }
}

const isJupyterMD = computed(() => {
  return navItems.value.some(item =>
    item.navType === NavItemEnumTypes.JUPYTER ||
    item.navType === NavItemEnumTypes.MD
  )
})

// The font-awesome icon needed for default menu (not for Jupyter or Markdown)
const currentIcon = computed(() => {
  const activeItem = navItems.value.find(item => item.translateKey === currentSectionTitle.value)
  return activeItem?.faIcon || ['fas', 'bars']
})

const currentTitle = computed(() => {
  // Case 1: Jupyter/Markdown with section
  if (isJupyterMD.value && currentSectionTitle.value) {
    return currentSectionTitle.value
  }
  // Case 2: Jupyter/Markdown without section
  if (isJupyterMD.value && !currentSectionTitle.value) {
    return firstNavItemType.value === NavItemEnumTypes.MD ? 'Markdown' : 'Jupyter'
  }
  // Case 3: Title of section
  if (navMenuLocale.value && currentSectionTitle.value) {
    const key = `${navMenuLocale.value}.${currentSectionTitle.value}`
    return t(key, currentSectionTitle.value)
  }
  // Empty title
  return ''
})

const isDisabledMenuBtn = computed(() => {
  return navItems.value.length <= 1
})
</script>

<style lang="scss" scoped>
.nav-wrapper {
    display: flex;
    align-items: center;
    gap: 0.5rem;
    position: relative;
    flex-shrink: 1;
    flex-grow: 0;
    min-width: 0;
}

.menu-btn {
    display: flex;
    align-items: center;
    font-size: 1.5rem;
    gap: 0.5rem;
    min-width: 0;
    border: 2px solid transparent;
    background: none;
    cursor: pointer;
}

.menu-btn:hover {
    border-color: var(--btn-hover);
    background-color: var(--btn-bg);
    border-radius: 10px;
}

.menu-btn:disabled {
    opacity: 0.5;
    border: 2px solid transparent;
    background: none;
    cursor: not-allowed;
}

.page-title {
    display: inline-block;
    max-width: 100%;
    font-weight: bold;
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
}

.backdrop {
    position: fixed;
    top: 0;
    left: 0;
    width: 100vw;
    height: 100vh;
    background-color: rgba(0, 0, 0, 0.4);
    z-index: 999; /* below side-menu (1000) */
}

.side-menu {
    position: fixed;
    top: 0;
    left: 0;
    height: 100vh;
    width: 240px;
    background-color: var(--body-bg);
    color: var(--body-txt);
    padding-top: 2rem;
    padding-left: 1rem;
    transition: transform 0.3s ease;
    z-index: 1000;
    box-shadow: var(--drop-down-shadow);
    transform: translateX(-100%);
}

.side-menu.open {
    left: 0;
    top: 0;
    padding-top: 2rem;
    overflow-y: auto;
    max-height: 100vh;
    transform: translateX(0);
}

.side-menu ul {
    list-style: none;
    padding: 0;
    margin: 0;
}

.side-menu li {
    padding: 0.5rem;
    margin-right: 1rem;
    display: flex;
    cursor: pointer;
    gap: 0.5rem;
    align-items: center;
    border: 2px solid transparent;
}

.side-menu li.active,
.side-menu li:hover {
    border-color: var(--btn-hover);
    background-color: var(--btn-bg);
    border-radius: 10px;
}

.side-menu li.disabled {
    opacity: 0.5;
    pointer-events: none;
}

.jupyter-md-icon {
    width: 1em;
    height: 1em;
    margin-right: 0.5em;
    flex-shrink: 0;
    display: inline-block;
}

@media (max-width: 600px) {
    .side-menu {
        width: 50vw;
    }
}

@media (min-width: 601px) and (max-width: 1024px) {
    .side-menu {
        width: 50vw;
    }
}
</style>
