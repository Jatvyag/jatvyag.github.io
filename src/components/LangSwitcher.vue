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
        <button @click="toggleDropdown" class="lang-button">
            <span>{{ '\u{1F310}' }}   </span> {{ currentLabel }}
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
    position: fixed;
    top: 1rem;
    right: 1rem;
    text-align: right;
}

.lang-button {
    padding: 0.4rem 0.8rem;
    border-radius: 0.4rem;
    cursor: pointer;
    font-size: 1rem;
}

.dropdown {
    margin-top: 0.5rem;
    border-radius: 0.4rem;
    box-shadow: 0 0 5px rgba(0, 0, 0, 0.1);
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
    background: rgb(133, 133, 133);
}
</style>
