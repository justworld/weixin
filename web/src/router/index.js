import Vue from 'vue'
import VueRouter from 'vue-router'
Vue.use(VueRouter)

import ChatIndex from '@/pages/chat'

import Login from '@/pages/login.vue'
import Reg from '@/pages/reg.vue'

import Contact from '@/pages/contact'
import AddFriend from '@/pages/contact/add.vue'

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
  },
  {
    path: '/contact',
    name: 'contact',
    component: Contact
  },
  {
    path: '/contact/add',
    name: 'addFriend',
    component: AddFriend
  }
]

export default new VueRouter({
  routes,
  mode: 'history', //路由模式
})
