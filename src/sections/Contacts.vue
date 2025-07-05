<script setup>
import { ref } from 'vue'
import JSONData from '../data/data.json'
import { useI18n } from 'vue-i18n'
const { t } = useI18n()

const contactsData = JSONData.contacts

function copyEmail() {
    const email = document.getElementById('email')?.textContent
    if (email) {
        navigator.clipboard.writeText(email)
    }
}

const formRef = ref(null)
const handleSubmit = (event) => {
    event.preventDefault()
    const form = formRef.value
    if (!form) return
    form.classList.add('was-attempted')
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

function clearError(event) {
    const input = event.target
    input.setCustomValidity('')
    const errorSpan = input.nextElementSibling
    if (errorSpan) errorSpan.textContent = ''
}
</script>

<template>
    <section id="contacts" class="section last">
        <h2>{{ t('navMenu.contacts') }}</h2>
        <p class="contacts">{{ t('contacts.email_client') }}: 
            <a :href="`mailto:${contactsData.email}`" title="Email">
                <font-awesome-icon :icon="['fas', 'at']" />
            </a>
        </p>
        <p class="contacts">{{ t('contacts.email_address') }}</p>
        <div class="code-wrapper">
            <code id="email" class="code-area">{{ contactsData.email }}</code>
            <button 
                class="clipboard" 
                @click="copyEmail"
                :title="t('contacts.tooltip_copy')">
                <font-awesome-icon :icon="['fas', 'clipboard']" />
            </button>
        </div>        
        <p class="contacts">{{ t('contacts.social_platforms') }}</p>
        <div class="social-media">
            <a
                v-for="item in contactsData.social"
                :key="item.id"
                :href="item.link"
                :title="item.tooltip"
                target="_blank"
                rel="noopener noreferrer"
                class="social-icon"
            >
                <font-awesome-icon :icon="item.faIcon" />
            </a>
        </div>
        <form
            class="contact-form"
            @submit.prevent.native="handleSubmit" novalidate
            :action="`https://formsubmit.co/${contactsData.email}`"
            method="POST"
            ref="formRef"
        >
            <label>
                {{ t('contacts.form.name') }}
                <input 
                    type="text" 
                    name="name" 
                    required 
                    @input="clearError($event)"
                />
                <span class="error-message" aria-live="polite"></span>
            </label>
            <label>
                {{ t('contacts.form.email') }}
                <input 
                    type="email" 
                    name="email" 
                    required 
                    @input="clearError($event)"
                />
                <span class="error-message" aria-live="polite"></span>
            </label>
            <label>
                {{ t('contacts.form.subject') }}
                <input 
                    type="text" 
                    name="subject" 
                    required 
                    @input="clearError($event)"
                />
                <span class="error-message" aria-live="polite"></span>
            </label>
            <label>
                {{ t('contacts.form.message') }}
                <textarea 
                    name="message" 
                    rows="4" 
                    required 
                    @input="clearError($event)"
                ></textarea>
                <span class="error-message" aria-live="polite"></span>
            </label>
            <button type="submit" class="submit-btn">
                {{ t('contacts.form.send') }}
            </button>
        </form>
    </section>
</template>

<style scoped>
.section.last{
    min-height: 80vh;
}

p.contacts {
    margin: 0.5rem;
}

.code-wrapper {
    display: inline-flex;
    align-items: center;
}

.code-area {
    background-color: var(--code-background);
    color: var(--code-text-color);
    border: 2px solid var(--btn-hover-color);
    padding: 0.25em 0.5em;
    border-radius: 4px;
    font-family: 'Fira Code', monospace;
}

button.clipboard {
    color: var(--link);
    background-color: transparent;
    border: none;
    cursor: pointer;
}

button.clipboard:hover {
    color: var(--link-hover);
}

button.clipboard:active {
    color: var(--link-active); 
    transform: scale(0.95); 
}

.social-media {
    display: flex;
    flex-wrap: wrap;
    gap: 1rem;
    justify-content: center;
    align-items: center;
    margin-top: 0rem;
}

.social-icon {
    font-size: 1.5rem;
    transition: color 0.3s ease;
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
    border-radius: var(--border-radius);
    box-shadow: var(--card-box-shadow);
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
    border: 2px solid var(--btn-hover-color);
    border-radius: 4px;
    background-color: var(--code-background);
    color: var(--text);
}

.submit-btn {
    align-self: flex-end;
    padding: 0.5rem 1rem;
    font-size: 1rem;
    background-color: var(--link);
    color: white;
    border: none;
    border-radius: var(--border-radius);
    cursor: pointer;
    transition: background-color 0.3s ease;
}

.submit-btn:hover {
    background-color: var(--link-hover);
}

.contact-form.was-attempted input:invalid,
.contact-form.was-attempted textarea:invalid {
    border: 1px solid var(--attention-color);
    outline: none;
}

.error-message {
    display: inline-block;
    color: var(--attention-color);
    border-radius: 0px 0px 10px 10px;
    font-size: 0.8rem;
    margin-top: 0rem;
    padding: 0.2rem;
    background-color: #dfc9c9;
    border: 1px solid var(--attention-color);  
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
    border: 1px solid var(--attention-color);
    min-height: 1em;
}

@media (max-width: 600px) {
    .contact-form {
        min-width: 100px;
    }
}
</style>

