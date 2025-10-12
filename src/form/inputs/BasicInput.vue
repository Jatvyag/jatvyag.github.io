<template>
  <label
    v-if="label"
    :for="name"
  >{{ label }}</label>
  <div>
    <input
      ref="basicInputRef"
      :value="basicInputModel"
      :type="type"
      :name="name"
      :class="[inputClass, { invalid: inputErrorModel }]"
      :required="required"
      :aria-invalid="!!inputErrorModel"
      @input="$emit('update:basicInputModel', $event.target.value)"
    >
    <span
      v-if="inputErrorModel"
      class="error-message"
      aria-live="polite"
    >{{ inputErrorModel }}</span>
  </div>
</template>

<script setup>
import { ref } from 'vue'

const basicInputRef = ref(null)

defineExpose({ basicInputRef })

defineModel('basicInputModel', {
  type: [String, Number],
  default: ''
})

defineEmits(['update:basicInputModel'])

defineModel('inputErrorModel', {
  type: String,
  default: ''
})

const { label, name, type, inputClass, required } = defineProps({
  label: { type: String, default: '' },
  name: { type: String, required: true },
  type: { type: String, default: 'text' },
  inputClass: { type: String, default: '' },
  required: { type: Boolean, default: false }
})
</script>

<style lang="scss" scoped>
@use 'sass:map';
@use '@/styles/abstracts/variables' as *;

.form-contacts__input {
  border: 2px solid var(--btn-hover);
  border-radius: 4px;
  background-color: var(--code-bg);
  color: var(--text);
  width: 100%;
  transition: border-color 0.3s ease, box-shadow 0.3s ease;

  &:focus {
    outline: none;
    border-color: var(--link-hover);
    box-shadow: 0 0 0 2px rgba(var(--link-hover-rgb), 0.2);
  }

  &.invalid {
    border-color: $attention-color;
  }
}
</style>
