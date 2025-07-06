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

function extractHeadingsFromIframe(iframeEl) {
    try {
        const doc = iframeEl.contentDocument || iframeEl.contentWindow?.document
        if (!doc) return
        const headings = doc.querySelectorAll('h2')
        const result = []
        headings.forEach(h2 => {
            const id = h2.id
            const text = h2.textContent?.replace('¶', '').trim() || 'untitled'
            const item = {
                key: text,
                link: `#${id}`,
                faIcon: ['fas', 'circle'],
                disabled: false,
                type: "jupyter"
            }
            result.push(item)
        })
        console.log('Jupyter navigation items:', result)
    } catch (err) {
        console.error('Failed to access iframe contents:', err)
    }
}

function onThemeChange(e) {
    theme.value = e.detail.theme
}

watch(theme, (newTheme) => {
    iframeSrc.value = `/notebooks/${newTheme}/analyse_tv.html`
})

let hasExtracted = false

onMounted(() => {
    window.addEventListener('theme-changed', onThemeChange)

    const iframe = document.querySelector('iframe')
    iframe.addEventListener('load', () => {
        if (!hasExtracted) {
            extractHeadingsFromIframe(iframe)
            hasExtracted = true
        }
    })
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
