<template>
    <div class="h:80px flex jc:space-between ai:center bg:sky-60 color:white p:10px f:20 f:semibold">
        <IconMenu2 class="hide@>md mx:20px"/>
            <ul class="lt:none hide@<md flex ai:center mx:20px">
                <li class="cursor:pointer inline mx:20px">使用者頁面</li>
            </ul>
            <div class="rel flex right:35px text:center">
                <a class="cursor:pointer mx:30px">wewae
                </a>
            </div>
    </div>
</template>

<script setup>
import "@master/css";
import { IconMenu2 } from "@tabler/icons-vue"

</script>

<style scoped>

</style>