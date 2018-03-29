import Vue from 'vue'
import App from './App'
import router from './router'
import vuet from './vuet'

import components from './components'

Object.keys(components).forEach((key) => {
  let name = key.replace(/(\w)/, (v) => v.toUpperCase())
  Vue.component(`v${name}`, components[key])//注册公共组件
})


new Vue({
  el: '#app',
  router,
  vuet,
  template: '<App/>',
  components: {App}
})
