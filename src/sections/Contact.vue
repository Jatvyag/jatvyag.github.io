<script setup>
import { useI18n } from 'vue-i18n'

const { t } = useI18n()

</script>

<template>
    <section id="contacts" class="section last">
        <h2>{{ t('navMenu.contacts') }}</h2>
        <p>Some text...</p>
    </section>
</template>

<style scoped>
.section.last{
    min-height: 80vh;
}
</style>

