<script setup>
import About from './components/About.vue'
import LangSwitcher from './components/LangSwitcher.vue'
import { useI18n } from 'vue-i18n'
const { t } = useI18n()
</script>

<template>
  <LangSwitcher />
  <About :msg="t('about.myName')" />
</template>

<style scoped>
</style>
