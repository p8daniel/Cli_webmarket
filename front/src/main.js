import Vue from 'vue'
import App from './App.vue'
import vuetify from './plugins/vuetify';
import router from './router';

Vue.config.productionTip = false

new Vue({
  vuetify,
  router,
  render: h => h(App)
}).$mount('#app')




/*export default new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  route: [
    {
      path: '/',
      name: 'home',
      component: Home
    },
    {
      path: '/about',
      name: 'about',

      component: () => import(/!* webpackChunkName: "about" *!/ './views/About.vue/')
    }
  ]

})*/
