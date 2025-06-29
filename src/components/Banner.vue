<script setup>
import { useI18n } from 'vue-i18n'
import { computed, watch, onMounted } from 'vue'
import enData from '../data/en.json'
import beData from '../data/be.json'
import Typewriter from 'typewriter-effect/dist/core'

const { locale } = useI18n()

const dataMap = {
    en: enData,
    be: beData,
}

const currentData = computed(() => dataMap[locale.value] || enData)

function startTypewriter() {
    const el = document.getElementById('typewriter')
    if (!el) return

    el.innerHTML = '' // Clear previous content
    new Typewriter(el, {
        strings: currentData.value.banner.titles,
        autoStart: true,
        loop: true,
        deleteSpeed: 5,
    })
}

onMounted(() => {
    startTypewriter()
})

watch(locale, () => {
    startTypewriter()
})
</script>

<template>
    <div>
        <h2 id="typewriter"></h2>
    </div>
</template>

<style scoped>
</style>