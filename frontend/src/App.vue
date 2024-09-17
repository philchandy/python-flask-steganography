<template>
  <div id="app" class="bg-app-background relative z-0 overflow-x-clip">
    <div class=" absolute flex flex-col min-h-screen inset-0 bg-grainImage opacity-35 -z-30"></div>
    <div class="flex flex-col min-h-screen">
      <div class="flex-grow">
        <HeroSection v-if="currentView === 'home'" @selectForm="handleFormSelection" />
        <HideText v-if="currentView === 'hideText'" @back="showHome" />
        <ExtractText v-if="currentView === 'extractText'" @back="showHome" />
      </div>
      <FooterSection />
    </div>
  </div>
</template>

<script>
import ExtractText from './components/ExtractText.vue';
import FooterSection from './components/FooterSection.vue';
import HeroSection from './components/HeroSection.vue';
import HideText from './components/HideText.vue';

export default {
  name: 'App',
  components: {
    HeroSection,
    ExtractText,
    HideText,
    FooterSection
  },
  data() {
    return {
      currentView:'home',
    };
  },
  methods: {
    handleFormSelection(formType) {
      console.log("form selected:", formType)
      this.currentView = formType
    },
    showHome(){
      this.currentView = 'home'
    },
  },
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
