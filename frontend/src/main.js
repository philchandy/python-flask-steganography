import { createApp } from 'vue'
import App from './App.vue'
import './assets/tailwind.css'
import '../node_modules/flowbite-vue/dist/index.css'
import router from './router';

createApp(App)
  .use(router)
  .mount('#app');