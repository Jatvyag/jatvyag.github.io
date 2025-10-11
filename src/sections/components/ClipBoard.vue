<template>
  <div class="code-wrapper">
    <code
      ref="clipBoardRef"
      class="code-area"
    >
      {{ clipBoardValue }}
    </code>
    <button
      class="clipboard"
      :title="t('contacts.tooltip_copy')"
      @click="copyClipBoardValue"
    >
      <font-awesome-icon :icon="['fas', 'clipboard']" />
    </button>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useI18n } from 'vue-i18n'
const { t } = useI18n()

const { clipBoardValue } = defineProps({
  clipBoardValue: {
    type: [String, Object],
    required: true
  }
})

// Refs
const clipBoardRef = ref(null)

/**
 * Copy the clipboard value to the clipboard
 */
function copyClipBoardValue () {
  const clipBoardValue = clipBoardRef.value?.textContent
  if (clipBoardValue) {
    const valueToCopy = typeof clipBoardValue === 'string'
      ? clipBoardValue
      : clipBoardValue.textContent || ''
    navigator.clipboard.writeText(valueToCopy)
  }
}
</script>

<style lang="scss" scoped>
.code-wrapper {
  display: inline-flex;
  align-items: center;

  .code-area {
    background-color: var(--code-bg);
    color: var(--code-txt);
    border: 2px solid var(--btn-hover);
    padding: 0.25em 0.5em;
    border-radius: 4px;
    font-family: 'Fira Code', monospace;
  }

  button.clipboard {
    color: var(--link);
    background-color: transparent;
    border: none;
    cursor: pointer;

    &:hover {
      color: var(--link-hover);
    }

    &:active {
      color: var(--link-active);
      transform: scale(0.95);
    }
  }
}
</style>
