<script setup>
import { watch, onMounted } from 'vue'
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
  <div class="top-lang-theme-bar">
    <LangSwitcher /> 
    <ThemeSwitcher />       
  </div>
  <About :msg="t('about.myName')" />
</template>

<style scoped>
.top-lang-theme-bar {
  display: flex;
  justify-content: flex-end; /* or space-between / center */
  align-items: center;
  gap: 1rem; /* spacing between buttons */
  padding: 1rem;
}
</style>
