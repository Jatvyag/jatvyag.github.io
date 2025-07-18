import { createApp } from 'vue'
import { library } from '@fortawesome/fontawesome-svg-core'
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'
import '@/styles/main.css'
import App from '@/App.vue'
import router from '@/router'
import i18n from '@/i18n'

import { 
    faChevronDown, faChevronUp, 
    faEnvelopeOpenText, faBars, faAward, faBarsProgress, faAt,
    faLanguage, faCopyright, faClipboard, faHouse,
    faAddressCard, faBlog
} from '@fortawesome/free-solid-svg-icons'

import { 
    faVuejs, 
    faLinkedin, 
    faGithub, 
    faOrcid, 
    faFontAwesome
} from '@fortawesome/free-brands-svg-icons'

const savedPath = sessionStorage.getItem('redirect-path');
if (savedPath) {
    sessionStorage.removeItem('redirect-path');
    router.replace(savedPath);
}

library.add(
    faChevronDown, faChevronUp, faEnvelopeOpenText, faAt, faClipboard,
    faBars, faAward, faBarsProgress, faLanguage, faCopyright, 
    faHouse, faAddressCard, faBlog)
library.add(faVuejs, faLinkedin, faGithub, faOrcid, faFontAwesome)

const app = createApp(App)
app.component('font-awesome-icon', FontAwesomeIcon)
app.use(i18n)
app.use(router)
app.mount('#app')
