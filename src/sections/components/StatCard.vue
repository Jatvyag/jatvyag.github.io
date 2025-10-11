<template>
  <div class="completed-stats">
    <div
      v-for="item in statCardArray"
      :key="item.id"
      class="stat-card"
    >
      <div class="stat-type">
        {{ item.type }}
      </div>
      <div class="stat-number">
        {{ item.number }}
      </div>
    </div>
  </div>
</template>

<script setup>
const { statCardArray } = defineProps({
  statCardArray: {
    type: Array[String],
    required: true
  }
})
</script>

<style lang="scss" scoped>
.completed-stats {
    display: flex;
    gap: 1rem;
    margin-top: 1.5rem;
    flex-wrap: wrap;

  .stat-card {
      background-color: var(--card-bg);
      border-radius: 10px;
      padding: 0.7rem 0.9rem;
      box-shadow: var(--card-shadow);
      text-align: center;
      min-width: 6rem;

    .stat-type {
        font-size: 0.875rem;
        color: var(--text-light);
    }

    .stat-number {
        font-size: 1.5rem;
        font-weight: bold;
    }
  }
}
</style>
