// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  devtools: { enabled: true },
  css: [
    '@/assets/style.css',
    '@/assets/animation.css',
  ],
  modules: ['@nuxtjs/i18n','@vueuse/nuxt',
            // '@nuxtjs/algolia'
  ],
  app: {
    // pageTransition: {
      // name: 'Transition',
      // mode: 'out-in'
    // },
    head: {
      titleTemplate: 'CSG 歷程獵人',
      meta: [
        { charset: 'utf-8' },
        { name: 'viewport', content: 'width=device-width, initial-scale=1' },
        { name: 'description', content: 'Meta description' }
      ]
    },
    // algolia:{
      // apiKey: '5bb80baef05d10fd0476b8d33038445f',
      // applicationId: 'K6A25QQ0RF'
    // }
  }
})