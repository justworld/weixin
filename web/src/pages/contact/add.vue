<template>
  <div class="cover">
    <div class="search">
      <span class="iconfont icon-search"></span>
      <input type="text" placeholder="微信号" @click="$router.replace('/contact/info')">
    </div>
    <p style="text-align: center;">我的微信号是：xiap</p>
    <div class="options">
      <a class="cell" href="javascript:;">
        <div><img src="../../assets/images/add-friend-scanqr.png"></div>
        <div class="title"><p>扫一扫</p>
          <p>扫描二维码名片</p></div>
      </a>
    </div>
  </div>
</template>

<script>
  export default {
    methods: {
    }
  }
</script>

<style scoped>
  .cover {
    position: relative;
    width: 100%;
    height: 100%;
    overflow: hidden;
    z-index: 1;
    transition: .2s all ease-in-out;
    opacity: 1;
    transform: translate3d(0%, 0, 0);
    background-color: #efeff4;
    box-shadow: 0px 0 41px rgba(0, 0, 0, 0.1);
  }

  .search {
    position: relative;
    height: 50px;
    padding-left: 30px;
    padding-top: 5px;
    padding-bottom: 5px;
    background-color: #ffffff;
    border-top: 1px solid #d9d9d9;
    border-bottom: 1px solid #d9d9d9;
    margin-top: 20px;
  }

  .icon-search {
    color: #40b938;
  }

  .search input {
    width: calc(100% - 30px);
    font-size: 16px;
    height: 100%;
    border: 0;
    outline: none;
    vertical-align: middle;
    border-bottom: 1px solid #40b938;
  }

  .options {
    margin-top: 1.17647059em;
    background-color: #fff;
    line-height: 1.41176471;
    font-size: 17px;
    overflow: hidden;
    position: relative;
  }

  .options .cell {
    padding: 10px 15px;
    position: relative;
    display: -webkit-box;
    display: -webkit-flex;
    display: flex;
    -webkit-box-align: center;
    -webkit-align-items: center;
    align-items: center;
  }

  .options .cell img {
    width: 35px;
    display: block;
    margin-right: 10px;
  }

  .options .cell p {
    font-size: 15px;
  }

  .options .cell p:last-child {
    font-size: 12px;
    color: #b7b7b7;
  }
</style>
