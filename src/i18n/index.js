import { createI18n } from 'vue-i18n'

import en from '@/i18n/en.json'
import be from '@/i18n/be.json'

const savedLocale = sessionStorage.getItem('locale') || 'en'

const i18n = createI18n({
    legacy: false, // Composition API
    locale: savedLocale,  // Default language
    fallbackLocale: 'en',
    messages: {
        en,
        be,
    },
})

export default i18n
