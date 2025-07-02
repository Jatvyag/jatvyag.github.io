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

function scrollToPrevSection() {
    const previous = document.querySelector('#main') 
    if (previous) previous.scrollIntoView({ behavior: 'smooth' })
}
</script>

<template>
    <section id="skills" class="section">
        <font-awesome-icon :icon="['fas', 'chevron-up']" class="scroll-up" @click="scrollToPrevSection" />
        <h2>{{ t('skills.header') }}</h2>
        <div class="skill-card">
        <div class="category-grid">
            <div
            v-for="(pair, i) in getCategoryPairs(skills)"
            :key="i"
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
                    v-for="(pair, i) in getSkillPairs(items)"
                    :key="i"
                    class="skill-row"
                >
                    <div
                    v-for="skill in pair"
                    :key="skill.name"
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
        <font-awesome-icon :icon="['fas', 'chevron-down']" class="scroll-down" />
    </section>
</template>

<style scoped>
.skill-card {
    padding: 2rem;
    background-color: var(--card-bg); 
    color: var(--text);
    border-radius: 12px;
    box-shadow: var(--card-box-shadow);
    transition: box-shadow 0.3s ease;
}

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
}

.skill-icon {
    width: 24px;
    height: 24px;
    margin-right: 0.75rem;
    filter: var(--icon-filter);
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

