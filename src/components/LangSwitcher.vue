<template>
  <Transition
    name="slide-up"
    mode="out-in"
  >
    <div
      v-if="locale"
      :key="locale"
      class="lang-btn"
      @click="cycleLanguage"
    >
      <span lang-label>
        {{ currentLabel }}
      </span>
      <font-awesome-icon
        :icon="['fas', 'language']"
        class="lang-icon"
      />
    </div>
  </Transition>
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
.slide-up-enter-active,
.slide-up-leave-active {
  transition: all 0.25s ease-out;
}

.slide-up-enter-from {
  opacity: 0;
  transform: translateY(30px);
}

.slide-up-leave-to {
  opacity: 0;
  transform: translateY(-30px);
}

.lang-btn {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  width: 3rem;
  margin-right: 2rem;
}

.lang-btn:hover {
    color: var(--btn-hover);
    transition: color 0.3s;
}

.lang-icon {
  height: 2rem;
}
</style>
