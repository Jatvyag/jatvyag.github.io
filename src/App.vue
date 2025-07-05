<script setup>
import { ref, computed, watch, onMounted } from 'vue'
import TopBar from './components/TopBar.vue'
import Footer from './components/Footer.vue'
import { useI18n } from 'vue-i18n'

const { locale, t, messages } = useI18n()

const navItems = ref([])
const currentSection = ref('')
const mainSection = ref('')
const navMenuLangPage = ref('')

const isLocaleReady = computed(() => Boolean(messages.value?.[locale.value]))

function updateMetadata(lang) {
  document.documentElement.lang = lang
  document.title = t('app.title')
}

watch(locale, updateMetadata)
onMounted(() => updateMetadata(locale.value))
</script>

<template>
  <TopBar 
    :navItems="navItems"
    :currentSection="currentSection"
    :navMenuLangPage="navMenuLangPage"
    @update:currentSection="currentSection = $event" 
  />
  <div v-if="isLocaleReady">
    <router-view
      v-slot="{ Component }"
      @update:navItems="navItems = $event"
      @update:currentSection="currentSection = $event"
      @update:mainSection="mainSection = $event"
      @update:navMenuLangPage="navMenuLangPage = $event"
    >
      <component
        :is="Component"
        :currentSection="currentSection"
        :navItems="navItems"
      />
    </router-view>
  </div>
  <Footer :mainSection="mainSection" />
</template>

<style scoped>
</style>
