<template>
  <div class="m:30px">
    <div class="flex jc:space-between ai:center">
      <h1>課外活動：</h1>
      <div class="flex rel ai:center bg:sky-76 r:10">
        <IconSearch color="white" class="m:5px|0px|5px|5px"/>
        <input class="mr:10px b:none outline:none r:3px" @input="fun_search" type="search">
      </div>
    </div>
    <div class="inline-block w:190px text:center float:right"> <!-- 將 div 的類名改為 flex jc:space-between ai:center -->
      <div v-if="hits.length" class="bg:sky-76 r:5px color:white"> <!-- 將 div 的類名改為 flex ai:center -->
        <ul class="list-style:none">
          <li class="p:10px" v-for="hit in hits" :key="hit.objectID">{{ hit.firstname }}</li> <!-- 將 hits.objectID 改為 hit.objectID -->
        </ul>
      </div>
    </div>
    <section>
    </section>
  </div>

</template>

<script setup>
import '@master/css'
import { IconSearch } from '@tabler/icons-vue';

const { result, search } = useAlgoliaSearch('CSG') // pass your index name as param
const hits = ref([])

const fun_search = async (v) => {
  await search({ query: v.target.value });
  hits.value = result.value.hits
}

</script>

<style scoped></style>