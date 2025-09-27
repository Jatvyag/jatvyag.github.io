import { defineStore } from 'pinia'
import { ref } from 'vue'

export const useJupyterStore = defineStore('jupyterIframe', () => {
  const iframeDoc = ref(null) // iframe html-document object
  const iframeRef = ref(null) // reference to the iframe element

  return { iframeDoc, iframeRef }
})
