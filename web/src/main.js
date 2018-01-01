import Vue from 'vue'
import App from './App'
import router from './router'
import vuet from './vuet'
import components from './components'

components.install(Vue)//注册公共组件

new Vue({
  el: '#app',
  router,
  vuet,
  template: '<App/>',
  components: {App}
})
