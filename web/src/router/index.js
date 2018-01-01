import Vue from 'vue'
import VueRouter from 'vue-router'
Vue.use(VueRouter)

import ChatIndex from '@/pages/chat'

import Login from '@/pages/login.vue'
import Reg from '@/pages/reg.vue'

const routes= [
  {
    path: '/',
    name: 'index',
    component: ChatIndex,
  },
  {
    path: '/login',
    name: 'login',
    component: Login
  },
  {
    path: '/reg',
    name: 'reg',
    component: Reg
  }
]

export default new VueRouter({
  routes,
  mode: 'history', //路由模式
})
