<template>
  <div class="m:30px f:semibold">
    <section class="my:20px">
        <h1>我們是誰：</h1>
          <p class="f:20 w:600px color:gray mt:10px">
            CSG 全名為 CYSH Study Group，即嘉義高中讀書會。
            身為一群志向遠大的高中生，我們不想僅僅透過辦讀書會讓大家受惠
            因此我們創了 CSG 歷程獵人
            透過彙整、媒合國高中生能參加的課外活動
            充實你的學習歷程
            創造一個難忘的高中生活!
          </p>
    </section>
    <section class="my:20px">
      <h1>為什麼您需要我們?</h1>
      <ul class="inline-block list-style:none text:left mt:10px bt:2|solid|gray-86">
        <li class="my:10px flex"><IconCircleCheck color='gray'/>我們的「獵人」會幫你彙整全台的課外活動，包括競賽、營隊、志工機會等。</li>
        <li class="my:10px flex"><IconCircleCheck color='gray'/>各活動的地點、報名連結、報名截止日期等都會告訴你。</li>
        <li class="my:10px flex"><IconCircleCheck color='gray'/>快速搜尋到適合你的活動，充實學習歷程!。</li>
      </ul>
    </section>
    <section class="my:20px w:600px">
        <h1>和我們互動~</h1>
          <p class="inline-block f:20 color:gray mt:10px">
            我們有一個 Discord 伺服器，除了不定期辦適合大眾的線上讀書會外，
            也有一個溫暖的社群 (至少目前如此)
            快點來吧!
            </p>
            <div class="inline-block">
              <a target="_blank" href="https://bit.ly/45Y9AIX" class="f:18 text:center flex color:gray-60 shadow:0|2|gray-60:hover ~300ms|ease-in"><IconBrandDiscordFilled/> Discord</a>
            </div>
    </section>
    <section>
      <h1>目前職位有：</h1>
      <ul class="list-style:none inline-block mt:10px bt:2|solid|gray-86">
        <li class="my:10px flex color:gray"><IconFocus2 color="gray"/>獵人：協助尋找課外活動與競賽</li>
        <li class="my:10px flex color:gray"><IconBrandInstagram color="gray"/>公關：經營 IG、處理電子郵件等</li>
        <li class="my:10px flex color:gray"><IconSettings2 color="gray"/>工程師：負責維護網頁與資料庫</li>
      </ul>
    </section>
  </div>
</template>

<script setup>
import '@master/css'
import { IconCircleCheck,IconBrandDiscordFilled, IconFocus2, IconBrandInstagram, IconSettings2 } from '@tabler/icons-vue';

</script>

<style scoped></style>