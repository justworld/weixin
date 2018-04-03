<template>
  <div class="top">
    <div class="right" style="right: 60px;">
      <i class="weui_icon_search"></i>
    </div>
    <div class="right">
      <span class="iconfont icon-tips-jia" @click="showMenu"></span>
      <ul class="menu" :class="isShowMenu?'menu-open':'menu-close'">
        <li>
          <span class="iconfont icon-tips-xiaoxi"></span>
          <div>发起群聊</div>
        </li>
        <li>
          <span class="iconfont icon-tips-add-friend"></span>
          <div><a @click="$router.replace('/contact/add');isShowMenu=false">添加朋友</a></div>
        </li>
        <li>
          <span class="iconfont icon-tips-saoyisao"></span>
          <div>扫一扫</div>
        </li>
        <li>
          <span class="iconfont icon-tips-fukuan"></span>
          <div>收付款</div>
        </li>
      </ul>
    </div>
    <div class="left">微信</div>
  </div>
</template>

<script>
  export default {
    data() {
      return {
        isShowMenu: false,
      }
    },
    created() {
    },
    methods: {
      showMenu() {
        const that = this
        that.isShowMenu = !that.isShowMenu
      },
    }
  }
</script>

<style scoped>
  .top {
    position: relative;
    z-index: 2;
    height: 45px;
    padding: 0 15px 0 10px;
    line-height: 45px;
    background: linear-gradient(to bottom, #303036, #3c3b40);
    opacity: 1;
    color: #ffffff;
    user-select: none;
    -webkit-user-select: none;
    transition: .22s all ease;
  }

  .left {
    text-align: left;
  }

  .right {
    position: absolute;
    right: 15px;
  }

  .top .iconfont {
    font-size: 22px;
  }

  .weui_icon_search:before {
    color: #fff;
    font-size: 18px;
    font-weight: bolder;
  }

  .menu {
    position: absolute;
    z-index: 2;
    width: 166px;
    font-size: 16px;
    right: -10px;
    top: 45px;
    text-align: left;
    border-radius: 2px;
    background-color: #49484b;
    padding: 0 15px;
    transform-origin: 90% 0%;
  }

  .menu-open {
    transition: initial;
    opacity: 1;
  }

  .menu-close {
    opacity: 0;
    transition: .2s opacity ease, .6s transform ease;
    transform: scale(0);
  }

  .menu li {
    position: relative;
    height: 40px;
    line-height: 40px;
  }

  .menu .iconfont {
    float: left;
    margin-right: 15px;
    font-size: 14px;
  }
</style>
