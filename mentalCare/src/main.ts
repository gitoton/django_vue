import { createApp } from 'vue'
import './style.css'
import App from './App.vue'
import { worker } from './mocks/browser'

if(import.meta.env.NODE_ENV === 'development'){
  worker.start()
}

createApp(App).mount('#app')
