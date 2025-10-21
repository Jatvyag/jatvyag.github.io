import { createApp } from 'vue'
import { createPinia } from 'pinia'
import { library } from '@fortawesome/fontawesome-svg-core'
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'
import '@/styles/main.scss'
import App from '@/App.vue'
import router from '@/router'
import VueGtag from 'vue-gtag-next'
import i18n from '@/i18n'
import Toast from 'vue-toastification'
import 'vue-toastification/dist/index.css'

import {
  faChevronDown, faChevronUp,
  faEnvelopeOpenText, faBars, faAward, faBarsProgress, faAt,
  faLanguage, faCopyright, faClipboard, faHouse,
  faAddressCard, faBlog, faForwardStep, faBackwardStep,
  faFilter, faFilterCircleXmark, faGhost
} from '@fortawesome/free-solid-svg-icons'

import {
  faVuejs,
  faLinkedin,
  faGithub,
  faOrcid,
  faFontAwesome
} from '@fortawesome/free-brands-svg-icons'

const savedPath = sessionStorage.getItem('redirect-path')
if (savedPath) {
  sessionStorage.removeItem('redirect-path')
  router.replace(savedPath)
}

library.add(
  faChevronDown, faChevronUp, faEnvelopeOpenText, faAt, faClipboard,
  faBars, faAward, faBarsProgress, faLanguage, faCopyright,
  faHouse, faAddressCard, faBlog, faForwardStep, faBackwardStep,
  faFilter, faFilterCircleXmark, faGhost)
library.add(faVuejs, faLinkedin, faGithub, faOrcid, faFontAwesome)

const GA_MEASUREMENT_ID = import.meta.env.VITE_GA_MEASUREMENT_ID

const app = createApp(App)
app.use(createPinia())
app.use(router)
app.use(i18n)
app.use(VueGtag, {
  property: {
    id: GA_MEASUREMENT_ID,
    config: {
      cookie_domain: 'none'
    }
  },
  pageTrackerScreenviewEnabled: true
}, router)
app.use(Toast)
app.component('FontAwesomeIcon', FontAwesomeIcon)
app.mount('#app')
