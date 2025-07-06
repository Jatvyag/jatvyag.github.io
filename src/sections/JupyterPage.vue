<script setup>
import { ref, watch, onMounted, onBeforeUnmount } from 'vue'

const props = defineProps({
    sectionLink: {
        type: String,
        required: true,
    },
})

const theme = ref(sessionStorage.getItem('theme') || 'dark')
const iframeSrc = ref(`/notebooks/${theme.value}/analyse_tv.html`)

function onThemeChange(e) {
    theme.value = e.detail.theme
}

watch(theme, (newTheme) => {
    iframeSrc.value = `/notebooks/${newTheme}/analyse_tv.html`
})

onMounted(() => {
    window.addEventListener('theme-changed', onThemeChange)
})

onBeforeUnmount(() => {
    window.removeEventListener('theme-changed', onThemeChange)
})
</script>

<template>
    <section :id="props.sectionLink.replace('#', '')" class="jupyter-section">
        <h1 class="blog">Jupyter Notebook</h1>
        <iframe 
            :src="iframeSrc" 
            frameborder="0" 
            sandbox="allow-same-origin allow-scripts allow-popups allow-forms"
            title="Jupyter Notebook"
        />
    </section>
</template>

<style scoped>
.jupyter-section {
    width: 100%;
    max-width: 80%;
    padding: 2rem;
}

iframe {
    border-radius: var(--border-radius);
    width: 100%; 
    height: 70vh; 
}

.blog {
    margin-bottom: 1rem;
}
</style>
