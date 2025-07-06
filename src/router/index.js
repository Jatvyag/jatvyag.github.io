import { createRouter, createWebHistory } from 'vue-router'
import Main from '../views/Main.vue'
import Blog from '../views/Blog.vue'
import Jupyter from '../views/Jupyter.vue'

const routes = [
    { path: '/', name: 'Main', component: Main },
    { path: '/blog', name: 'Blog', component: Blog },
    {
        path: '/jupyter/:postUrl',
        name: 'JupyterView',
        component: () => import('../views/Jupyter.vue'),
        props: route => ({ post_url: route.params.postUrl })
    }
]

const router = createRouter({
    history: createWebHistory(),
    routes,
})

export default router
