// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  devtools: { enabled: true },
  modules: ["@nuxt/ui", "@nuxt/image", "@nuxtjs/google-fonts", "@pinia/nuxt"],
  runtimeConfig: {
    public: {
      flaskApiUrl: process.env.FLASK_API_URL,
    },
  },
  css: ["~/assets/scss/style.scss"],
});
