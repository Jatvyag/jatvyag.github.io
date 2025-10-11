<template>
  <a
    :href="`mailto:${emailAddress}`"
    title="Email"
  >
    <font-awesome-icon :icon="['fas', 'at']" />
  </a>
</template>

<script setup>
const { emailAddress } = defineProps({
  emailAddress: {
    type: String,
    required: true
  }
})
</script>
