import { createRouter, createWebHistory } from 'vue-router'
import Main from '@/views/Main.vue'
import Blog from '@/views/Blog.vue'
import Jupyter from '@/views/Jupyter.vue'
import MD from '@/views/MD.vue'

const routes = [
  { path: '/', name: 'Main', component: Main },
  { path: '/blog', name: 'Blog', component: Blog },
  {
    path: '/jupyter/:postUrl',
    name: 'Jupyter',
    component: Jupyter,
    props: route => ({ postUrl: route.params.postUrl })
  },
  {
    path: '/md/:postUrl',
    name: 'MD',
    component: MD,
    props: route => ({ postUrl: route.params.postUrl })
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router
