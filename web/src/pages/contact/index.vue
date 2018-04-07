<template>
  <div class="contact">
    <div class="weui_search_bar">
      <form class="weui_search_outer">
        <div class="weui_search_inner">
          <i class="weui_icon_search"></i>
          <input type="search" class="weui_search_input" placeholder="搜索" id="">
          <a href="javascript:" class="weui_icon_clear" style="display: none;"></a>
        </div>
        <label class="weui_search_text" for="">
          <i class="weui_icon_search"></i>
          <span>搜索</span>
        </label>
      </form>
    </div>
    <div class="contact-head weui_cells weui_cells_access">
      <a class="weui_cell" href="/contact/add">
        <div class="cell-hd"><img src="../../assets/images/contact_top_friend.png"></div>
        <div class="cell-hd weui_cell_primary"><p>新的朋友</p></div>
      </a>
      <a class="weui_cell" href="/contact/add">
        <div class="cell-hd"><img src="../../assets/images/contact_top_group.png"></div>
        <div class="cell-hd weui_cell_primary"><p>群聊</p></div>
      </a>
      <a class="weui_cell" href="/contact/add">
        <div class="cell-hd"><img src="../../assets/images/contact_top_tag.png"></div>
        <div class="cell-hd weui_cell_primary"><p>标签</p></div>
      </a>
      <a class="weui_cell" href="/contact/add">
        <div class="cell-hd"><img src="../../assets/images/contact_top_official.png"></div>
        <div class="cell-hd weui_cell_primary"><p>公众号</p></div>
      </a>
    </div>
    <div class="contact-friends">
      <div class="weui_cells weui_cells_access" v-for="item in friends">
        <div class="weui_cell" @click="$router.replace({path:`/chat/dialog/${item.user}`})">
          <div class="weui_cell_hd"><img src="../../assets/images/avatar.jpg"></div>
          <div class="weui_cell_bd weui_cell_primary"><p style="padding-left: 10px">{{item.name}}</p></div>
        </div>
      </div>
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
    data() {
      return {
        friends: []
      }
    },
    async created() {
      const that = this
      //获取好友列表
      const result = await that.$user.getFriends()
      if(result.result){
        that.friends = result.data
      }else{
        alert(result.msg)
      }
      that.$parent.showNav = true
    },
    methods: {

    }
  }
</script>

<style scoped>
  .contact {
    background: #f1f0f6;
    overflow: auto;
    height: 100%;
  }

  .contact-head {
    margin-top: 0;
  }

  .contact-head .weui_cell {
    padding: 9px 15px
  }

  .weui_cell .cell-hd {
    height: 36px;
    width: 36px;
    overflow: hidden;
    margin-right: 10px;
  }

  .cell-hd img {
    display: block;
    border: 0;
    width: 100%;
    height: 100%;
    object-fit: cover;
  }

  .contact-friends .weui_cells {
    margin-top: 10px;
  }

  .contact-friends .weui_cell_hd img {
    width: 35px;
    margin-right: 5px;
    display: block;
  }
</style>
