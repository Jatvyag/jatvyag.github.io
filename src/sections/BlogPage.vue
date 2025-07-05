<script setup>
import { useI18n } from 'vue-i18n'
const { t, tm } = useI18n()

const props = defineProps({
    sectionLink: {
        type: String,
        required: true,
    }
})
</script>

<template>
  <section :id="props.sectionLink.replace('#', '')" class="section">
    <h1>Hello from blog</h1>
  </section>
</template>

<style scoped>
</style>
