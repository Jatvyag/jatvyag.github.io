<template>
  <h2 class="typewriter-line">
    <span
      ref="typeWriterRef"
      class="typewriter-dynamic"
    />
    <span class="typewriter-fixed">{{ tm('banner') }}</span>
  </h2>
</template>

<script setup>
import { useI18n } from 'vue-i18n'
import { onMounted, ref } from 'vue'
import TypeWriter from 'typewriter-effect/dist/core'

const { tm } = useI18n()

// Declared a ref to the typeWriter span
const typeWriterRef = ref(null)

/**
 * Start typewriter effect
 */
function startTypeWriter () {
  const span = typeWriterRef.value
  if (!span) return

  // Clear previous content
  span.innerHTML = ''
  /* eslint-disable no-new */
  new TypeWriter(span, {
    strings: ['Python', 'JavaScript', 'Full-Stack'],
    autoStart: true,
    loop: true,
    deleteSpeed: 5
  })
  /* eslint-enable no-new */
}

onMounted(() => {
  startTypeWriter()
})
</script>

<style lang="scss" scoped>
.typewriter-line {
    display: flex;
    flex-wrap: wrap;
    align-items: baseline;
    justify-content: center;
    white-space: nowrap;

  .typewriter-dynamic {
      min-width: 11ch; /* the max length of typewritten words */
      display: inline-block;
      text-align: right;
  }

  .typewriter-fixed {
      flex-shrink: 0;
  }
}
</style>
