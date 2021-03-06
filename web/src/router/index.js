import Vue from 'vue'
import Router from 'vue-router'

Vue.use(Router)

import ChatIndex from '@/pages/chat'
import ChatDialog from '@/pages/chat/dialog.vue'

import Login from '@/pages/login.vue'
import Reg from '@/pages/reg.vue'

import Contact from '@/pages/contact'
import AddFriend from '@/pages/contact/add.vue'
import ContactInfo from '@/pages/contact/info.vue'

const routes = [
  {
    path: '/',
    name: 'index',
    meta: {nav: true},
    component: ChatIndex,
  },
  {
    path: '/login',
    name: 'login',
    meta: {auth: false},
    component: Login
  },
  {
    path: '/reg',
    name: 'reg',
    meta: {auth: false},
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
  },
  {
    path: '/contact/info',
    name: 'info',
    component: ContactInfo
  },
  {
    path: '/chat/dialog/:friend',
    name: 'dialog',
    component: ChatDialog
  }
]

const router = new Router({
  routes,
  mode: 'history', //路由模式
})

//路由变换之前
router.beforeEach(async (to, from, next) => {
  const {auth = true} = to.meta//是否需要登陆
  if (auth) {
    const userId = sessionStorage.getItem('weixin')
    if (userId != null) {
      next()
      return
    } else {
      next(false)
      router.replace('/login')
    }
  }
  next()

})


export default router
