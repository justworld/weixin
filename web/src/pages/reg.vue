<template>
  <div class="banner">
    <div class="inner">
      <div class="title">注册</div>
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
          <div class="login-div">
            <label class="icon icon-pwd" for="password-sure"></label>
            <input id="password-sure" placeholder="确认密码" type="password" v-model="passwordSure">
            <i class="clear" v-show="passwordSure" @click="clear('passwordSure')"></i>
          </div>
        </div>
        <div class="login-panel">
          <div style="width: 100%;height: 15px;">
            <a title="点击登录" @click="$router.replace('/login')" class="btn-reg">登录</a>
          </div>
        </div>
        <div class="login-panel">
          <a title="点击注册" href="javascript:;" class="btn-login" @click="submit">注册</a>
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
        passwordSure: '',
        error: ''
      }
    },
    methods: {
      clear(name) {
        const that = this
        console.log(that)
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
        if (!that.passwordSure) {
          that.error = '请确认您的密码'
          return
        }
        if (that.passwordSure !== that.password) {
          that.error = '两次密码输入不一致'
          return
        }
        //注册
        that.error = ''
        const data = await that.$user.createUser(that.account, that.password)
        if (data.result) {
          that.$router.replace('/login')
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
