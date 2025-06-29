<script setup>
import Banner from './Banner.vue'
import { useI18n } from 'vue-i18n'
const { t } = useI18n()

defineProps({
  msg: String,
})

function calculateYears(startDateStr) {
  const startDate = new Date(startDateStr)
  const today = new Date()
  let years = today.getFullYear() - startDate.getFullYear()
  const monthDiff = today.getMonth() - startDate.getMonth()
  const dayDiff = today.getDate() - startDate.getDate()
  if (monthDiff < 0 || (monthDiff === 0 && dayDiff < 0)) {
    years--
  }
  return years
}

const coding_years = calculateYears('2023-09-04')
const data_years = calculateYears('2014-09-04')
</script>

<template>
  <h1>{{ msg }}</h1>
  <Banner />
  <div class="card">
    <p>{{ t('about.intro') }}</p>
    <p>{{ t('about.tagline', { coding_years }) }}</p>
    <p>{{ t('about.careerPath') }}</p>
    <p>{{ t('about.legalTags', { data_years }) }}</p>
  </div>
</template>

<style scoped>
.card {
  padding: 2em;
  background-color: var(--button-bg); 
  color: var(--text);
  border-radius: 12px;
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.15);
  transition: box-shadow 0.3s ease;
}

.card:hover {
  box-shadow: 0 6px 24px rgba(0, 0, 0, 0.2);
}
</style>
