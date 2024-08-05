<template>
  <header>
    <button @click="toggleForm">{{ showForm ? 'Закрыть форму' : 'Создать картинку' }}</button>
  </header>
</template>

<script>
export default {
  props: {
    showForm: Boolean
  },
  methods: {
    toggleForm() {
      this.$emit('toggle-form');
    }
  }
}
</script>

<style scoped>
header {
  display: flex;
  justify-content: space-between;
  padding: 20px;
  background-color: #f4f4f4;
  border-bottom: 1px solid #ddd;
}
button {
  padding: 10px 20px;
  border: none;
  background-color: #007bff;
  color: white;
  cursor: pointer;
  border-radius: 4px;
}
button:hover {
  background-color: #0056b3;
}
</style>
