<template>
  <footer class="footer-bar">
    <p class="footer">
      <font-awesome-icon :icon="['fas', 'copyright']" />
      {{ t('about.my_name') }}, 2025
    </p>
    <p class="footer">
      {{ t('footer.powerby') }}
      <a
        :href="vueCred.link"
        target="_blank"
        rel="noopener noreferrer"
        :title="vueCred.tooltip"
      >
        <font-awesome-icon :icon="vueCred.faIcon" />
      </a>.
      {{ t('footer.iconsby') }}
      <a
        :href="faCred.link"
        target="_blank"
        rel="noopener noreferrer"
        :title="faCred.tooltip"
      >
        <font-awesome-icon :icon="faCred.faIcon" />
      </a>.
    </p>
    <font-awesome-icon
      v-if="showChevron"
      :icon="['fas', 'chevron-up']"
      class="chevron up"
      @click="scrollToMain"
    />
  </footer>
</template>

<script setup>
import { computed } from 'vue'
import JSONData from '@/data/data.json'
import { useI18n } from 'vue-i18n'
import { useNavStore } from '@/stores/nav'

const { t } = useI18n()

const nav = useNavStore()

const vueCred = JSONData.footer_creds.find(c => c.brand === 'vue')
const faCred = JSONData.footer_creds.find(c => c.brand === 'fontawesome')

const showChevron = computed(() => {
  return nav.mainSection !== 'Jupyter'
})

function scrollToMain () {
  const next = document.querySelector(nav.mainSection)
  if (next) next.scrollIntoView({ behavior: 'smooth' })
}
</script>

<style scoped>
.footer-bar {
    display: flex;
    flex-direction: column;
    box-shadow: var(--footer-box-shadow);
    justify-content: center;
    align-items: center;
    padding-top: 0.5rem;
}

p.footer {
    margin: 0.3rem;
}

.chevron.up{
    margin-bottom: 0rem;
    padding-bottom: 0rem;
}
</style>
