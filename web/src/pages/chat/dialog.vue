<template>
  <div style="background-color: #efeff4;height: 100%;">
    <div class="dialog">

    </div>
    <div class="footer">
      <span class="iconfont icon-dialogue-voice"></span>
      <div class="chat">
        <input class="chat-txt" v-on:keyup.13="sendMsg()" v-model="msg"/>
      </div>
      <span class="iconfont icon-dialogue-smile"></span>
      <span class="iconfont icon-dialogue-jia"></span>
    </div>
  </div>
</template>

<script>
  export default {
    data() {
      return {
        msg: ''
      }
    },
    created() {
      const that = this
      that.$parent.isLogin = false
      init()
    },
    methods: {
      sendMsg() {
        const that = this
        if (that.msg) {
          ws.send(that.msg)
        }
      }
    }
  }

  var ws;

  function init() {
    // Connect to Web Socket
    ws = new WebSocket("ws://localhost:8012/");

    ws.onopen = function () {
      console.log("onopen");
    };

    ws.onmessage = function (e) {
      console.log("onmessage: " + e.data);
    };

    ws.onclose = function () {
      console.log("onclose");
    };

    ws.onerror = function (e) {
      console.log("onerror");
      console.log(e)
    };
  }
</script>

<style scoped>
  .footer {
    width: 100%;
    position: fixed;
    bottom: 0;
    left: 0;
    height: 50px;
    background-color: #ffffff;
  }

  .iconfont {
    width: 40px;
    color: #7d7e83;
    font-size: 30px;
    padding-right: 5px;
  }

  .chat {
    display: inline-block;
    vertical-align: middle;
    padding: 4px 0px;
    height: 100%;
  }

  .chat-txt {
    border-radius: 6px;
    overflow: hidden;
    padding: 0 10px;
    width: 100%;
    height: 32px;
    border: 1px solid #7d7e83;
  }
</style>
