<template>
  <h2 class="typewriter-line">
    <span
      id="typewriter"
      class="typewriter-dynamic"
    />
    <span class="typewriter-fixed">{{ tm('banner') }}</span>
  </h2>
</template>

<script setup>
import { useI18n } from 'vue-i18n'
import { onMounted } from 'vue'
import Typewriter from 'typewriter-effect/dist/core'

const { tm } = useI18n()

// CamelCase startTypeWrite
function startTypewriter () {
  // во Vue для получения элемента используй ref сслылки на элемент
  const el = document.getElementById('typewriter')
  if (!el) return

  // Clear previous content
  // используй v-html для вставки содержимого в элемент и его удаления
  el.innerHTML = ''
  /* eslint-disable no-new */
  new Typewriter(el, {
    strings: ['Python', 'JavaScript', 'Full-Stack'],
    autoStart: true,
    loop: true,
    deleteSpeed: 5
  })
  /* eslint-enable no-new */
}

onMounted(() => {
  startTypewriter()
})
</script>

<style scoped>
.typewriter-line {
    display: flex;
    flex-wrap: wrap;
    align-items: baseline;
    justify-content: center;
    white-space: nowrap;
}

.typewriter-dynamic {
    min-width: 11ch; /* the max length of typewritten words */
    display: inline-block;
    text-align: right;
}

.typewriter-fixed {
    flex-shrink: 0;
}
</style>
