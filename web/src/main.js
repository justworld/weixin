import Vue from 'vue'
import App from './App'
import VueRouter from 'vue-router'
import routes from './router'
import components from './components'

Vue.use(VueRouter)

components.install(Vue)//注册公共组件

const router = new VueRouter({
  routes,
  mode: 'history', //路由模式
})

new Vue({
  el: '#app',
  router,
  template: '<App/>',
  components: {App}
})
