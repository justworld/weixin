<template>
  <div class="banner">
    <div class="inner">
      <div class="title">登录</div>
      <div class="err" v-show="error">{{error}}</div>
      <form class="login_form">
        <div class="login-panel">
          <div class="login-div">
            <label class="icon icon-un" for="account"></label>
            <input id="account" placeholder="帐号" type="text" v-model="account">
            <i class="clear" v-show="account" @click="clear('account')"></i>
          </div>
          <div class="login-div">
            <label class="icon icon-pwd" for="password"></label>
            <input id="password" placeholder="密码" type="password" v-model="password">
            <i class="clear" v-show="password" @click="clear('password')"></i>
          </div>
        </div>
        <div class="login-panel">
          <div style="width: 100%;height: 15px;">
            <a title="点击注册" href="/reg" class="btn-reg">注册帐号</a>
          </div>
        </div>
        <div class="login-panel">
          <a title="点击登录" href="javascript:;" class="btn-login" @click="submit">登录</a>
        </div>
      </form>
    </div>
  </div>
</template>

<script>
  import {mapModules, mapRules} from 'vuet'

  export default {
    mixins: [
      mapModules({
        user: 'user'
      }),
      mapRules({
        manual: 'user'
      })
    ],
    data() {
      return {
        account: '',
        password: '',
        error: ''
      }
    },
    methods: {
      clear(name) {
        const that = this
        if (name) {
          that[name] = ''
        }
      },
      async submit() {
        const that = this
        //校验
        if (!that.account) {
          that.error = '请输入帐号'
          return
        }
        if (!that.password) {
          that.error = '请输入密码'
          return
        }
        //登陆
        that.error = ''
        const data = await that.$user.login(that.account, that.password)
        if (data.result) {
          that.$parent.userId = data.data
          that.$parent.userName = that.account
          that.$router.push('/')
        } else {
          that.error = data.msg
        }
      }
    }
  }
</script>

<style scoped>
  @import "../assets/css/login.css";
</style>
