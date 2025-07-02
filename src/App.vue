<script setup>
import { ref, watch, onMounted, onUnmounted, nextTick } from 'vue'
import NavMenu from './components/NavMenu.vue'
import LangSwitcher from './components/LangSwitcher.vue'
import ThemeSwitcher from './components/ThemeSwitcher.vue'
import About from './sections/About.vue'
import Skills from './sections/Skills.vue'
import Achievements from './sections/Achievements.vue'
import Footer from './components/Footer.vue'
import { useI18n } from 'vue-i18n'
import Contact from './sections/Contact.vue'

const { locale, t } = useI18n()

function updateMetadata(lang) {
  document.documentElement.lang = lang
  document.title = t('app.title')
}

const currentSection = ref('main')

const navItems = [
    { key: 'main', link: '#main', faIcon: ['fas', 'bars'], disabled: false },
    { key: 'skills', link: '#skills', faIcon: ['fas', 'bars-progress'], disabled: false },
    { key: 'achievements', link: '#achievements', faIcon: ['fas', 'award'], disabled: false },
    { key: 'contacts', link: '#contacts', faIcon: ['fas', 'envelope-open-text'], disabled: false },
]

const observeSections = () => {
  const observer = new IntersectionObserver(
    (entries) => {
      for (const entry of entries) {
        if (entry.isIntersecting) {
          currentSection.value = entry.target.id
        }
      }
    },
    {
      rootMargin: '0px',
      threshold: 0.1,
    }
  )
  document.querySelectorAll('main section[id]').forEach((section) => {
    observer.observe(section)
  })
  return observer
}

let observer = null

watch(locale, (newLocale) => {
  updateMetadata(newLocale)
})

onMounted(async () => {
  updateMetadata(locale.value)
  await nextTick()
  observer = observeSections()   
})

onUnmounted(() => {
  if (observer) {
    observer.disconnect()
  }
})
</script>

<template>
  <div class="top-bar">
    <NavMenu v-model:currentSection="currentSection" :navItems="navItems" />
    <div class="top-lang-theme-bar">
      <LangSwitcher />
      <ThemeSwitcher />   
    </div>
  </div>
  <!-- Main Page Sections -->
  <main>
    <About />
    <Skills />
    <Achievements />
    <Contact />
  </main>
  <Footer />
</template>

<style scoped>
.top-bar {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  background-color: var(--bg); 
  z-index: 1000;
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 0.3rem 0.3rem 0.3rem 0.3rem;
  box-shadow: var(--drop-down-box-shadow);
}

.top-lang-theme-bar {
  display: flex;
  justify-content: flex-end; /* or space-between / center */
  align-items: center;
  gap: 0.5rem; /* spacing between buttons */
  padding: 0.3rem 1rem 0.3rem 0.3rem;
}
</style>
