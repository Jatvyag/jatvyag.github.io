<script setup>
import { ref, onMounted } from 'vue'

const theme = ref('dark')

onMounted(() => {
    const saved = sessionStorage.getItem('theme')
    theme.value = saved || 'dark'
    document.documentElement.setAttribute('data-theme', theme.value)
})

function toggleTheme() {
    theme.value = theme.value === 'dark' ? 'light' : 'dark'
    sessionStorage.setItem('theme', theme.value)
    document.documentElement.setAttribute('data-theme', theme.value)
}
</script>

<template>
    <div class="theme-toggle" @click="toggleTheme" :class="theme">
        <span class="icon moon">{{ '\u{1F315}' }}</span>
        <span class="icon sun">{{ '\u{26C5}' }}</span>
        <span class="sliding-circle"></span> 
    </div>
</template>

<style scoped>
.theme-toggle {
    position: relative;
    width: 3.5rem; 
    height: 1.75rem;
    background: var(--btn-bg);
    color: var(--text-color);
    border-radius: 999px;
    border: 2px solid transparent;
    cursor: pointer;
    display: flex;
    align-items: center;
    justify-content: space-between;
    font-size: 1rem;
    transition: background 0.3s ease;
}

.theme-toggle:hover {
    border-color: var(--btn-hover-color);
    transition: border-color 0.25s;
}

.theme-toggle .icon {
    flex: 1;
    display: flex;
    align-items: center;
    justify-content: center;
    padding-bottom: 2px;
    height: 100%;
    font-size: 1rem;
    line-height: 1;
    z-index: 1;
    transition: opacity 0.3s ease;
}

.moon,
.sun {
    margin: 0; 
}

.sliding-circle {
    position: absolute;
    left: 2px;
    width: calc(100% / 2 - 4px);
    height: calc(100% - 4px);
    background: white;
    border-radius: 50%;
    transition: transform 0.3s ease;
}

.theme-toggle.light .sliding-circle {
    transform: translateX(115%);
}

.theme-toggle.dark .sun {
    opacity: 0;
}

.theme-toggle.light .moon {
    opacity: 0;
}
</style>
