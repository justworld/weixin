import Vue from 'vue'
import Vuet from 'vuet'

Vue.use(Vuet)

import API from '../api'

export default new Vuet({
  modules: {
    user: {
      data() {
        return {
          userId: 0,
          userName: ''
        }
      },
      manuals: {
        createUser({state}, name, password) {
          return API.reg(name, password)
        },
        async login({state}, name, password) {
          state.userId = 2
          return await API.login(name, password)
        },
        addFriend({state}, friendId) {
          return API.addFriend(state.userId, friendId)
        }
      }
    },

  }
})
