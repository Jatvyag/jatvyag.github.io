<template>
  <p
    v-for="(paragraph, index) in props.paragraphArray"
    :key="index"
    class="paragraph-array"
  >
    {{ paragraph }}
  </p>
</template>

<script setup>
const props = defineProps({
  paragraphArray: {
    type: Array[String],
    required: true
  }
})
</script>

<style lang="scss" scoped>
.paragraph-array {
  text-align: left;
  width: 100%;
}
</style>
