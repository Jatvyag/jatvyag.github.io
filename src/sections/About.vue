<template>
  <section
    :ref="sectionLink"
    class="section"
  >
    <h1>{{ t('about.my_name') }}</h1>
    <Banner />
    <div>
      <TagLine
        :exp-desc="t('about.intro')"
        :exp-years="t('about.tagline_prefix', { coding_years: codingYears })"
        :exp-tags="tm('about.tech_tags')"
      />
      <TagLine
        :exp-desc="t('about.career_path')"
        :exp-years="t('about.legal_prefix', { data_years: dataYears })"
        :exp-tags="tm('about.legal_tags')"
      />
    </div>
    <ChevronSection
      :section-ref="nextSection"
    />
  </section>
</template>

<script setup>
import { Banner, TagLine } from '@/sections/components'
import ChevronSection from '@/components'
import { useI18n } from 'vue-i18n'

const { t, tm } = useI18n()

const { sectionLink, nextSection } = defineProps({
  sectionLink: {
    type: Object,
    required: true
  },
  nextSection: {
    type: Object,
    required: true
  }
})

const CODING_START = '2023-09-04'
const DATA_START = '2014-09-04'

/**
 * Full years expirience calculation
 * @param {string} startDateStr - Start date for full years expirience calculation
 * @return {number}
 */
function getDataExpYears (startDateStr) {
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

const codingYears = getDataExpYears(CODING_START)
const dataYears = getDataExpYears(DATA_START)
</script>
<style lang="scss">
</style>
