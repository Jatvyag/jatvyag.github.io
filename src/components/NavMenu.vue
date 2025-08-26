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
          v-for="item in navStore.navItems"
          :key="item.key"
          :class="{ active: item.key === navStore.currentSection, disabled: item.disabled }"
          @click="handleNavigation(item)"
        >
          <!-- Icons of side menu -->
          <template v-if="!isJupyterMD">
            <font-awesome-icon
              v-if="item.faIcon"
              :icon="item.faIcon"
            />
            <span v-else>{{ item.unicodeIcon }}</span>
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
import { useI18n } from 'vue-i18n'
import { useNavStore, useJupyterStore } from '@/stores'
import { NavItemEnumTypes } from '@/constants'

const { t } = useI18n()

// Navigation elements
const navStore = useNavStore()
const jupyterStore = useJupyterStore()

// The type of the first navigation item
const firstNavItemType = computed(() => {
  return navStore.navItems[0]?.type
})

// The toggle menu functionality
const isOpen = ref(false)

function toggleMenu () {
  isOpen.value = !isOpen.value
}

function handleNavigation (item) {
  if (item.disabled) return
  const hash = item.link
  if (!hash || !hash.startsWith('#')) return
  nextTick(() => {
    let el = null
    if (item.type === NavItemEnumTypes.JUPYTER) {
      if (jupyterStore.iframeDoc) {
        el = jupyterStore.iframeDoc.querySelector(hash)
      }
    } else {
      el = document.querySelector(hash)
    }
    if (el) {
      el.scrollIntoView({ behavior: 'smooth' })
      navStore.setCurrentSection(item.key)
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
  if (Object.values(NavItemEnumTypes).includes(item.type)) {
    return item.key
  } else {
    // If there is not 'md' or 'jupyter' type, then it is from i18n
    return t(`${navStore.navMenuLocale}.${item.key}`)
  }
}

const activeItem = computed(() => {
  return navStore.navItems.find(item => item.key === navStore.currentSection)
})

const isJupyterMD = computed(() => {
  return navStore.navItems.some(item =>
    item.type === NavItemEnumTypes.JUPYTER ||
    item.type === NavItemEnumTypes.MD
  )
})

// The font-awesome icon needed for default menu (not for Jupyter or Markdown)
const currentIcon = computed(() => {
  return activeItem.value?.faIcon || ['fas', 'bars']
})

const currentTitle = computed(() => {
  // Case 1: Jupyter/Markdown with section
  if (isJupyterMD.value && navStore.currentSection) {
    return navStore.currentSection
  }
  // Case 2: Jupyter/Markdown without section
  if (isJupyterMD.value && !navStore.currentSection) {
    return firstNavItemType.value === NavItemEnumTypes.MD ? 'Markdown' : 'Jupyter'
  }
  // Case 3: Title of section
  if (navStore.navMenuLocale && navStore.currentSection) {
    const key = `${navStore.navMenuLocale}.${navStore.currentSection}`
    return t(key, navStore.currentSection)
  }
  // Empty title
  return ''
})

const isDisabledMenuBtn = computed(() => {
  return navStore.navItems.length <= 1
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
