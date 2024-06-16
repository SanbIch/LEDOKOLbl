import { createRouter, createWebHistory } from 'vue-router'
// import MainView from '../views/MainView.vue'
import MapView from '@/views/MapView.vue'
import RequestView from '@/views/RequestView.vue'
import GanttaView from '@/views/GanttaView.vue'
import UploadIce from '@/views/UploadIce.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'root',
      component: MapView
    },
    {
      path: '/map',
      name: 'map',
      component: MapView
    },
    {
      path: '/request',
      name: 'request',
      component: RequestView
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      // component: () => import('../views/AboutView.vue')
    },
    {
      path: '/icebreakers',
      name: 'icebreakers',
      component: GanttaView
    },
    {
      path: '/upload_ice',
      name: 'upload_ice',
      component: UploadIce
    }
  ]
})

export default router
