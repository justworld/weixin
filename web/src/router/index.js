import ChatIndex from '@/pages/chat'

import Login from '@/pages/login.vue'
import Reg from '@/pages/reg.vue'

export default [
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
