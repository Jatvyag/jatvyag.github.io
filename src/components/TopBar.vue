<template>
  <div class="top-bar">
    <NavMenu />
    <div class="top-bar--right">
      <router-link
        v-for="link in visibleLinks"
        :key="link.path"
        :to="link.path"
        class="top-bar--right-link-btn"
      >
        <font-awesome-icon :icon="link.icon" />
      </router-link>
      <LangSwitcher />
      <ThemeSwitcher />
    </div>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue'
import { useRoute } from 'vue-router'
import LangSwitcher from '@/components/LangSwitcher.vue'
import ThemeSwitcher from '@/components/ThemeSwitcher.vue'
import NavMenu from '@/components/NavMenu.vue'

const route = useRoute()

const routeLink = ref([
  {
    path: '/',
    icon: ['fas', 'address-card']
  },
  {
    path: '/blog',
    icon: ['fas', 'blog']
  }
])

const visibleLinks = computed(() =>
  routeLink.value.filter(link => link.path !== route.path)
)
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
  padding: 0.3rem;
  box-shadow: var(--drop-down-shadow);

  &--right {
    display: flex;
    justify-content: flex-end;
    align-items: center;
    gap: 0.5rem;
    padding: 0.3rem 1rem 0.3rem 0.3rem;

    &-link-btn {
      display: flex;
      font-size: 1.7rem;
      color: inherit;
      transition: background 0.3s, border-color 0.3s;

      &:hover {
        color: var(--btn-hover);
        transition: color 0.3s;
      }
    }
  }
}
</style>
