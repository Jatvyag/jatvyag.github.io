<script setup>
import { watch, onMounted } from 'vue'
import NavMenu from './components/NavMenu.vue'
import About from './components/About.vue'
import LangSwitcher from './components/LangSwitcher.vue'
import ThemeSwitcher from './components/ThemeSwitcher.vue'
import { useI18n } from 'vue-i18n'
const { locale, t } = useI18n()

function updateMetadata(lang) {
  document.documentElement.lang = lang
  document.title = t('app.title')
}

watch(locale, (newLocale) => {
  updateMetadata(newLocale)
})

onMounted(() => {
  updateMetadata(locale.value)
})
</script>

<template>
  <div class="top-bar">
    <NavMenu />
    <div class="top-lang-theme-bar">
      <LangSwitcher />
      <ThemeSwitcher />   
    </div>
  </div>
  <About :msg="t('about.my_name')" />
</template>

<style scoped>
.top-bar {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 0.1rem 0.5rem;
}

.top-lang-theme-bar {
  display: flex;
  justify-content: flex-end; /* or space-between / center */
  align-items: center;
  gap: 0.5rem; /* spacing between buttons */
  padding: 0.1rem;
}
</style>
