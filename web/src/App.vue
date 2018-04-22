<template>
  <div id="app">
    <!-- 头部 -->
    <div class="header" v-show="load">
      <v-header></v-header>
    </div>
    <!-- 主体 -->
    <div class="content" v-show="load">
      <router-view></router-view>
    </div>
    <!-- di bu导航 -->
    <div class="footer" v-show="load && showNav">
      <v-footer></v-footer>
    </div>
    <!-- 欢迎页 -->
    <div class="welcome" v-show="welcome" transition="welcome"></div>
    <!--    <div class="mobile-tips" style="dislay:none;" v-show="isnotMobile">
          <div class="mobile-tips-inner">
            <div class="mobile-model"><img src="./assets/images/mobile.png" alt=""></div>
            <p><br>为保证最佳用户体验,<br></p>
            <p class="_align-left">1.请用chrome移动设备调试模式(F12)下打开</p>
            <p class="_align-left">2.手机浏览器访问</p>
            <br>
            <button class="weui_btn weui_btn_mini weui_btn_primary" v-touch:tap='isnotMobile = false'>关闭</button>
          </div>
        </div>-->
  </div>
</template>

<script>
  export default {
    data() {
      return {
        load: false,//加载
        navIndex: 1,
        showNav: true,
        welcome: true,
        chatList: []//聊天记录缓存
      }
    },
    created() {
      const that = this
      setTimeout(() => {
        that.welcome = false
      }, 2000)
      that.load = true
      websocketInit()
      ws.onmessage = that.recevData
      //获取历史未读聊天记录
    },
    methods: {
      sendData(fid, msg, group, time) {
        ws.send(JSON.stringify({
          socket_uid: sessionStorage.getItem('weixin'),
          socket_fid: fid,
          socket_isGroup: group,
          socket_msg: msg,
          socket_time: time
        }))
      },
      recevData(e) {
        const that = this
        const data = JSON.parse(e.data)
        const currFriend = that.$children[1].friend
        if (data.socket_uid == currFriend) {//当前正和该好友聊天
          that.$children[1].receMsg(data.socket_msg, data.socket_time)
        } else {
          let t = that.chatList.find(i => i.id == data.socket_uid)
          if (t == null) {
            let tempMsgs = []
            tempMsgs.push({send: false, time: data.socket_time, msg: data.socket_msg})
            that.chatList.push({id: data.socket_uid, tempMsgs: tempMsgs, count: 1})
          } else {
            t.tempMsgs.push({send: false, time: data.socket_time, msg: data.socket_msg})
            t.count += 1
          }
        }
        console.log(that.chatList)
        //console.log("onmessage: " + e.data);
      }
    }
  }

  var ws;

  function websocketInit() {
    if (!ws) {
      // Connect to Web Socket
      ws = new WebSocket("ws://localhost:8012/");

      ws.onopen = function () {
        console.log("onopen");
      };

      ws.onclose = function () {
        console.log("onclose");
      };

      ws.onerror = function (e) {
        console.log("onerror");
        console.log(e)
      };
    }
  }
</script>
<style>
  @import "./assets/css/base.css";
  @import "./assets/css/iconfont.css";
  @import "./assets/css/weui.min.css";
</style>
<style scoped>
  .header {
    position: absolute;
    left: 0;
    top: 0;
    width: 100%;
    z-index: 3;
    height: 45px;
    line-height: 45px;
    font-size: 19px;
    background: linear-gradient(to bottom, #303036, #3c3b40);
    color: #ffffff;
    text-align: center;
  }

  .content {
    padding-top: 45px;
    padding-bottom: 50px;
    overflow: hidden;
    position: relative;
    height: 100%;
  }

  .content ._full_inner {
    z-index: 2;
  }

  .footer {
    bottom: 0;
    left: 0;
    width: 100%;
    position: absolute;
    z-index: 3;
  }

  .welcome {
    width: 100%;
    height: 100%;
    z-index: 1000;
    position: fixed;
    left: 0;
    top: 0;
    transition: .25s all linear;
    background: url(./assets/images/start.png) no-repeat center center;
    background-size: cover;
  }

  .welcome-leave {
    opacity: 0;
  }
</style>
