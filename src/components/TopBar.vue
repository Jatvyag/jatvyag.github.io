<script setup>
import LangSwitcher from './LangSwitcher.vue'
import ThemeSwitcher from './ThemeSwitcher.vue'
import NavMenu from './NavMenu.vue'

defineProps({
    navItems: Array,
    currentSection: String,
    navMenuLangPage: String
})

defineEmits(['update:currentSection'])
</script>

<template>
    <div class="top-bar">
        <NavMenu
            :navItems="navItems"
            :currentSection="currentSection"
            :navMenuLangPage="navMenuLangPage"
            @update:currentSection="$emit('update:currentSection', $event)"
        />
        <div class="top-lang-theme-bar">
            <LangSwitcher />
            <ThemeSwitcher />
        </div>
    </div>
</template>

<style scoped>
.top-bar {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    background-color: var(--bg); 
    z-index: 1000;
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 0.3rem 0.3rem 0.3rem 0.3rem;
    box-shadow: var(--drop-down-box-shadow);
}

.top-lang-theme-bar {
    display: flex;
    justify-content: flex-end;
    align-items: center;
    gap: 0.5rem; 
    padding: 0.3rem 1rem 0.3rem 0.3rem;
}
</style>
