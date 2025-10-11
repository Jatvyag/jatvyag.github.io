<template>
  <div class="social-media">
    <a
      v-for="item in socialMediaArray"
      :key="item.id"
      :href="item.link"
      :title="item.tooltip"
      target="_blank"
      rel="noopener noreferrer"
      class="social-icon"
    >
      <font-awesome-icon :icon="item.faIcon" />
    </a>
  </div>
</template>

<script setup>
const { socialMediaArray } = defineProps({
  socialMediaArray: {
    type: Array,
    required: true
  }
})
</script>

<style lang="scss" scoped>
.social-media {
  display: flex;
  flex-wrap: wrap;
  gap: 1rem;
  justify-content: center;
  align-items: center;
  margin-top: 0rem;
}

.social-icon {
  font-size: 1.5rem;
  transition: color 0.3s ease;
}
</style>
