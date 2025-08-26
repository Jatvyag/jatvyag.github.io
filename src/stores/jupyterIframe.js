import { defineStore } from 'pinia'
import { ref } from 'vue'

export const useJupyterStore = defineStore('jupyterIframe', () => {
  const iframeDoc = ref(null)

  return { iframeDoc }
})
