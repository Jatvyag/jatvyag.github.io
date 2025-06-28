<script setup>
import { ref } from 'vue'
import { useI18n } from 'vue-i18n'
const { t } = useI18n()

defineProps({
  msg: String,
})

</script>

<template>
  <h1>{{ msg }}</h1>
  <div class="card">
    {{ t('about.intro') }}
  </div>
</template>

<style scoped>
.read-the-docs {
  color: #888;
}
</style>
