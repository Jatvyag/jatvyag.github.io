<script setup>
import { useI18n } from 'vue-i18n'

const { t, tm } = useI18n()

function scrollToMain() {
    const next = document.querySelector('#main') 
    if (next) next.scrollIntoView({ behavior: 'smooth' })
}
</script>

<template>
    <section id="contacts" class="section">
        <h2>{{ t('navMenu.contacts') }}</h2>
        <p>Some text...</p>
        <font-awesome-icon :icon="['fas', 'chevron-up']" class="chevron" @click="scrollToMain" />
    </section>
</template>

<style scoped>
</style>

