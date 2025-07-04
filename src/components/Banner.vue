<script setup>
import { useI18n } from 'vue-i18n'
import { watch, onMounted } from 'vue'
import Typewriter from 'typewriter-effect/dist/core'

const { tm, locale } = useI18n()

function startTypewriter() {
    const el = document.getElementById('typewriter')
    if (!el) return

    el.innerHTML = '' // Clear previous content
    new Typewriter(el, {
        strings: tm('banner'),
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