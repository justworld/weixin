import Vue from 'vue'
import Vuet from 'vuet'

Vue.use(Vuet)

import API from '../api'

export default new Vuet({
  modules: {
    user: {
      data() {
        return {
          userId: 0
        }
      },
      manuals: {
        createUser({state}, name, password) {
          return API.reg(name, password)
        },
        async login({state}, name, password) {
          let data = await API.login(name, password)
          if (data.result) {
            state.userId = data.data
            sessionStorage.setItem('weixin', data.data)
          }
          return data
        },
        addFriend({state}, friendId) {
          return API.addFriend(state.userId, friendId)
        }
      }
    },

  }
})
