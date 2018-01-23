import axios from 'axios'

//配置
axios.defaults.baseURL = 'http://localhost:8000'
axios.defaults.headers.post['Content-Type'] = 'application/json'

export default {
  login(name, password) {
    return axios.post('/login', {
      name: name,
      password: password
    }).then(function (response) {
      console.log(response)
    })
  },
  reg(name, password) {
    return axios.post('/reg', {
        name: name,
        password: password
      }
    ).then(response => response.data)
  }
}
