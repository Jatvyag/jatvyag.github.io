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
    { code: 'be', label: t('languageNames.be') },
])

const currentLabel = computed(() => {
    const match = languages.value.find(l => l.code === locale.value)
    return match?.label || locale.value
})
</script>

<template>
    <div class="lang-switcher">
        <button @click="toggleDropdown">
            {{ currentLabel }} <font-awesome-icon :icon="['fas', 'language']" />
        </button>
        <div v-if="isOpen" class="dropdown">
            <button
                v-for="lang in languages"
                :key="lang.code"
                @click="switchTo(lang.code)"
                class="dropdown-item"
                :class="{ active: lang.code === locale }"
            >
                {{ lang.label }}
            </button>
        </div>
    </div>
</template>

<style scoped>
.lang-switcher {
    position: relative;
    display: inline-block;
}

.dropdown {
    position: absolute;
    top: 100%;
    left: 1%;
    margin-top: 0.1rem;
    border-radius: 0.6rem;
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
    border: none;
    cursor: pointer;
}

.dropdown-item:hover,
.dropdown-item.active {
    background: var(--btn-hover-color);
    color: white;
}
</style>
