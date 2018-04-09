<template>
  <div style="background-color: #efeff4;height: 100%;overflow: auto">
    <ul class="dialog">
      <li v-for="item in tempMsgs" :class="{'right':item.send}">
        <div class="other">
          <div class="time">{{item.time}}</div>
          <img class="avatar" src="../../assets/images/avatar.jpg">
          <div class="whatsay">{{item.msg}}</div>
        </div>
      </li>
    </ul>
    <div class="footer">
      <span class="iconfont icon-dialogue-voice"></span>
      <div class="chat">
        <input class="chat-txt" v-on:keyup.13="sendMsg" v-model="msg"/>
      </div>
      <a title="点击发送" class="btn-send" @click="sendMsg">发送</a>
    </div>
  </div>
</template>

<script>
  export default {
    data() {
      return {
        friend: 0,
        msg: '',
        tempMsgs: []
      }
    },
    created() {
      const that = this
      that.$parent.showNav = false
      that.friend = that.$route.params.friend
      let t = that.$parent.chatList.find(i => i.id == that.friend)
      if (t != null) {//读取未读消息
        that.tempMsgs = t.tempMsgs
        t.count = 0
      }
    },
    beforeDestroy() {
      const that = this
      let t = that.$parent.chatList.find(i => i.id == that.friend)
      //缓存聊天记录
      if (t == null) {
        that.$parent.chatList.push({id: that.friend, tempMsgs: that.tempMsgs, count: 0})
      } else {
        t.tempMsgs = that.tempMsgs
      }
    },
    methods: {
      sendMsg() {
        const that = this
        if (that.msg) {
          const time = new Date().format('yyyy-MM-dd hh:mm:ss')
          that.$parent.sendData(that.friend, that.msg, false, time)
          that.tempMsgs.push({send: true, time: time, msg: that.msg})
          that.msg = ''
        }
      },
      receMsg(msg, time) {
        this.tempMsgs.push({send: false, time: time, msg: msg})
      }
    }
  }
</script>

<style scoped>
  .dialog {
    height: 100%;
    padding: 0 10px 10px 10px;
  }

  .dialog li {
    margin-bottom: 10px;
  }

  .dialog .other .avatar {
    width: 40px;
    height: 40px;
    float: left;
  }

  .dialog .other .time {
    font-size: 12px;
    color: #999;
    text-align: center;
    width: 100%;
    margin-top: 5px;
  }

  .dialog .whatsay {
    display: inline-block;
    height: 40px;
    max-width: 80%;
    margin-left: 10px;
    background: #fff;
    padding: 10px;
    border: 1px solid #d9d9d9;
    border-radius: 8px;
    font-size: 14px;
    color: #333;
    word-break: break-all;
  }

  .dialog .right {
    text-align: right;
  }

  .dialog .right .other .avatar {
    width: 40px;
    height: 40px;
    float: right;
  }

  .dialog .right .whatsay {
    display: inline-block;
    height: 40px;
    max-width: 80%;
    margin-right: 10px;
    background: #9fe658;
    padding: 10px;
    border: 1px solid #d9d9d9;
    border-radius: 8px;
    font-size: 14px;
    color: #333;
    word-break: break-all;
  }

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
    width: 70%;
  }

  .chat-txt {
    border-radius: 6px;
    overflow: hidden;
    padding: 0 10px;
    width: 100%;
    height: 32px;
    border: 1px solid #7d7e83;
  }

  .btn-send {
    margin-bottom: 10px;
    margin-left: 10px;
    vertical-align: middle;
    height: 30px;
    line-height: 30px;
    width: 50px;
    padding-left: 0;
    padding-right: 0;
    background-color: #44b549;
    color: #fff;
    display: inline-block;
    text-decoration: none;
    text-align: center;
    border-color: #44b549;
  }
</style>
