<template>
  <section
    :ref="props.sectionLink"
    class="section"
  >
    <h2>{{ t('navMenu.main.achievements') }}</h2>
    <h3 class="achievements">
      DataCamp
    </h3>
    <ParagraphArray
      :paragraph-array="tm('achievements.datacamp.intro')"
    />
    <div class="certificates">
      <div
        v-for="certificate in tm('achievements.certificates')"
        :key="certificate.id"
        class="certificate"
      >
        <img
          :src="getAssetHref('achievements', certificate.badge)"
          :alt="certificate.name"
          class="badge"
        >
        <div class="info">
          <div class="name">
            {{ certificate.name }}
          </div>
          <div class="issuer">
            {{ certificate.issuer }}, {{ certificate.issued }}
          </div>
        </div>
      </div>
    </div>
    <StatCard
      :stat-card-array="tm('achievements.datacamp.completed')"
    />
    <ChevronSection
      :section-ref="props.nextSection"
    />
  </section>
</template>

<script setup>
import ParagraphArray from '@/sections/components/ParagraphArray.vue'
import StatCard from '@/sections/components/StatCard.vue'
import ChevronSection from '@/components/ChevronSection.vue'
import { getAssetHref } from '@/utils'
import { useI18n } from 'vue-i18n'

const { t, tm } = useI18n()

const props = defineProps({
  sectionLink: {
    type: Object,
    required: true
  },
  nextSection: {
    type: Object,
    required: true
  }
})
</script>

<style lang="scss" scoped>
.achievements {
  &.h3 {
    margin-top: 0;
  }

  &.p {
    text-align: left;
    width: 100%;
  }
}

.certificates {
    display: flex;
    justify-content: center;
    flex-wrap: wrap;
    gap: 1rem;
    margin-top: 1rem;
}

.certificate {
  display: flex;
  align-items: center;
  background-color: var(--card-bg);
  box-shadow: var(--card-shadow);
  border-radius: 10px;
  padding: 0.75rem;

  .badge {
    width: 96px;
    height: 96px;
    object-fit: contain;
    flex-shrink: 0;
  }

  .info {
    display: flex;
    flex-direction: column;
    padding-left: 0.5rem;

    .name {
      text-align: left;
      font-weight: bold;
      font-size: 1.1rem;
    }

    .issuer {
      text-align: left;
      color: #8f8f8f;
      font-size: 0.9rem;
    }
  }
}
</style>
