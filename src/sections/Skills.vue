<template>
  <section
    :id="props.sectionLink.replace('#', '')"
    class="section"
  >
    <h2>{{ t(`${navMenuLangPage}.skills`) }}</h2>
    <div class="card skills">
      <div
        v-for="(items, categoryKey) in skillsData"
        :key="categoryKey"
        class="skill-group"
      >
        <h3>{{ t(`skills.${categoryKey}`) }}</h3>
        <div class="skill-grid">
          <div
            v-for="skill in items"
            :key="skill.id"
            class="skill-item"
          >
            <img
              :src="getIconPath(skill.icon)"
              :alt="skill.name"
              class="skill-icon"
            >
            <span class="skill-name">{{ skill.name }}</span>
          </div>
        </div>
      </div>
    </div>
    <font-awesome-icon
      :icon="['fas', 'chevron-down']"
      class="chevron"
      @click="scrollToNextSection"
    />
  </section>
</template>

<script setup>
import { useI18n } from 'vue-i18n'
import JSONData from '@/data/data.json'

const { t } = useI18n()
const skillsData = JSONData.skills

const props = defineProps({
  sectionLink: {
    type: String,
    required: true
  },
  navMenuLangPage: {
    type: String,
    required: true
  },
  nextSection: {
    type: String,
    required: true
  }
})

const getIconPath = (iconFile) =>
  new URL(`../assets/icons/${iconFile}`, import.meta.url).href

function scrollToNextSection () {
  const next = document.querySelector(props.nextSection)
  if (next) next.scrollIntoView({ behavior: 'smooth' })
}
</script>

<style scoped>
.card.skills {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 0.5rem 2rem;
    padding: 1rem 2rem 2rem 2rem;
}

.skill-group {
    display: flex;
    flex-direction: column;
    align-items: center;
}

.skill-group h3 {
    margin: 0.5rem 0;
    text-align: center;
    word-break: break-word;
}

.skill-grid {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 0.5rem 1rem;
}

.skill-item {
    display: flex;
    align-items: center;
}

.skill-icon {
    width: 36px;
    height: 36px;
    margin-right: 0.75rem;
}

.skill-name {
    white-space: nowrap;
    font-size: 1rem;
    text-overflow: ellipsis;
}

@media (max-width: 600px) {
    .skill-group {
        align-items: start;
    }

    .skill-group h3 {
        text-align: start;
    }

    .card.skills {
        grid-template-columns: 1fr;
    }
}
</style>
