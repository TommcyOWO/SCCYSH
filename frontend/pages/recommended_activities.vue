<template>
    <div class="m:30px jc:center flex">
      <div class="text:center b:2|solid|sky-76 r:10px">
        <h1 class="mt:20">推薦活動</h1>
        <div class="flex jc:space-between font:semibold color:gray-60">
    <div class="flex:1">
      <div class="m:40px|20px">
        <label class="block m:0|20px">主辦單位：</label> 
        <input class="p:5px|5px outline:none shadow:0|2|blue-60:focus ~300ms|ease-in border:none" type="text">
      </div>
      <div class="m:40px|20px">
        <label class="block m:0|20px">縣市：</label>
        <input class="p:5px|5px outline:none shadow:0|2|blue-60:focus ~300ms|ease-in border:none" type="text">
      </div>
      <div class="m:40px|20px">
        <label class="block m:0|20px">地點：</label>
        <input class="p:5px|5px outline:none shadow:0|2|blue-60:focus ~300ms|ease-in border:none" type="text">
      </div>
    
    </div>


    <div class="flex:1">
      <div class="m:40px|20px">
        <label class="block m:0|20px">費用：</label> 
        <input class="p:5px|5px outline:none shadow:0|2|blue-60:focus ~300ms|ease-in border:none" type="text">
      </div>  
      <div class="m:40px|20px">
        <label class="block m:0|20px">對象：</label>
        <input class="p:5px|5px outline:none shadow:0|2|blue-60:focus ~300ms|ease-in border:none" type="text">
      </div>
    </div>
    <div class="flex:1">
      <div class="m:40px|20px">
        <label class="block m:0|20px">報名連結：</label> 
        <input class="p:5px|5px outline:none shadow:0|2|blue-60:focus ~300ms|ease-in border:none" type="text">
      </div>
      <div class="m:40px|20px">
        <label class="block m:0|20px">官網：</label> 
        <input class="p:5px|5px outline:none shadow:0|2|blue-60:focus ~300ms|ease-in border:none" type="text">
      </div>
      <div class="m:40px|20px">
        <label class="block m:0|20px">其他連結：</label> 
        <input class="p:5px|5px outline:none shadow:0|2|blue-60:focus ~300ms|ease-in border:none" type="text">
      </div>
    </div>
    <div class="flex:1">
      <div class="m:40px|20px">
        <label class="block m:0|20px">活動開始時間：</label> 
        <input class="p:5px|5px outline:none shadow:0|2|blue-60:focus ~300ms|ease-in border:none" type="text">
      </div>
      <div class="m:40px|20px">
        <label class="block m:0|20px">報名截止時間：</label> 
        <input class="p:5px|5px outline:none shadow:0|2|blue-60:focus ~300ms|ease-in border:none" type="text">
      </div>
      <div class="m:40px|20px">
        <label class="block m:0|20px">活動結束時間：</label> 
        <input class="p:5px|5px outline:none shadow:0|2|blue-60:focus ~300ms|ease-in border:none" type="text">
      </div>
    </div>
    <div class="flex:1">
      <div class="m:40px|20px">
        <label class="block m:0|20px">您的聯絡方式：</label>
        <input class="p:5px|5px outline:none shadow:0|2|blue-60:focus ~300ms|ease-in border:none" type="text"> 
      </div>
      <div class="m:40px|20px">
        <label class="block m:0|20px">活動內容：</label> 
        <input class="p:5px|5px outline:none shadow:0|2|blue-60:focus ~300ms|ease-in border:none" type="text">
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