import { createI18n } from 'vue-i18n'

import en from './en.json'
import be from './be.json'

const i18n = createI18n({
    legacy: false, // Composition API
    locale: 'en',  // Default language
    fallbackLocale: 'en',
    messages: {
        en,
        be,
    },
})

export default i18n
