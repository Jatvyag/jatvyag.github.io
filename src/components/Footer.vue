<script setup>
import { useI18n } from 'vue-i18n'
const { t, tm } = useI18n()
</script>

<template>
    <footer class="footer-bar">
        <p>
            <font-awesome-icon :icon="['fas', 'copyright']" />
            {{ t('about.my_name') }}, 2025
        </p>
    </footer>
</template>

<style scoped>
.footer-bar {
    width: 100vw; 
    background-color: var(--bg);
    box-shadow: var(--footer-box-shadow);
    padding: 0.3rem;
    display: flex;
    justify-content: center;
    align-items: center;
    /* These break it out of centered layout if inside a constrained container */
    position: relative;
    left: 50%;
    right: 50%;
    margin-left: -50vw;
    margin-right: -50vw;
}
</style>
