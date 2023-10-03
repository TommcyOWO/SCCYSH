<template>
    <div class="h:80px flex jc:space-between ai:center bg:sky-60 color:white p:10px f:20 f:semibold">
        <IconMenu2 class="hide@>md mx:20px"/>
            <ul class="lt:none hide@<md flex ai:center mx:20px">
                <li class="cursor:pointer inline mx:20px shadow:0|2|white:hover ~300ms|ease-in"><NuxtLink to="/">首頁</NuxtLink></li>
                <li class="cursor:pointer inline mx:20px shadow:0|2|white:hover ~300ms|ease-in"><NuxtLink to="/extracurricular">課外活動</NuxtLink></li>
                <li class="cursor:pointer inline mx:20px shadow:0|2|white:hover ~300ms|ease-in"><NuxtLink to="/recommended_activities">推薦活動</NuxtLink></li>
                <li class="cursor:pointer inline mx:20px shadow:0|2|white:hover ~300ms|ease-in"><NuxtLink to="/connection">聯絡我們</NuxtLink></li>
            </ul>
            <div class="rel flex right:35px text:center">
                <a class="cursor:pointer mx:30px">wewae
                </a>
            </div>
    </div>
    <slot/>
</template>

<script setup>
import "@master/css";
import { IconMenu2 } from "@tabler/icons-vue"
useHead({
    title:"app"
})

</script>
<style scoped>

</style>