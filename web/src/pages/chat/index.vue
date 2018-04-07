<template>
  <ul class="chat-list">
    <li>
      <div class="info" @click="goDialog">
        <div class="icobox">
          <i class="count">1</i>
          <div class="ico">
            <img src="//ad-gold-cdn.xitu.io/1499913766441c45960d8bd44ed5ffcf0d4a67d0aa317.jpg">
          </div>
        </div>
        <div class="summary">
          <div class="time">23:34</div>
          <div class="title">612</div>
          <div class="message">以前有</div>
        </div>
      </div>
    </li>
  </ul>
</template>

<script>
  export default {
    created() {
      this.$parent.showNav = true
    },
    methods: {
      goDialog() {
        const that = this;
        that.$router.replace('/chat/dialog')
      },
    }
  }
</script>

<style scoped>
  .chat-list {
    position: relative;
    overflow-x: hidden;
    height: 100%;
  }
  .chat-list li{
    position: relative;
    height: 64px;
    transition: .3s height ease;
  }
  .chat-list .info {
    position: relative;
    z-index: 2;
    left: 0;
    width: 100%;
    padding: 8px;
    background-color: #ffffff;
    transition: .2s all linear;
  }
  .chat-list .icobox{
    position: relative;
    float: left;
    width: 48px;
    height: 48px;
    margin-right: 10px;
  }
  .chat-list .icobox .count{
    position: absolute;
    font-style: initial;
    font-family: PingFang SC, Hiragino Sans GB, Arial, Microsoft YaHei, Helvetica;
    right: -9px;
    top: -5px;
    z-index: 2;
    padding: 0 4px;
    width: auto;
    min-width: 18px;
    height: 18px;
    line-height: 18px;
    border-radius: 9px;
    color: #ffffff;
    text-align: center;
    font-size: 14px;
    background-color: #f43531;
  }
  .chat-list .icobox .dot{
    position: absolute;
    right: -3px;
    top: -3px;
    width: 10px;
    height: 10px;
    z-index: 2;
    border-radius: 50%;
    color: #ffffff;
    text-align: center;
    background-color: red;
    background-color: #f43531;
    font-size: 0;
  }
  .chat-list .icobox .ico{
    height: 100%;
    border-radius: 5px;
    overflow: hidden;
  }
  .chat-list .ico img{
    width: 100%;
    border: 0;
  }
  .chat-list .summary .time{
    float: right;
    color: #b2b2b2;
    font-size: 12px;
  }
  .chat-list .summary .title{
    height: 25px;
    line-height: 25px;
    font-size: 18px;
    color: #000;
  }
  .chat-list .summary .message{
    height: 23px;
    line-height: 23px;
    font-size: 14px;
    color: #888888;
  }
</style>
