import Vue from 'vue'
import Router from 'vue-router'
// import Home from './views/Home.vue'

import ProductList from './components/ProductList';
import Basket from './components/Basket';
import MyAccount from './components/MyAccount';
import BasketCheckout from './components/BasketCheckout'
import Register from './components/Register'

Vue.use(Router)


export default new Router({
 mode: 'history',
 base: process.env.BASE_URL,
 routes: [
   // {
   //   path: '/',
   //   name: 'home',
   //   component: Home
   // },
   {
     path: '/about',
     name: 'about',
     // route level code-splitting
     // this generates a separate chunk (about.[hash].js) for this route
     // which is lazy-loaded when the route is visited.
     component: () => import(/* webpackChunkName: "about" */ './views/About.vue')
   },
     {
         name: 'Home',
         path: '/',
         // params: ['search', 'search_category'],
         component: ProductList
     },
// },{
//      path: '/search',
//          component: ProductList,
//          props: (route) => ({ query: route.query.q })
//      },
{
    path: '/:search',
  props:true,
  component: ProductList
},

{
    path: '/category/:search_category',
    props:true,
    component: ProductList
},

     {
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
})