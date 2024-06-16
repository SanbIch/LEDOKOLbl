// import './assets/main.css'

import { createApp } from 'vue'
import { createPinia } from 'pinia'

import '@mdi/font/css/materialdesignicons.css'
import 'vuetify/styles'
import { createVuetify } from 'vuetify'
import ganttastic from '@infectoone/vue-ganttastic'

import App from './App.vue'
import router from './router'

const vuetify = createVuetify({})

const app = createApp(App)

app.use(vuetify)
app.use(createPinia())
app.use(router)
app.use(ganttastic)

app.mount('#app')
