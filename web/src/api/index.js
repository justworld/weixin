import axios from 'axios'

//配置
axios.defaults.baseURL = 'http://localhost:8000'
axios.defaults.headers.post['Content-Type'] = 'application/json'

export default {
  login(name, password) {
    return axios.post('/login', {
      name: name,
      password: password
    }).then(res => res.data)
  },
  reg(name, password) {
    return axios.post('/reg', {
        name: name,
        password: password
      }
    ).then(res => res.data)
  },
  addFriend(userId, friendId) {
    debugger
    return axios.post('/addFriend', {
        userId: userId,
        friendId: friendId
      }
    ).then(res => res.data)
  }
}
