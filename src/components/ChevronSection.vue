<template>
  <font-awesome-icon
    :icon="['fas', chevronIcon]"
    class="chevron"
    :class="{ up: isUp }"
    @click="scrollToNextSection"
  />
</template>

<script setup>
import { computed } from 'vue'

const { sectionRef, isUp } = defineProps({
  sectionRef: {
    type: Object,
    required: true
  },
  isUp: {
    type: Boolean,
    default: false
  }
})

const chevronIcon = computed(() => {
  return isUp ? 'chevron-up' : 'chevron-down'
})

function scrollToNextSection () {
  if (sectionRef.value) {
    sectionRef.value.scrollIntoView({ behavior: 'smooth' })
  }
}
</script>

<style lang="scss" scoped>
@use 'sass:map';
@use '@/styles/abstracts/variables' as *;

.chevron {
  margin-top: auto;
  margin-bottom: 3rem;
  text-align: center;
  font-size: 3rem;
  color: var(--btn-hover);
  cursor: pointer;
  padding-bottom: 1rem;

  &:hover {
    color: $attention-color;
  }

  &:active {
    transform: scale(0.9);
  }

  &.up {
    padding-bottom: 0;
    margin-top: 0.5rem;
    margin-bottom: 0;
  }
}
</style>
