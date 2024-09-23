import { createRouter, createWebHistory } from 'vue-router';
import Home from './components/HeroSection.vue';
import HideText from './components/HideText.vue';
import ExtractText from './components/ExtractText.vue';

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home,
  },
  {
    path: '/hide-text',
    name: 'HideText',
    component: HideText,
  },
  {
    path: '/extract-text',
    name: 'ExtractText',
    component: ExtractText,
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;