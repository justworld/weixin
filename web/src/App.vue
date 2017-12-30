<template>
  <div id="app">
    <!-- 头部 -->
    <div class="header" v-show="load"></div>
    <!-- 主体 -->
    <div class="content" v-show="load"></div>
    <!-- di bu导航 -->
    <div class="footer" v-show="load"></div>
    <!-- 欢迎页 -->
    <div class="welcome" v-show="welcome" transition="welcome"></div>
    <router-view/>
  </div>
</template>

<script>
  export default {
    data() {
      return {
        load: false,//加载
        welcome: true,
      }
    },
    created() {
      const that = this
      if (that.$route.matched.length === 1) {
        that.welcome = true;
      }
      that.load = true;
      setTimeout(() => {
        that.welcome = false;
      }, 2000)
    }
  }
</script>

<style scoped>
  .welcome {
    width: 100%;
    height: 100%;
    z-index: 1000;
    position: fixed;
    left: 0;
    top: 0;
    transition: .25s all linear;
    background: url(./assets/images/launchimage.png) no-repeat center center;
    background-size: cover;
  }
  .welcome-leave {
    opacity: 0;
  }
</style>
