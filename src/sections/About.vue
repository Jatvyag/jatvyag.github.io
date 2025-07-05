<script setup>
import Banner from '../components/Banner.vue'
import { useI18n } from 'vue-i18n'
const { t, tm } = useI18n()

const props = defineProps({
    sectionLink: {
        type: String,
        required: true,
    },
    nextSection: {
      type: String,
      required: true
    }
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
function scrollToNextSection() {
  const next = document.querySelector(props.nextSection) 
  if (next) next.scrollIntoView({ behavior: 'smooth' })
}
</script>

<template>
  <section :id="props.sectionLink.replace('#', '')" class="section">
    <h1>{{ t('about.my_name') }}</h1>
    <Banner />
    <div>
      <p class="tagline">{{ t('about.intro') }}</p>
      <p class="tagline">
        <span class="tag">{{ t('about.tagline_prefix', { coding_years }) }}</span>
        <span v-for="(tag, index) in tm('about.tech_tags')" :key="index" class="tag">
          {{ tag }}
        </span>
      </p>
      <p class="tagline">{{ t('about.career_path') }}</p>
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
  display: flex;
  font-size: 1rem;
  flex-wrap: wrap;
  gap: 0.5rem;
  text-align: center;
  justify-content: center;
}

@media (max-width: 600px) {
  .tagline {
    text-align: start;
    justify-content: start;
  }
}
</style>
