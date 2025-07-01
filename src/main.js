import { createApp } from 'vue'
import { library } from '@fortawesome/fontawesome-svg-core'
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'
import './style.css'
import App from './App.vue'
import i18n from './i18n'

import { 
    faChevronDown, faChevronUp, 
    faBriefcase, faEnvelopeOpenText, faBars, faAward, faBarsProgress,
    faLanguage
} from '@fortawesome/free-solid-svg-icons'

library.add(faChevronDown, faChevronUp, faBriefcase, faEnvelopeOpenText, faBars, faAward, faBarsProgress, faLanguage)

const app = createApp(App)
app.component('font-awesome-icon', FontAwesomeIcon)
app.use(i18n)
app.mount('#app')
