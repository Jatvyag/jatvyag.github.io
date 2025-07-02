<script setup>
import { useI18n } from 'vue-i18n'
import commonData from '../data/common.json'

const { t, tm } = useI18n()

const skills = commonData.skills

const getIconPath = (iconFile) =>
    new URL(`../assets/skills/${iconFile}`, import.meta.url).href

const getSkillPairs = (skillsArray) => {
    const pairs = []
    for (let i = 0; i < skillsArray.length; i += 2) {
        pairs.push(skillsArray.slice(i, i + 2))
    }
    return pairs
}

const getCategoryPairs = (skillsObj) => {
    const entries = Object.entries(skillsObj)
    const pairs = []
    for (let i = 0; i < entries.length; i += 2) {
        const pair = {}
        pair[entries[i][0]] = entries[i][1]
        if (entries[i + 1]) {
        pair[entries[i + 1][0]] = entries[i + 1][1]
        }
        pairs.push(pair)
    }
    return pairs
}

function scrollToNextSection() {
    const next = document.querySelector('#achievements') 
    if (next) next.scrollIntoView({ behavior: 'smooth' })
}
</script>

<template>
    <section id="skills" class="section">
        <h2>{{ t('navMenu.skills') }}</h2>
        <div class="card">
        <div class="category-grid">
            <div
            v-for="pair in getCategoryPairs(skills)"
            :key="Object.keys(pair).join('-')"
            class="category-row"
            >
            <div
                v-for="(items, key) in pair"
                :key="key"
                class="skill-group"
            >
                <h3>{{ t(`skills.h3.${key}`) }}</h3>
                <div class="skill-grid">
                <div
                    v-for="pair in getSkillPairs(items)"
                    :key="pair.map(s => s.id).join('-')"
                    class="skill-row"
                >
                    <div
                    v-for="skill in pair"
                    :key="skill.id"
                    class="skill-item"
                    >
                    <img :src="getIconPath(skill.icon)" :alt="skill.name" class="skill-icon" />
                    <span class="skill-name">{{ skill.name }}</span>
                    </div>
                </div>
                </div>
            </div>
            </div>
        </div>
        </div>
        <font-awesome-icon :icon="['fas', 'chevron-down']" class="chevron" @click="scrollToNextSection" />
    </section>
</template>

<style scoped>
.category-grid {
    display: flex;
    flex-direction: column;
    gap: 0.5rem;
}

.category-row {
    display: flex;
    gap: 1rem;
    flex-wrap: wrap;
}

.skill-group {
    flex: 1;
    display: flex;
    flex-direction: column;
    align-items: center;
    text-align: center;
}

.skill-group h3 {
    margin-bottom: 1rem;
    margin-top: 0.2rem;
    word-break: break-word;
    white-space: normal;
}

.skill-grid {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
    gap: 0.5rem 0.5rem;
}

.skill-item {
    display: flex;
    align-items: left;
    width: calc(50% - 1rem); 
    justify-content: flex-start;
    padding-bottom: 0.5rem;
}

.skill-icon {
    width: 24px;
    height: 24px;
    margin-right: 0.75rem;
}

.skill-name {
    white-space: nowrap;
    font-size: 1rem;
    text-overflow: ellipsis;
}

@media (max-width: 768px) {
    .category-row {
        flex-direction: column;
    }

    .skill-grid {
        flex-direction: column;
        align-items: center;
    }

    .skill-item {
        width: 100%;
        justify-content: center;
    }
}

</style>

