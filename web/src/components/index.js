import header from './header.vue'
import footer from './footer.vue'

const install = function (Vue) {
  if (install.installed) return
  Vue.component('v-header', header)
  Vue.component('v-footer', footer)
}

export default {
  install
}
