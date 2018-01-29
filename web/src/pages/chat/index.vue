<template>
  <ul class="chat-list">
    <li>
      <div class="info">
        <div class="ico"></div>
        <div class="summary"></div>
      </div>
    </li>
  </ul>
</template>

<script>
  export default {}
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
  .chat-list .ico{
    position: relative;
    float: left;
    width: 48px;
    height: 48px;
    margin-right: 10px;
  }
</style>
