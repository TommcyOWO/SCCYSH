<template>
  <div class="mx:60px my:30px f:medium">
    <section class="my:60px">
        <h1 class="f:40">充實歷程，成就青春</h1>
          <p class="my:20px color:gray">我們是 CSG 歷程獵人，負責幫你找競賽、營隊、志工等課外活動<br>充實你的學習歷程，為高中生活留下滿滿回憶!</p>
        <div class="inline-block">
          <a class="btn m:10px" target="_blank" href="https://www.instagram.com/studygroup_cysh/"><IconBrandInstagram class="mr:3px"/>查看IG粉絲專業</a>
          <a class="btn m:10px" target="_blank" href="https://bit.ly/45Y9AIX"><IconBrandDiscordFilled class="mr:3px"/>加入我們Discord</a>
          <a class="btn m:10px" target="_blank" href="https://bit.ly/48D54C2"><IconPlus/>加入我們!!</a>
        </div>
    </section>
    <section class="my:60px w:200px@<md w:400@>md">
        <h1>我們是誰：</h1>
        <p class="f:20 color:gray mt:10px">
          CSG 全名為 CYSH Study Group，即嘉義高中讀書會。
          身為一群志向遠大的高中生，我們不想僅僅透過辦讀書會讓大家受惠
          因此我們創了 CSG 歷程獵人
          透過彙整、媒合國高中生能參加的課外活動
          充實你的學習歷程
          創造一個難忘的高中生活!
        </p>
    </section>
    <section class="my:40px">
    <ul ref="imgList" class="list-style:none flex-wrap:nowrap flex overflow:hidden">
      <li :class="`overflow:hidden flex:0|0|auto ~300ms|ease-in translateX(${transfroms}%)`" v-for="img in imgs" :key="img">
        <img :src="img" class="h:100vh">
      </li>
    </ul>

      <div class="flex jc:center bottom:100px rel">
        <IconArrowBadgeLeft @click="changp_func('next_')" height="40px" width="40px" color="white" class="m:20px cursor:pointer shadow:0|3|white:hover ~300ms|ease-in"/>
        <IconArrowBadgeRight @click="changp_func('pre')" height="40px" width="40px" color="white" class="m:20px cursor:pointer shadow:0|3|white:hover ~300ms|ease-in"/>
      </div>
    </section>
    <section class="my:60px">
      <h1>為什麼您需要我們?</h1>
      <ul class="block list-style:none text:left mt:10px bt:2|solid|gray-86">
        <li class="my:10px flex"><IconCircleCheck color='gray'/>我們的「獵人」會幫你彙整全台的課外活動，包括競賽、營隊、志工機會等。</li>
        <li class="my:10px flex"><IconCircleCheck color='gray'/>各活動的地點、報名連結、報名截止日期等都會告訴你。</li>
        <li class="my:10px flex"><IconCircleCheck color='gray'/>快速搜尋到適合你的活動，充實學習歷程!。</li>
      </ul>
    </section>
    <section class="my:60px w:200px@<md w:400@>md">
        <h1>和我們互動~</h1>
          <p class="inline-block f:20 color:gray mt:10px">
            我們有一個 Discord 伺服器，除了不定期辦適合大眾的線上讀書會外，
            也有一個溫暖的社群 (至少目前如此)
            快點來吧!
            </p>
            <div class="block">
              <a target="_blank" href="https://bit.ly/45Y9AIX" class="f:18 text:center flex color:gray-60 shadow:0|2|gray-60:hover ~300ms|ease-in"><IconBrandDiscordFilled/> Discord</a>
            </div>
    </section>
    <section>
      <h1>目前職位有：</h1>
      <ul class="list-style:none inline-block mt:10px bt:2|solid|gray-86">
        <li class="my:10px flex color:gray"><IconFocus2 color="gray"/>獵人：協助尋找課外活動與競賽。</li>
        <li class="my:10px flex color:gray"><IconBrandInstagram color="gray"/>公關：經營 IG、處理電子郵件等。</li>
        <li class="my:10px flex color:gray"><IconSettings2 color="gray"/>工程師：負責維護網頁與資料庫。</li>
        <a class="btn mt:20px flex" target="_blank" href="https://bit.ly/48D54C2"><IconPlus/>加入我們!!</a>
      </ul>
    </section>
    <div class="w:100% h:20px text:center"><a target="_blank" href="https://github.com/TommcyOWO" class="flex jc:center color:gray"><IconBadgeCc/> Dev by Tomycat</a></div>
  </div>
</template>

<script setup lang="ts">
import { init, Style } from '@master/css';
import { IconCircleCheck,IconBrandDiscordFilled , IconPlus, IconBadgeCc, IconFocus2, IconBrandInstagram, IconSettings2, IconArrowBadgeRight, IconArrowBadgeLeft } from '@tabler/icons-vue';

Style.extend('classes', {
  btn: 'inline-flex b:none center-content font:14 font:semibold font:white bg:sky-74 px:18 h:40 r:4',
})

init()

const imgs = ref(['1.png', '2.png', '3.png', '4.png', '5.png'])

const transfroms = ref(0)

const changp_func = (type:string) => {
  if (type === 'next_') {
    transfroms.value += 100
  } else {
    transfroms.value -= 100
  }
}

watch(transfroms,(newVal,oldVal)=>{
  if (newVal > 0 || newVal <-400){
    transfroms.value = 0
  }
})

</script>

<style scoped></style>