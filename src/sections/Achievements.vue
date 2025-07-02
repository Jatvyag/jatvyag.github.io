<script setup>
import { useI18n } from 'vue-i18n'

const { t, tm } = useI18n()

const getBadgePath = (badgeFile) =>
    new URL(`../assets/achievements/${badgeFile}`, import.meta.url).href

function scrollToNextSection() {
    const next = document.querySelector('#contact') 
    if (next) next.scrollIntoView({ behavior: 'smooth' })
}
</script>

<template>
    <section id="achievements" class="section">
        <h2>{{ t('navMenu.achievements') }}</h2>
        <h3 class="in-section">DataCamp</h3>
        <p
            v-for="(paragraph, index) in tm('achievements.datacamp.intro')"
            :key="index"
        >
            {{ paragraph }}
        </p>
        <div class="certificates">
            <div
                class="certificate"
                v-for="certificate in tm('achievements.certificates')"
                :key="certificate.id"
            >
                <img
                    :src="getBadgePath(certificate.badge)"
                    :alt="certificate.name"
                    class="badge"
                />
                <div class="info">
                    <div class="name">{{ certificate.name }}</div>
                    <div class="issuer">{{ certificate.issuer }}</div>
                </div>
            </div>
            <div class="completed-stats">
                    <div
                        class="stat-card"
                        v-for="item in tm('achievements.datacamp.completed')"
                        :key="item.id"
                    >
                        <div class="stat-type">{{ item.type }}</div>
                        <div class="stat-number">{{ item.number }}</div>
                    </div>
                </div>
            </div>
        <font-awesome-icon :icon="['fas', 'chevron-down']" class="chevron" @click="scrollToNextSection" />
    </section>
</template>

<style scoped>
h3.in-section {
    margin-top: 0rem;
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
    width: 100%;
    max-width: 15rem;
    background-color: #666;
    border-radius: 10px;
    padding: 0.75rem;
}

.badge {
    width: 96px;
    height: 96px;
    object-fit: contain;
}

.info {
    display: flex;
    flex-direction: column;
    padding-left: 0.5rem;
}

.name {
    text-align: left;
    font-weight: bold;
    font-size: 1.1rem;
    }

.issuer {
    text-align: left;
    color: lightgray;
    font-size: 0.9rem;
}
.completed-stats {
    display: flex;
    gap: 1rem;
    margin-top: 1rem;
    flex-wrap: wrap;
    justify-content: center;
}

.stat-card {
    background-color: var(--card-bg);
    border-radius: 8px;
    padding: 0.75rem 1rem;
    box-shadow: var(--card-box-shadow);
    text-align: center;
    min-width: 6rem;
}

.stat-number {
    font-size: 1.5rem;
    font-weight: bold;
}

.stat-type {
    font-size: 0.875rem;
    color: var(--text-light);
}

</style>

