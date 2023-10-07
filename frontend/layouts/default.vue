<template>
    <div class="h:80px flex jc:space-between ai:center color:sky-74 p:10px f:20 f:semibold">
        <IconMenu2 @click="menu()" class="hide@>md mx:20px cursor:pointer"/>
            <ul class="lt:none hide@<md flex ai:center mx:20px">
                <li @click="moveTo('index')" class="cursor:pointer inline mx:20px shadow:0|2|sky-80:hover ~300ms|ease-in">首頁</li>
                <li @click="moveTo('extracurricular')" class="cursor:pointer inline mx:20px shadow:0|2|sky-80:hover ~300ms|ease-in">課外活動</li>
                <li @click="moveTo('recommended_activities')" class="cursor:pointer inline mx:20px shadow:0|2|sky-80:hover ~300ms|ease-in">推薦活動</li>
                <li @click="moveTo('connection')" class="cursor:pointer inline mx:20px shadow:0|2|sky-80:hover ~300ms|ease-in">聯絡我們</li>
            </ul>
        </div>
        <ul v-if="menuv" class="mx:20px hide@>md color:sky-74 f:20 f:semibold ">
            <li @click="moveTo('index')" class="cursor:pointer block m:20px|30px">首頁</li>
            <li @click="moveTo('extracurricular')" class="cursor:pointer block m:20px|30px">課外活動</li>
            <li @click="moveTo('recommended_activities')" class="cursor:pointer block m:20px|30px">推薦活動</li>
            <li @click="moveTo('connection')" class="cursor:pointer block m:20px|30px">聯絡我們</li>
        </ul>
        <div> {{ result }} </div>
    <slot/>
</template>

<script setup lang="ts">
import "@master/css";
import { IconMenu2 } from "@tabler/icons-vue"

const [menuv , menu] = useToggle()

const router = useRouter()
const moveTo = (path:string) => router.push({ name: path })

const { result, search } = useAlgoliaSearch('CSG') // pass your index name as param
await search({ query: 'John' });
</script>
<style scoped>

</style>