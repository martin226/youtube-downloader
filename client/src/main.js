import 'bootstrap/dist/css/bootstrap.css';
import VueSweetalert2 from 'vue-sweetalert2';
import '@fortawesome/fontawesome-free/js/all.js';
import Vue from 'vue';
import App from './App.vue';
import router from './router';
import './registerServiceWorker'

Vue.use(VueSweetalert2);

Vue.config.productionTip = false;

new Vue({
  router,
  render: h => h(App),
}).$mount('#app');
