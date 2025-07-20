<template>
  <div class="nav-wrapper">
    <button
      class="menu-btn"
      :disabled="nav.navItems.length <= 1"
      @click="toggleMenu"
    >
      <template v-if="isJupyter">
        <img
          :src="jupyterIcon"
          alt="Jupyter"
          class="jupyter-icon"
        >
      </template>
      <template v-else>
        <font-awesome-icon :icon="currentIcon" />
      </template>
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
      <ul>
        <li
          v-for="item in nav.navItems"
          :key="item.key"
          :class="{ active: item.key === nav.currentSection, disabled: item.disabled }"
          @click="handleNavigation(item)"
        >
          <!-- Icon for non-jupyter -->
          <template v-if="item.type !== 'jupyter'">
            <font-awesome-icon
              v-if="item.faIcon"
              :icon="item.faIcon"
            />
            <span v-else>{{ item.unicodeIcon }}</span>
          </template>
          <span>
            {{ item.type === 'jupyter' ? item.key : t(`${nav.navMenuLocale}.${item.key}`) }}
          </span>
        </li>
      </ul>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, nextTick } from 'vue'
import { useI18n } from 'vue-i18n'
import { useNavStore } from '@/stores/nav'

const nav = useNavStore()

const { t } = useI18n()
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
    if (item.type === 'jupyter') {
      const iframe = document.querySelector('iframe')
      const iframeDoc = iframe?.contentDocument || iframe?.contentWindow?.document
      if (iframeDoc) {
        el = iframeDoc.querySelector(hash)
      }
    } else {
      el = document.querySelector(hash)
    }
    if (el) {
      el.scrollIntoView({ behavior: 'smooth' })
      nav.setCurrentSection(item.key)
      isOpen.value = false
    }
  })
}

const jupyterIcon = new URL('@/assets/icons/jupyter.svg', import.meta.url).href

const activeItem = computed(() => {
  return nav.navItems.find(item => item.key === nav.currentSection)
})

const isJupyter = computed(() => {
  return nav.navItems.some(item => item.type === 'jupyter')
})

const currentIcon = computed(() => {
  return activeItem.value?.faIcon || ['fas', 'bars']
})

const currentTitle = computed(() => {
  if (isJupyter.value && nav.currentSection) {
    return nav.currentSection
  } else if (isJupyter.value && !nav.currentSection) {
    const icon = 'Jupyter'
    return icon
  }
  if (nav.navMenuLocale && nav.currentSection) {
    const key = `${nav.navMenuLocale}.${nav.currentSection}`
    return t(key, nav.currentSection)
  }
  return ''
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
    border-color: var(--btn-hover-color);
    background-color: var(--btn-bg);
    border-radius: $border-radius;
}

.menu-btn:disabled {
    opacity: 0.5;
    border: 2px solid transparent;
    background: none;
    cursor: not-allowed;
    transform: scale(1);
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
    background-color: var(--bg);
    color: var(--text-color);
    padding-top: 2rem;
    padding-left: 1rem;
    transition: transform 0.3s ease;
    z-index: 1000;
    box-shadow: var(--drop-down-box-shadow);
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
    border-color: var(--btn-hover-color);
    background-color: var(--btn-bg);
    border-radius: $border-radius;
}

.side-menu li.disabled {
    opacity: 0.5;
    pointer-events: none;
}

.jupyter-icon {
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
