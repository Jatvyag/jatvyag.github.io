<template>
  <button
    class="lang-btn"
    @click="cycleLanguage"
  >
    <Transition
      name="slide-up"
      mode="out-in"
    >
      <span :key="locale">
        {{ currentLabel }}
      </span>
    </Transition>
    <font-awesome-icon
      :icon="['fas', 'language']"
      class="lang-icon"
    />
  </button>
</template>

<script setup>
import { useI18n } from 'vue-i18n'
import { computed } from 'vue'

const { locale, t } = useI18n()

const languageOptions = [
  { code: 'en', label: () => t('languageNames.en') },
  { code: 'be', label: () => t('languageNames.be') }
]

const cycleLanguage = () => {
  const currentIndex = languageOptions.findIndex(lang => lang.code === locale.value)
  const nextIndex = (currentIndex + 1) % languageOptions.length
  const nextLang = languageOptions[nextIndex].code
  locale.value = nextLang
  sessionStorage.setItem('locale', nextLang)
}

const currentLabel = computed(() => {
  const match = languageOptions.find(lang => lang.code === locale.value)
  return match ? match.label() : locale.value
})
</script>

<style lang="scss" scoped>
.lang-icon {
  width: 3rem;
  height: 1.75em;
  padding: 0rem;
  margin: 0rem;
}
.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.3s ease;
}
.fade-enter-from,
.fade-leave-to {
  opacity: 0;
}
.lang-btn {
  width: 6rem;
  height: 1.9rem;
  gap: 0.5rem;
  padding: 0.3rem 1rem 0.3rem 0.3rem;
}
</style>
