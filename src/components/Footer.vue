<script setup>
import { useI18n } from 'vue-i18n'
const { t } = useI18n()

function scrollToMain() {
    const next = document.querySelector('#main') 
    if (next) next.scrollIntoView({ behavior: 'smooth' })
}
</script>

<template>
    <footer class="footer-bar">
        <p>
            <font-awesome-icon :icon="['fas', 'copyright']" />
            {{ t('about.my_name') }}, 2025
        </p>
        <font-awesome-icon :icon="['fas', 'chevron-up']" class="chevron up" @click="scrollToMain" />
    </footer>
</template>

<style scoped>
.footer-bar {
    display: flex;
    flex-direction: column;
    box-shadow: var(--footer-box-shadow);
    justify-content: center;
    align-items: center;
}

.chevron.up{
    margin-bottom: 0rem;
}
</style>
