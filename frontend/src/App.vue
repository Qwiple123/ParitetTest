<template>
  <AppHeader :showForm="showForm" @toggle-form="toggleForm" />
  <CreateImage v-if="showForm" :toggleForm="toggleForm" />
  <ItemsCatalog v-if="!showForm" />
</template>

<script>
import AppHeader from './components/AppHeader.vue'
import CreateImage from './components/CreateImage.vue'
import ItemsCatalog from './components/ItemsCatalog.vue'

export default {
  name: 'App',
  components: {
    AppHeader,
    ItemsCatalog,
    CreateImage
    
  },
  data() {
    return {
    showForm: false
    };
  },
  methods: {
    toggleForm() {
      this.showForm = !this.showForm;
    }
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

}
</style>
