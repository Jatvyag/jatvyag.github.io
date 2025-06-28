<script setup>
import Banner from './Banner.vue'
import { useI18n } from 'vue-i18n'
const { t } = useI18n()

defineProps({
  msg: String,
})

</script>

<template>
  <h1>{{ msg }}</h1>
  <Banner />
  <div class="card">
    {{ t('about.intro') }}
  </div>
</template>

<style scoped>
</style>
