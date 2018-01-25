import Vue from 'vue'
import Vuet from 'vuet'

Vue.use(Vuet)

import API from '../api'

export default new Vuet({
  modules: {
    user: {
      data() {
        return {
          username: ''
        }
      },
      manuals: {
        createUser({state}, name, password) {
          return API.reg(name, password)
        },
        async login({state}, name, password) {
          const data = await API.login(name, password)
          if (data.result) {
            state = {username: name}
          }
          return data
        }
      }
    },

  }
})