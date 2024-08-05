<template>
  <div id="app">
    <ItemsCatalog />
  </div>
</template>

<script>
import ItemsCatalog from './ItemsCatalog.vue'

export default {
  name: 'HomePage',
  components: {
    ItemsCatalog
  }
}
</script>

<style>
body {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}
#app {
  display: flex;
  justify-content: center;
  align-items: center;
  min-height: 100vh;
}
</style>

