<script setup>
import { ref } from 'vue'
import { useI18n } from 'vue-i18n'

const { t } = useI18n()
const isOpen = ref(false)
const currentPage = ref('main') 

const navItems = [
    { key: 'main', icon: '\u{2630}', disabled: false },
    { key: 'projects', icon: '\u{2699}', disabled: true },
    { key: 'skills', icon: '\u{1F6E0}', disabled: true },
    { key: 'certifications', icon: '\u{2714}', disabled: true },
    { key: 'articles', icon: '\u{270E}', disabled: true },
    { key: 'contact', icon: '\u{2709}', disabled: true },
]

function toggleMenu() {
    isOpen.value = !isOpen.value
}
</script>

<template>
    <div class="nav-wrapper">
        <button class="menu-btn" @click="toggleMenu"><span>{{ '\u{2630}' }}</span></button>
        <span class="page-title">{{ t(`navMenu.${currentPage}`) }}</span>
        <div class="side-menu" :class="{ open: isOpen }">
        <button class="close-btn" @click="toggleMenu" :class="{ rotated: isOpen }"><span>{{ '\u{2716}' }}</span></button>
        <ul>
            <li
            v-for="item in navItems"
            :key="item.key"
            :class="{ active: item.key === currentPage, disabled: item.disabled }"
            >
            <span>{{ item.icon }}</span>
            <span>{{ t(`navMenu.${item.key}`) }}</span>
            </li>
        </ul>
        </div>
    </div>
</template>

<style scoped>
.nav-wrapper {
    display: flex;
    align-items: center;
    gap: 0.5rem;
    position: relative;
}

.menu-btn {
    font-size: 1.5rem;
    background: none;
    border: none;
    cursor: pointer;
}

.close-btn {
    background: none;
    border: none;
    font-size: 2rem;
    color: var(--attention-color);
    cursor: pointer;
    margin: 0 auto;
    display: block;
    transition: transform 0.4s ease, color 0.3s ease;
}

.close-btn.rotated {
    transform: rotate(180deg);
}

.page-title {
    font-weight: bold;
}

.side-menu {
    position: fixed;
    top: 0;
    left: -20vw;
    height: 100vh;
    width: 15vw;
    min-width: 140px;
    max-width: 260px;    
    background-color: var(--bg);
    color: var(--text);
    padding-top: 2rem;
    padding-left: 1rem;
    transition: left 0.3s ease;
    z-index: 1000;
    box-shadow: var(--drop-down-box-shadow);
}

.side-menu.open {
    left: 0;
    top: 0;
    padding-top: 2rem;
}

.side-menu ul {
    list-style: none;
    padding: 0;
    margin: 0;
}

.side-menu li {
    padding: 0.5rem 0;
    display: flex;
    gap: 0.5rem;
    align-items: center;
    cursor: default;
}

.side-menu li.active {
    font-weight: bold;
}

.side-menu li.disabled {
    opacity: 0.5;
    pointer-events: none;
}
</style>
