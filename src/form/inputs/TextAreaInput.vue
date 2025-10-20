<template>
  <label
    v-if="label"
    :for="name"
  >
    {{ label }}
    <span
      v-if="required"
      class="required-asterisk"
      aria-hidden="true"
      :title="t('form.required_field')"
    >*</span>
  </label>
  <div>
    <textarea
      ref="textAreaInputRef"
      :value="textAreaInputModel"
      :type="type"
      :name="name"
      :rows="rows"
      :class="[inputClass, { invalid: inputErrorModel, required: required }]"
      :required="required"
      :aria-invalid="!!inputErrorModel"
      @input="$emit('update:textAreaInputModel', $event.target.value)"
    />
    <span
      v-if="inputErrorModel"
      class="error-message"
      aria-live="polite"
    >{{ inputErrorModel }}</span>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useI18n } from 'vue-i18n'

const { t } = useI18n()

const textAreaInputRef = ref(null)

defineExpose({ textAreaInputRef })

defineModel('textAreaInputModel', {
  type: [String, Number],
  default: ''
})

defineModel('inputErrorModel', {
  type: String,
  default: ''
})

defineEmits(['update:textAreaInputModel'])

const { label, name, rows, type, inputClass, required } = defineProps({
  label: { type: String, default: '' },
  name: { type: String, required: true },
  rows: { type: Number, default: 5 },
  type: { type: String, default: 'text' },
  inputClass: { type: String, default: '' },
  required: { type: Boolean, default: false }
})
</script>

<style lang="scss" scoped>
@use 'sass:map';
@use '@/styles/abstracts/variables' as *;

.form-contacts__textarea {
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

  &.required {
    background-color: $required-bg-color;
  }

  &.required:focus {
    background-color: var(--code-bg);
  }
}

.required-asterisk {
  color: $attention-color;
  margin-left: 0.25rem;
  cursor: help;
}
</style>
