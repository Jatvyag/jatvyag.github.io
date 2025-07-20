import { createRouter, createWebHistory } from 'vue-router'
import Main from '@/views/Main.vue'
import Blog from '@/views/Blog.vue'

const routes = [
  { path: '/', name: 'Main', component: Main },
  { path: '/blog', name: 'Blog', component: Blog },
  {
    path: '/jupyter/:postUrl',
    name: 'Jupyter',
    component: () => import('@/views/Jupyter.vue'),
    props: route => ({ postUrl: route.params.postUrl })
  },
  {
    path: '/md/:postUrl',
    name: 'MD',
    component: () => import('@/views/MD.vue'),
    props: route => ({ postUrl: route.params.postUrl })
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router
