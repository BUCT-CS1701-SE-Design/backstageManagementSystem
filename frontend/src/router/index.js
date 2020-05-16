import Vue from 'vue'
import VueRouter from 'vue-router'
import Hello from '../components/HelloWorld.vue'
import Signin from '../components/Signin.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/S',
    name: 'Signin',
    component: Signin
  },
  {
    path: '/Home',
    name: 'Home',
    component: Hello
  },
  {
    path: '/about',
    name: 'About',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/About.vue')
  }
  // {
  //   path: '/backsys',
  //   name: 'sys',
  //   component: Backsys
  // }
]

const router = new VueRouter({
  routes
})

export default router
