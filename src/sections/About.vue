<script setup>
import Banner from '../components/Banner.vue'
import { useI18n } from 'vue-i18n'
const { t, tm } = useI18n()

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
function scrollToNextSection() {
  const next = document.querySelector('#skills') 
  if (next) next.scrollIntoView({ behavior: 'smooth' })
}
</script>

<template>
  <section id="main" class="section">
    <h1>{{ t('about.my_name') }}</h1>
    <Banner />
    <div>
      <p>{{ t('about.intro') }}</p>
      <p class="tagline">
        <span class="tag">{{ t('about.tagline_prefix', { coding_years }) }}</span>
        <span v-for="(tag, index) in tm('about.tech_tags')" :key="index" class="tag">
          {{ tag }}
        </span>
      </p>
      <p>{{ t('about.career_path') }}</p>
      <p class="tagline">
        <span class="tag">{{ t('about.legal_prefix', { data_years }) }}</span>
        <span v-for="(tag, index) in tm('about.legal_tags')" :key="index" class="tag">
          {{ tag }}
        </span>
      </p>
    </div>
    <font-awesome-icon :icon="['fas', 'chevron-down']" class="chevron" @click="scrollToNextSection" />
  </section>
</template>

<style scoped>
.tagline {
  font-size: 1rem;
  line-height: 1.6;
  display: flex;
  flex-wrap: wrap;
  gap: 0.5rem;
  align-items: center;
  justify-content: center;
}

.tag {
  background-color: var(--btn-bg);
  color: var(--text-color);
  border-radius: 999px;
  padding: 0.3rem 0.6rem 0.5rem 0.6rem;
  font-size: 0.9rem;
  white-space: nowrap;
}
</style>
