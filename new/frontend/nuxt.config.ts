// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  devtools: { enabled: true },
  modules:['@pinia/nuxt','@nuxtjs/i18n','@vueuse/nuxt'],
  i18n:{
    vueI18n:'./i18n/index.ts'
  },
  pinia: {
    storesDirs: ['./stores/**'],
  },
})
