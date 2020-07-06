import Vue from 'vue';
import Router from 'vue-router';
import Download from './components/Download.vue';
import NotFound from './components/NotFound.vue';
import Home from './components/Home.vue';

Vue.use(Router);

export default new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/',
      name: 'Homepage',
      component: Home,
    },
    {
      path: '/download/:video_id',
      name: 'Download',
      component: Download,
    },
    {
      path: '/download',
      component: Download,
    },
    {
      path: '*',
      component: NotFound,
    },
  ],
});
