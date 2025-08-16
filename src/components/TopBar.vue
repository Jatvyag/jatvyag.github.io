<template>
  <div class="top-bar">
    <NavMenu />
    <div class="top-right-bar">
      <router-link
        v-if="route.path !== '/'"
        to="/"
        class="top-link-btn"
      >
        <font-awesome-icon :icon="['fas', 'address-card']" />
      </router-link>
      <router-link
        v-if="route.path !== '/blog'"
        to="/blog"
        class="top-link-btn"
      >
        <font-awesome-icon :icon="['fas', 'blog']" />
      </router-link>
      <LangSwitcher />
      <ThemeSwitcher />
    </div>
  </div>
</template>

<script setup>
import { useRoute } from 'vue-router'
import LangSwitcher from '@/components/LangSwitcher.vue'
import ThemeSwitcher from '@/components/ThemeSwitcher.vue'
import NavMenu from '@/components/NavMenu.vue'

const route = useRoute()
</script>

<style lang="scss" scoped>
.top-bar {
    position: fixed;
    display: flex;
    top: 0;
    left: 0;
    width: 100%;
    background-color: var(--body-bg);
    z-index: 1000;
    justify-content: space-between;
    align-items: center;
    gap: 1rem;
    padding: 0.3rem 0.3rem 0.3rem 0.3rem;
    box-shadow: var(--drop-down-shadow);
}

.top-right-bar {
    display: flex;
    justify-content: flex-end;
    align-items: center;
    gap: 0.5rem;
    padding: 0.3rem 1rem 0.3rem 0.3rem;
}

.top-nav-links {
    display: flex;
    gap: 1rem;
    align-items: center;
}

.top-link-btn {
    display: flex;
    font-size: 1.7rem;
    color: inherit;
    transition: background 0.3s, border-color 0.3s;
}

.top-link-btn:hover {
    color: var(--btn-hover);
    transition: color 0.3s;
}
</style>
