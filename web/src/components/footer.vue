<template>
  <div class="nav">
    <dl :class="{'active':$parent.navIndex==1}" @click="goIndex">
      <dt class="iconfont icon-wechat"></dt>
      <dd>微信</dd>
    </dl>
    <dl :class="{'active':$parent.navIndex==2}" @click="goContact">
      <dt class="iconfont icon-contact"></dt>
      <dd>通讯录</dd>
    </dl>
    <dl :class="{'active':$parent.navIndex==3}">
      <dt class="iconfont icon-find"></dt>
      <dd>发现</dd>
    </dl>
    <dl :class="{'active':$parent.navIndex==4}">
      <dt class="iconfont icon-me"></dt>
      <dd>我</dd>
    </dl>
  </div>
</template>

<script>
  export default {
    methods: {
      goIndex() {
        const that = this
        that.$parent.navIndex = 1
        that.$router.replace('/')
      },
      goContact() {
        const that = this
        that.$parent.navIndex = 2
        that.$router.replace('/contact')
      },
    }
  }
</script>

<style scoped>
  .nav {
    display: flex;
    width: 100%;
    overflow: hidden;
    height: 50px;
    padding-top: 8px;
    background: #f9f9f9;
    font-size: 12px;
  }

  .nav dl {
    user-select: none;
    -webkit-user-select: none;
    flex-grow: 1;
    text-align: center;
    line-height: 1;
  }

  .nav dt {
    position: relative;
    width: 28px;
    height: 28px;
    margin: 0 auto;
    font-size: 28px;
    color: #797979;
    margin-bottom: 2px;
  }

  .nav dd {
    color: #929292;
    transform-origin: 50% 0;
    transform: scale(0.9);
  }

  .nav dl.active dt, .nav dl.active dd {
    color: #0bb908;
  }
</style>
