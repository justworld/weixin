<template>
  <div class="top">
    <div class="right" style="right: 60px;">
      <i class="weui_icon_search search"></i>
    </div>
    <div class="right">
      <span class="iconfont icon-tips-jia"></span>
    </div>
    <div class="left">微信</div>
  </div>
</template>

<style scoped>
  .top {
    position: relative;
    z-index: 2;
    overflow: hidden;
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
  .left{
    text-align: left;
  }
  .right{
    position: absolute;
    right: 15px;
  }
  .top .iconfont{
    font-size: 22px;
  }
  .top .search{
    color: #fff;
    font-size: 18px;
    font-weight: bolder;
  }
</style>
