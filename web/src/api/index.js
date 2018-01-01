import axios from 'axios'

//配置
axios.defaults.baseURL = 'http://localhost:8000'
axios.defaults.headers.post['Content-Type'] = 'application/json'

export default {
  login() {
    axios.post('/login').then(function (response) {
      console.log(response)
    })
  },
  reg(name, password) {
    axios.post('/reg', {
        name: name,
        password: name
      }
    ).then(function (response) {
      console.log(response)
    })
  }
}
