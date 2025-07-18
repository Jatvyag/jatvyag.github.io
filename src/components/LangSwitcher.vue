<template>
  <div class="lang-switcher">
    <button @click="toggleDropdown">
      {{ currentLabel }}
      <font-awesome-icon :icon="['fas', 'language']" />
      <font-awesome-icon
        :icon="['fas', 'chevron-down']"
        :class="['chevron-icon', { open: isOpen }]"
      />
    </button>
    <div
      v-if="isOpen"
      class="dropdown"
    >
      <button
        v-for="lang in languages"
        :key="lang.code"
        class="dropdown-item"
        :class="{ active: lang.code === locale }"
        @click="switchTo(lang.code)"
      >
        {{ lang.label }}
      </button>
    </div>
  </div>
</template>

<script setup>
import { useI18n } from 'vue-i18n'
import { ref, computed } from 'vue'

const { locale, t } = useI18n()
const isOpen = ref(false)

const toggleDropdown = () => {
  isOpen.value = !isOpen.value
}

const switchTo = (lang) => {
  locale.value = lang
  isOpen.value = false
  sessionStorage.setItem('locale', lang)
}
const languages = computed(() => [
  { code: 'en', label: t('languageNames.en') },
  { code: 'be', label: t('languageNames.be') }
])

const currentLabel = computed(() => {
  const match = languages.value.find(l => l.code === locale.value)
  return match?.label || locale.value
})
</script>

<style lang="scss" scoped>
.lang-switcher {
    position: relative;
    display: inline-block;
}

.chevron-icon {
    transition: transform 0.3s ease;
}

.chevron-icon.open {
    transform: rotate(180deg);
}

.dropdown {
    position: absolute;
    top: 100%;
    left: 1%;
    margin-top: 0.1rem;
    border-radius: $border-radius;
    box-shadow: var(--drop-down-box-shadow);
    background: var(--bg);
    z-index: 10;
}

.dropdown-item {
    display: block;
    padding: 0.4rem 0.8rem;
    width: 100%;
    text-align: left;
    background: none;
    border: 2px solid transparent;
    cursor: pointer;
}

.dropdown-item:hover,
.dropdown-item.active {
    border-color: var(--btn-hover-color);
    background-color: var(--btn-bg);
    border-radius: $border-radius;
}
</style>
