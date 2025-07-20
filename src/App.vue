<template>
  <TopBar />
  <div v-if="isLocaleReady">
    <router-view v-slot="{ Component }">
      <component :is="Component" />
    </router-view>
  </div>
  <Footer />
</template>

<script setup>
import { computed, watch, onMounted } from 'vue'
import TopBar from '@/components/TopBar.vue'
import Footer from '@/components/Footer.vue'
import { useI18n } from 'vue-i18n'

const { locale, t, messages } = useI18n()

const isLocaleReady = computed(() => Boolean(messages.value?.[locale.value]))

function updateMetadata (lang) {
  document.documentElement.lang = lang
  document.title = t('app.title')
}

watch(locale, updateMetadata)
onMounted(() => updateMetadata(locale.value))
</script>

<style scoped>
</style>
