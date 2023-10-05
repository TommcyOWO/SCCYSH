<template>
  <div class="m:30px jc:center flex">
    <div class="text:center b:2|solid|sky-76 r:10px">
      <h1 class="mt:20">想推薦活動?</h1>
    <div class="flex jc:space-between font:semibold color:gray-60">
      <div class="flex:1">
        <div class="m:20px">
          <label class="block">主辦單位：</label> 
          <input class="" type="text">
        </div>
        <div class="m:20px">
          <label class="block">地點：</label>
          <input type="text">
        </div>
        <div class="m:20px">
          <label class="block">時間：</label> 
          <input type="text">
        </div>
        <div class="m:20px">
          <label class="block">費用：</label> 
          <input type="text">
        </div>  
      </div>
      <div class="flex:1">
        <div class="m:20px">
          <label class="block">活動內容：</label> 
          <input type="text">
        </div>
        <div class="m:20px">
          <label class="block">官網：</label> 
          <input type="text">
        </div>
        <div>
          <label class="block">連結：</label> 
          <input type="text">
        </div>
        <div class="m:20px">
          <label class="block">您的聯絡方式：</label>
          <input type="text"> 
        </div>
      </div>
    </div>
    <button class="btn">送出</button>
  </div>

  </div>
</template>

<script setup lang="ts">
import { init, Style } from '@master/css';

Style.extend('classes', {
  btn: 'inline-flex b:none center-content font:14 font:semibold font:white bg:sky-74 m:10px px:18 h:40 r:4',
})

init()

</script>

<style scoped>

</style>