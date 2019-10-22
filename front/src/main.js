import Vue from 'vue'
import App from './App.vue'
import vuetify from './plugins/vuetify';
// import router from './router';
import VueRouter from 'vue-router'

Vue.config.productionTip = false

Vue.use(VueRouter)

import ProductList from './components/ProductList';
import Basket from './components/Basket';
import MyAccount from './components/MyAccount';
import BasketCheckout from './components/BasketCheckout'
import Register from './components/Register'

// Vue.config.productionTip = false
// Vue.prototype.$eventBus = new Vue()
// export const Authentique = new Vue({
//   data: {
//     is_authentique: false,
//     search:"",
//   }
// })

const routers= [{
 name: 'Home',
 path: '/',
  component: ProductList
},{
 name: 'Basket',
 path: '/basket',
  component: Basket
},{
 name: 'MyAccount',
 path: '/my-account',
  component: MyAccount
},{
  name: 'BasketCheckout',
  path: '/basket/checkout',
  component: BasketCheckout
}
,{
  name: 'Register',
  path: '/register',
  component: Register
}
]

const router = new VueRouter({mode: 'history', routes: routers})

new Vue({
  vuetify,
  router,
  render: h => h(App),
    data: {


    }
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
