<template>
  <div class="banner">
    <div class="inner">
      <div class="title">登录</div>
      <form class="login_form">
        <div class="login-panel">
          <div class="login-div">
            <label class="icon icon-un" for="account"></label>
            <input id="account" placeholder="帐号" type="text">
            <i class="clear"></i>
          </div>
          <div class="login-div">
            <label class="icon icon-pwd" for="password"></label>
            <input id="password" placeholder="密码" type="password">
            <i class="clear"></i>
          </div>
        </div>
        <div class="login-panel">
          <div style="width: 100%;height: 15px;">
            <a title="点击注册" href="/reg" class="btn-reg">注册帐号</a>
          </div>
        </div>
        <div class="login-panel">
          <a title="点击登录" href="javascript:;" class="btn-login">登录</a>
        </div>
      </form>
    </div>
  </div>
</template>

<style scoped>
  @import "../assets/css/login.css";
</style>
