<template>
  <section
    :ref="sectionLink"
    class="section last"
  >
    <h2>{{ t('navMenu.main.contacts') }}</h2>
    <p class="contacts">
      {{ t('contacts.email_client') }}:
      <ContactEmail
        :email-address="contactsData.email"
      />
    </p>
    <p class="contacts">
      {{ t('contacts.email_address') }}
    </p>
    <ClipBoard
      :clip-board-value="contactsData.email"
    />
    <p class="contacts">
      {{ t('contacts.social_platforms') }}
    </p>
    <SocialMediaArray
      :social-media-array="contactsData.social"
    />
    <form
      ref="formRef"
      class="contact-form"
      :class="{ 'was-attempted': wasAttempted }"
      novalidate
      :action="`https://formsubmit.co/${contactsData.email}`"
      method="POST"
      @submit.prevent="handleSubmit"
    >
      <!-- TODO: отдельный компонент -->
      <label>
        {{ t('contacts.form.name') }}
        <input
          type="text"
          name="name"
          required
          @input="clearError($event)"
        >
        <span
          class="error-message"
          aria-live="polite"
        />
      </label>
      <label>
        {{ t('contacts.form.email') }}
        <input
          type="email"
          name="email"
          required
          @input="clearError($event)"
        >
        <span
          class="error-message"
          aria-live="polite"
        />
      </label>
      <label>
        {{ t('contacts.form.subject') }}
        <input
          type="text"
          name="subject"
          required
          @input="clearError($event)"
        >
        <span
          class="error-message"
          aria-live="polite"
        />
      </label>
      <label>
        {{ t('contacts.form.message') }}
        <textarea
          name="message"
          rows="4"
          required
          @input="clearError($event)"
        />
        <span
          class="error-message"
          aria-live="polite"
        />
      </label>
      <button
        type="submit"
        class="submit-btn"
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
import { ref } from 'vue'
import { ContactEmail, ClipBoard, SocialMediaArray } from '@/sections/components'
import ChevronSection from '@/components'
import JSONData from '@/data/main.json'
import { useI18n } from 'vue-i18n'
const { t } = useI18n()

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
const wasAttempted = ref(false)

const handleSubmit = (event) => {
  event.preventDefault()
  const form = formRef.value
  if (!form) return

  // Toggle form class was-attempted
  wasAttempted.value = true

  // TODO: refs
  const inputs = form.querySelectorAll('input, textarea')
  let isFormValid = true
  inputs.forEach(input => {
    input.setCustomValidity('')
    if (!input.checkValidity()) {
      isFormValid = false
      let message = ''
      if (input.validity.valueMissing) {
        message = t('contacts.form.required_field')
      } else if (input.validity.typeMismatch) {
        message = t('contacts.form.valid_email')
      }
      input.setCustomValidity(message)
      const errorSpan = input.nextElementSibling
      if (errorSpan) errorSpan.textContent = message
    } else {
      const errorSpan = input.nextElementSibling
      if (errorSpan) errorSpan.textContent = ''
    }
  })
  if (isFormValid) {
    form.submit()
  }
}

function clearError (event) {
  const input = event.target
  input.setCustomValidity('')
  const errorSpan = input.nextElementSibling
  if (errorSpan) errorSpan.textContent = ''
}
</script>

<style lang="scss" scoped>
.section.last{
  min-height: 80vh;
}

p.contacts {
  margin: 0.5rem;
}

.contact-form {
    display: flex;
    flex-direction: column;
    gap: 1rem;
    min-width: 600px;
    max-width: 1200px;
    margin-top: 1rem;
    padding: 1rem;
    background-color: var(--card-bg);
    border-radius: 10px;
    box-shadow: var(--card-shadow);
}

.contact-form label {
    display: flex;
    flex-direction: column;
    font-weight: bold;
}

.contact-form input,
.contact-form textarea {
    padding: 0.5rem;
    font-size: 1rem;
    border: 2px solid var(--btn-hover);
    border-radius: 4px;
    background-color: var(--code-bg);
    color: var(--text);
}

.submit-btn {
    align-self: flex-end;
    padding: 0.5rem 1rem;
    font-size: 1rem;
    background-color: var(--link);
    color: white;
    border: none;
    border-radius: 10px;
    cursor: pointer;
    transition: background-color 0.3s ease;
}

.submit-btn:hover {
    background-color: var(--link-hover);
}

.contact-form.was-attempted input:invalid,
.contact-form.was-attempted textarea:invalid {
    border: 1px solid #e63946;
    outline: none;
}

.error-message {
    display: inline-block;
    color: #e63946;
    border-radius: 0px 0px 10px 10px;
    font-size: 0.8rem;
    margin-top: 0rem;
    padding: 0.2rem;
    background-color: #dfc9c9;
    border: 1px solid #e63946;
    min-height: 1em;
    /* Keep space reserved but invisible */
    min-height: 1em;
    visibility: hidden;
    opacity: 0;
    transition: opacity 0.3s ease;
}

.error-message:empty {
    visibility: hidden;
    opacity: 0;
    padding: 0;
    border: none;
    min-height: 0;
}

.error-message:not(:empty) {
    visibility: visible;
    opacity: 1;
    padding: 0.2rem;
    border: 1px solid #e63946;
    min-height: 1em;
}

@media (max-width: 600px) {
    .contact-form {
        min-width: 100px;
    }
}
</style>
