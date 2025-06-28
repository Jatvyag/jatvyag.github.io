<script setup>
import { ref } from 'vue'

defineProps({
  msg: String,
})

</script>

<template>
  <h1>{{ msg }}</h1>
  <div class="card">
    Here you can find info about myself
  </div>
</template>

<style scoped>
.read-the-docs {
  color: #888;
}
</style>
