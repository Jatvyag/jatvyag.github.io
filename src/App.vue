<script setup>
import About from './components/About.vue'
import LangSwitcher from './components/LangSwitcher.vue'
import ThemeSwitcher from './components/ThemeSwitcher.vue'
import { useI18n } from 'vue-i18n'
const { t } = useI18n()
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
