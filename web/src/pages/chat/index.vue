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

  .chat-list .info {
    transition: .2s all linear;
  }
</style>
