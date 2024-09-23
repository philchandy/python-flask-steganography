<template>
  <div id="app" class="bg-gradient-to-b from-black via-[#200D42] via-34% via-[#4F21A1] via-65% to-[#A46EDB] to-82% relative z-0 overflow-x-clip">
    <div class=" absolute flex flex-col min-h-screen inset-0 bg-grainImage opacity-15 -z-30"></div>
    <div class="flex flex-col min-h-screen">
      <NavSection />
      <div class="flex flex-1">
        <router-view></router-view>
      </div>
      
      <FooterSection />
    </div>
  </div>
</template>

<script>
import FooterSection from './components/FooterSection.vue';
import NavSection from './components/NavSection.vue';

export default {
  name: 'App',
  components: {
    FooterSection,
    NavSection,
  },
  data() {},
  methods: {},
};
</script>

<style>
/* Set the background color for the whole app */
html, body, #app {
  color: white; /* Ensure the text is visible on the black background */
  height: 100%;
  margin: 0;
  padding: 0;
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
}

</style>
