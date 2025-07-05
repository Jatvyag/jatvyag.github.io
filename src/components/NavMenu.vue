<script setup>
import { ref } from 'vue'
import { useI18n } from 'vue-i18n'

const props = defineProps({
    currentSection: {
        type: String,
        required: true,
    },
    navItems: {
        type: Array,
        required: true,
    },
    navMenuLangPage: {
        type: String,
        required: true,
    }
})

const emit = defineEmits(['update:currentSection'])

const { t } = useI18n()
const isOpen = ref(false)

function toggleMenu() {
    isOpen.value = !isOpen.value
}

function handleNavigation(item) {
    if (item.disabled) return
    const hash = item.link
    if (hash && hash.startsWith('#')) {
        const el = document.querySelector(hash)
        if (el) {
        el.scrollIntoView({ behavior: 'smooth' })
        emit('update:currentSection', item.key)
        isOpen.value = false
        }
    }
}
</script>

<template>
    <div class="nav-wrapper">
        <button 
            class="menu-btn" 
            @click="toggleMenu"
            :disabled="navItems.length <= 1"
        >
            <font-awesome-icon 
                :icon="navItems.find(item => item.key === currentSection)?.faIcon || ['fas', 'bars']" 
            />
            <span class="page-title">{{ currentSection ? 
                t(`${navMenuLangPage}.${currentSection}`) :
                ''
            }}</span>
        </button>
        <!-- Backdrop -->
        <div v-if="isOpen" class="backdrop" @click="toggleMenu"></div>
        <!-- Side Menu -->
        <div class="side-menu" :class="{ open: isOpen }">
        <ul>
            <li
            v-for="item in navItems"
            :key="item.key"
            :class="{ active: item.key === currentSection, disabled: item.disabled }"
            @click="handleNavigation(item)"
            >
                <font-awesome-icon v-if="item.faIcon" :icon="item.faIcon" />
                <span v-else>{{ item.unicodeIcon }}</span>
                <span>{{ t(`${navMenuLangPage}.${item.key}`) }}</span>
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
    flex-shrink: 1;
    flex-grow: 0;
    min-width: 0;
}

.menu-btn {
    display: flex;
    align-items: center;
    font-size: 1.5rem;
    gap: 0.5rem;
    min-width: 0;
    border: 2px solid transparent; 
    background: none;
    cursor: pointer;
}

.menu-btn:hover {
    border-color: var(--btn-hover-color);
    background-color: var(--btn-bg);
    border-radius: var(--border-radius);
}

.menu-btn:disabled {
    opacity: 0.5;
    border: 2px solid transparent;
    background: none;
    cursor: not-allowed;
    transform: scale(1);
}

.page-title {
    display: block;
    max-width: 100%;  
    font-weight: bold;
    white-space: nowrap;
    overflow: hidden; 
    text-overflow: ellipsis; 
}

.backdrop {
    position: fixed;
    top: 0;
    left: 0;
    width: 100vw;
    height: 100vh;
    background-color: rgba(0, 0, 0, 0.4); 
    z-index: 999; /* below side-menu (1000) */
}

.side-menu {
    position: fixed;
    top: 0;
    left: 0;
    height: 100vh;
    width: 240px;
    background-color: var(--bg);
    color: var(--text-color);
    padding-top: 2rem;
    padding-left: 1rem;
    transition: transform 0.3s ease;
    z-index: 1000;
    box-shadow: var(--drop-down-box-shadow);
    transform: translateX(-100%);
}

.side-menu.open {
    left: 0;
    top: 0;
    padding-top: 2rem;
    transform: translateX(0);
}

.side-menu ul {
    list-style: none;
    padding: 0;
    margin: 0;
}

.side-menu li {
    padding: 0.5rem;
    margin-right: 1rem;
    display: flex;
    cursor: pointer;
    gap: 0.5rem;
    align-items: center;
    border: 2px solid transparent; 
}

.side-menu li.active,
.side-menu li:hover {
    border-color: var(--btn-hover-color);
    background-color: var(--btn-bg);
    border-radius: var(--border-radius);
}

.side-menu li.disabled {
    opacity: 0.5;
    pointer-events: none;
}

@media (max-width: 600px) {
    .side-menu {
        width: 50vw;
    }
}

@media (min-width: 601px) and (max-width: 1024px) {
    .side-menu {
        width: 50vw;
    }
}
</style>
