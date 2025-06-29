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
    width: 60px;
    height: 30px;
    background: var(--btn-bg);
    color: var(--text-color);
    border-radius: 999px;
    border: 2px solid transparent;
    cursor: pointer;
    display: flex;
    align-items: center;
    justify-content: space-between;
    font-size: 1.2rem;
    transition: background 0.3s ease;
}

.theme-toggle:hover {
    border-color: var(--btn-hover-color);
    transition: border-color 0.25s;
}

.icon {
    z-index: 1;
    transition: opacity 0.3s ease;
}

.moon {
    margin: 0px 0px 2px 3px;
}

.sun {
    margin: 0px 3px 2px 0px;
}

.sliding-circle {
    position: absolute;
    inset: 2px;
    width: 26px;
    height: 26px;
    background: white;
    border-radius: 50%;
    transition: transform 0.3s ease;
}

.theme-toggle.light .sliding-circle {
    transform: translateX(30px);
}

.theme-toggle.dark .sun {
    opacity: 0;
}

.theme-toggle.light .moon {
    opacity: 0;
}
</style>
