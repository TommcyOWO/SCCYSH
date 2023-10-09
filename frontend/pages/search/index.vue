<template>
  <div class="m:30px">
    <h1>課外活動：</h1>
    {{ result }}
    <div>
    </div>
  </div>
</template>

<script setup>
import '@master/css'
const { result, search } = useAlgoliaSearch('CSG') // pass your index name as param
onMounted(async () => {
  await search({ query: 'Samsung' });
})
</script>

<style scoped></style>