<template>
  <div class="cover">
    <div class="cell">
      <div class="pic" style="background-color: red"></div>
      <div class="card">
        <div class="remark">mask<span class="gender man"></span></div>
        <p class="wxid">微信号：xiap</p>
        <p class="nickname">昵称：狗蛋</p>
      </div>
    </div>
    <div class="cell">
      <p>设置备注和标签</p>
    </div>
    <div class="cell other">
      <div>
        <span class="first">地区</span>
        <span class="second">广东 光子</span>
      </div>
      <div>
        <span class="first">个性签名</span>
        <span class="second">前进骑兵连</span>
      </div>
    </div>
    <div class="add">
      <a @click="addFriend">添加到通讯录</a>
    </div>
  </div>
</template>
<script>
  import {mapModules, mapRules} from 'vuet'

  export default {
    mixins: [
      mapModules({
        user: 'user'
      }),
      mapRules({
        manual: 'user'
      })
    ],
    methods: {
      async addFriend() {
        const that = this;
        const data = await that.$user.addFriend(2);
        if (data.result) {
          that.$router.replace('/')
        } else {
          alert('添加好友失败')
        }
      },
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

  .cell {
    margin-top: 15px;
    padding: 10px 15px;
    position: relative;
    display: -webkit-box;
    display: -webkit-flex;
    display: flex;
    -webkit-box-align: center;
    -webkit-align-items: center;
    align-items: center;
    background-color: #fff;
  }

  .pic {
    width: 55px;
    height: 55px;
    border-radius: 6px;
    margin-right: 10px;
    background-repeat: no-repeat;
    background-size: cover;
  }

  .remark {
    font-size: 18px;
    color: #4f4f4f;
  }

  .gender {
    display: inline-block;
    width: 20px;
    height: 20px;
    vertical-align: middle;
    margin-left: 4px;
    margin-top: -2px;
  }

  .gender.man {
    background-image: url(../../assets/images/contact_male.png);
    background-repeat: no-repeat;
    background-size: contain;
    background-position: center center;
  }

  .card p {
    font-size: 14px;
    color: #888888;
  }

  .other {
    display: block;
  }

  .other div {
    width: 100%;
    padding: 10px 0;
    border-bottom: 1px solid #f3f0f0;
  }

  .other .first {
    display: inline-block;
    width: 68px;
    margin-right: 20px;
  }

  .other .second {
    color: #888888;
  }

  .add {
    margin: 20px auto;
    width: 92%;
    height: 40px;
    background-color: #0bb908;
    color: #fff;
    line-height: 40px;
    text-align: center;
  }
</style>
