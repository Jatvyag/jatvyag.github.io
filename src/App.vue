<template>
  <TopBar
    :nav-items="navItems"
    :current-section="currentSection"
    :nav-menu-lang-page="navMenuLangPage"
    @update:current-section="currentSection = $event"
  />
  <div v-if="isLocaleReady">
    <router-view
      v-slot="{ Component }"
      @update:nav-items="navItems = $event"
      @update:current-section="currentSection = $event"
      @update:main-section="mainSection = $event"
      @update:nav-menu-lang-page="navMenuLangPage = $event"
    >
      <component
        :is="Component"
        :current-section="currentSection"
        :nav-items="navItems"
      />
    </router-view>
  </div>
  <Footer :main-section="mainSection" />
</template>

<script setup>
import { ref, computed, watch, onMounted } from 'vue'
import TopBar from '@/components/TopBar.vue'
import Footer from '@/components/Footer.vue'
import { useI18n } from 'vue-i18n'

const { locale, t, messages } = useI18n()

const navItems = ref([])
const currentSection = ref('')
const mainSection = ref('')
const navMenuLangPage = ref('')

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
