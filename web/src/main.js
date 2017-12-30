import Vue from 'vue'
import App from './App'
import VueRouter from 'vue-router'
import routes from './router'

Vue.use(VueRouter)

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
