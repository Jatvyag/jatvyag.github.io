<template>
  <p class="tagline">
    {{ expDesc }}
  </p>
  <p class="tagline">
    <span class="tag">{{ expYears }}</span>
    <span
      v-for="(tag, index) in expTags"
      :key="index"
      class="tag"
    >
      {{ tag }}
    </span>
  </p>
</template>

<script setup>
const { expDesc, expYears, expTags } = defineProps({
  expDesc: {
    type: String,
    required: true
  },
  expYears: {
    type: String,
    required: true
  },
  expTags: {
    type: Array,
    required: true
  }
})
</script>
<style lang="scss">
.tagline {
  display: flex;
  font-size: 1rem;
  flex-wrap: wrap;
  gap: 0.5rem;
  text-align: center;
  justify-content: center;
}

@media (max-width: 600px) {
  .tagline {
    text-align: start;
    justify-content: start;
  }
}
</style>
