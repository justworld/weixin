import Vue from 'vue'
import Vuet from 'vuet'

Vue.use(Vuet)

import API from '../api'

export default new Vuet({
  modules: {
    reg: {
      data() {
        return {}
      },
      manuals: {
        createUser({state}, name, password) {
          console.log(state)
          API.reg(name, password)
        }
      }
    },

  }
})
