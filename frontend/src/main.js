import './assets/base.css'

import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import Toast from 'vue-toastification'
import 'vue-toastification/dist/index.css'

const app = createApp(App)
app.use(router)

app.use(Toast, {
  position: 'top-right',
  timeout: 2000,
  closeOnClick: false,
  pauseOnFocusLoss: false,
  pauseOnHover: true,
  draggable: true,
  draggablePercent: 0.6,
  showCloseButtonOnHover: false,
  hideProgressBar: false,
  closeButton: 'button',
  icon: true,
  rtl: false,
  transition: 'custom-toast',
  maxToasts: 20,
  newestOnTop: true,
})

app.mount('#app')
