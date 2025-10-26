<template>
  <section
    :ref="sectionLink"
    class="section last"
  >
    <h2>{{ t('navMenu.main.contacts') }}</h2>
    <p class="p-contacts">
      {{ t('contacts.email_client') }}:
      <ContactEmail
        :email-address="contactsData.email"
      />
    </p>
    <p class="p-contacts">
      {{ t('contacts.email_address') }}
    </p>
    <ClipBoard
      :clip-board-value="contactsData.email"
    />
    <p class="p-contacts">
      {{ t('contacts.social_platforms') }}
    </p>
    <SocialMediaArray
      :social-media-array="contactsData.social"
    />
    <p class="p-contacts">
      {{ t('contacts.before_form_par') }}:
    </p>
    <form
      ref="formRef"
      class="form-contacts"
      novalidate
      @submit.prevent="handleSubmit"
    >
      <BasicInput
        v-model:basic-input-model="formData.userName.text"
        :input-error-model="formData.userName.errorKey ? t(formData.userName.errorKey) : ''"
        :label="t('contacts.form.name')"
        name="userName"
        type="text"
        input-class="form-contacts__input"
        :disabled="isSubmitting"
      />
      <BasicInput
        v-model:basic-input-model="formData.userEmail.text"
        :input-error-model="formData.userEmail.errorKey ? t(formData.userEmail.errorKey) : ''"
        :label="t('contacts.form.email')"
        name="userEmail"
        type="email"
        input-class="form-contacts__input"
        :disabled="isSubmitting"
      />
      <TextAreaInput
        v-model:text-area-input-model="formData.userMessageText.text"
        :input-error-model="formData.userMessageText.errorKey ? t(formData.userMessageText.errorKey) : ''"
        :label="t('contacts.form.message')"
        name="userMessageText"
        :rows="4"
        type="text"
        input-class="form-contacts__textarea"
        required
        :disabled="isSubmitting"
      />
      <button
        type="submit"
        class="form-contacts__btn"
        :disabled="isSubmitting"
      >
        {{ t('contacts.form.send') }}
      </button>
    </form>
    <ChevronSection
      :section-ref="firstSection"
      :is-up="true"
    />
  </section>
</template>

<script setup>
import { reactive, ref, watch } from 'vue'
import { useToast } from 'vue-toastification'
import { ContactEmail, ClipBoard, SocialMediaArray } from '@/sections/components'
import { BasicInput, TextAreaInput } from '@/form'
import { ChevronSection } from '@/components'
import JSONData from '@/data/main.json'
import { useI18n } from 'vue-i18n'

const { t, locale } = useI18n()
const toast = useToast()

const CONTACT_API = import.meta.env.VITE_CONTACT_API

const { sectionLink, firstSection } = defineProps({
  sectionLink: {
    type: Object,
    required: true
  },
  firstSection: {
    type: Object,
    required: true
  }
})

const contactsData = JSONData.contacts

// Refs
const formRef = ref(null)

// Reactive data
const formData = reactive({
  userName: { text: '', errorKey: '' },
  userEmail: { text: '', errorKey: '' },
  userMessageText: { text: '', errorKey: '' }
})

const isSubmitting = ref(false)

// Field labels for the form
const fieldLabels = {
  userName: t('contacts.form.name'),
  userEmail: t('contacts.form.email'),
  userMessageText: t('contacts.form.message')
}

/**
 * Sends the form data to the backend
 */
const handleSubmit = async () => {
  let isFormValid = true

  // Reset errors
  Object.keys(formData).forEach(key => {
    formData[key].errorKey = ''
  })

  // Validation
  const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/
  if (formData.userEmail.text && !emailRegex.test(formData.userEmail.text)) {
    formData.userEmail.errorKey = 'contacts.form.valid_email'
    isFormValid = false
  }

  if (!formData.userMessageText.text) {
    formData.userMessageText.errorKey = 'contacts.form.required_field'
    isFormValid = false
  }

  if (!isFormValid) return

  // Prepare payload
  const payload = {
    userName: formData.userName.text,
    userEmail: formData.userEmail.text,
    userMessageText: formData.userMessageText.text,
    locale: locale.value
  }

  isSubmitting.value = true
  toast.warning(t('contacts.form.submission_pending'))

  try {
    // 60-second timeout wrapper
    const controller = new AbortController()
    const timeoutId = setTimeout(() => controller.abort(), 60000) // 60s

    const response = await fetch(CONTACT_API, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(payload),
      signal: controller.signal
    })
    clearTimeout(timeoutId)

    const result = await response.json()

    if (response.ok && result.success) {
      toast.success(t('contacts.form.success_message'))
      // Reset form
      Object.keys(formData).forEach(key => {
        formData[key].text = ''
      })
    } else {
      let toastMessage = result.message
      if (result.errors && Array.isArray(result.errors)) {
        const errorItems = []
        result.errors.forEach(err => {
          Object.entries(err).forEach(([field, msg]) => {
            const label = fieldLabels[field] || field
            errorItems.push(`- ${label}: ${msg}`)
          })
        })
        // Combine main message with errors
        toastMessage += ':\n' + errorItems.join('\n')
      }
      toast.error(toastMessage)
    }
  } catch (error) {
    if (error.name === 'AbortError') {
      toast.error(t('contacts.form.timeout'))
    } else {
      toast.error(t('contacts.form.failed_connection'))
    }
  } finally {
    isSubmitting.value = false
  }
}

// Clear the error style when the user has typed something
Object.keys(formData).forEach(key => {
  // If the text property is changed, then the user has typed something.
  watch(() => formData[key].text, () => {
    // If the errorKey is not empty, then reset it to an empty string.
    if (formData[key].errorKey) {
      formData[key].errorKey = ''
    }
  })
})
</script>

<style lang="scss" scoped>
@use 'sass:map';
@use '@/styles/abstracts/variables' as *;

.section.last{
  min-height: 80vh;
}

.p-contacts {
  margin: 0.5rem;
}

.form-contacts {
  min-width: 600px;
  max-width: 1200px;
  margin-top: 1rem;
  padding: 1rem;
  background-color: var(--card-bg);
  border-radius: 10px;
  box-shadow: var(--card-shadow);

  .form-contacts__btn {
    align-self: flex-end;
    padding: 0.5rem 1rem;
    font-size: 1rem;
    background-color: var(--submit-btn);
    color: var(--text-color);
    border: 2px solid var(--btn-hover);
    border-radius: 10px;
    cursor: pointer;
    transition: background-color 0.3s ease;

    &:hover {
      background-color: var(--link-hover);
    }

    &:disabled {
      opacity: 0.6;
      cursor: wait;
      background-color: var(--bg-color);
      border: 2px dashed var(--btn-hover);
    }
  }

  @media (max-width: 600px) {
    min-width: 100px;
  }
}
</style>
