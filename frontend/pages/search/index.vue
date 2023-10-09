<template>
  <div class="m:30px">
    <div class="flex jc:space-between ai:center">
      <h1>課外活動：</h1>
      <div class="flex rel ai:center bg:sky-76 r:10">
        <IconSearch color="white" class="m:5px|0px|5px|5px cursor:pointer"/>
        <input v-model="search_input" class="mr:10px b:none outline:none r:3px" @input="fun_search" type="text">
      </div>
    </div>
    {{ result }}
  </div>
</template>

<script setup lang="ts">
import '@master/css'
import { IconSearch } from '@tabler/icons-vue';

const { result, search } = useAlgoliaSearch('CSG') // pass your index name as param

const search_input = ref('')

const search_key = useMagicKeys()['Enter']

const fun_search = async () => {
  await search({ query: search_input.value });
}

</script>

<style scoped></style>