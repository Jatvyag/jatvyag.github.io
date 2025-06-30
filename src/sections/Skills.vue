<script setup>
import { useI18n } from 'vue-i18n'
const { t, tm } = useI18n()
function scrollToPrevSection() {
    const previous = document.querySelector('#main') 
    if (previous) previous.scrollIntoView({ behavior: 'smooth' })
}
</script>

<template>
    <section id="skills" class="section">
        <div class="scroll-up" @click="scrollToPrevSection">{{ '\u{2303}' }}</div>
        <h2>{{ t('skills.header') }}</h2>
        <div class="content">
        <p>Some text...</p>
        <p>Some text...</p>
        <p>Some text...</p>
        <p>Some text...</p>
        <p>Some text...</p>
        <p>Some text...</p>
        <p>Some text...</p>
        <p>Some text...</p>
        <p>Some text...</p>
        <p>Some text...</p>
        <p>Some text...</p>
        <p>Some text...</p>
        <p>Some text...</p>
        <p>Some text...</p>
        <p>Some text...</p>
        <p>Some text...</p>
        <p>Some text...</p>
        <p>Some text...</p>
        <p>Some text...</p>
        <p>Some text...</p>
        </div>
    </section>
</template>

<style scoped>
</style>
