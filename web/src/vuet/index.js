import Vue from 'vue'
import Vuet from 'vuet'

Vue.use(Vuet)

import API from '../api'

export default new Vuet({
  modules: {
    user: {
      data() {
        return {}
      },
      manuals: {
        createUser({state}, name, password) {
          API.reg(name, password).then(function (res) {
            console.log(res)
          })
        },
        login({state}, name, password) {
          API.login(name, password).then(function (res) {
            console.log(res)
          })
        }
      }
    },

  }
})
