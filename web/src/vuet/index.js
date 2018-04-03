import Vue from 'vue'
import Vuet from 'vuet'

Vue.use(Vuet)

import API from '../api'

export default new Vuet({
  modules: {
    user: {
      data() {
      },
      manuals: {
        createUser({state}, name, password) {
          return API.reg(name, password)
        },
        async login({state}, name, password) {
          let data = await API.login(name, password)
          if (data.result) {
            sessionStorage.setItem('weixin', data.data)
          }
          return data
        },
        addFriend({state}, friendId) {
          const userId = sessionStorage.getItem('weixin')
          return API.addFriend(userId, friendId)
        }
      }
    },

  }
})
