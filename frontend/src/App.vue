<template>
  <div id="app">
    <h1>Steganography App</h1>
    <HideText />
    <ExtractText />
  </div>
</template>

<script>
import ExtractText from './components/ExtractText.vue';
import HideText from './components/HideText.vue';

export default {
  name: 'App',
  components: {
    ExtractText,
    HideText
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
