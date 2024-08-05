<template>
  <div class="create-image-form">
    <form @submit.prevent="handleSubmit">
        <label for="image">Выберите изображение:</label>
        <input type="file" id="image" @change="handleImageChange" />
        <div v-if="imageSrc" class="preview">
            <img :src="imageSrc" alt="Предварительный просмотр" />
        </div>
        <label for="description">Описание:</label>
        <input type="text" id="description" v-model="description" />
        <button type="submit">Создать</button>
    </form>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  props: {
    showForm: Boolean
  },
  data() {
    return {
      image: null,
      imageSrc: null,
      description: ''
    };
  },
  methods: {
    handleImageChange(event) {
      const file = event.target.files[0];
      if (file) {
        const reader = new FileReader();
        reader.onloadend = () => {
          this.imageSrc = reader.result;
          this.image = reader.result
        };
        reader.readAsDataURL(file);
      }
    },
    async handleSubmit() {
      try {
        const response = await axios.post('http://localhost/api/api-auth/images/', {
          description: this.description,
          image: this.image
        }, {
          headers: {
            'Content-Type': 'application/json'
          }
        });
        console.log('Image uploaded successfully:', response.data);

        this.imageSrc = null;
        this.description = '';
      } catch (error) {
        console.error('Error uploading image:', error);
      }
    }
  }
}
</script>

<style scoped>
.create-image-form {
  margin: 20px;
  padding: 20px;
  border: 1px solid #ddd;
  border-radius: 4px;
  background-color: #f9f9f9;
}
form {
  display: flex;
  flex-direction: column;
}
label {
  margin-top: 10px;
}
input[type="file"], input[type="text"] {
  margin-top: 5px;
  padding: 5px;
}
button {
  margin-top: 10px;
  padding: 10px;
  background-color: #007bff;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}
button:hover {
  background-color: #0056b3;
}
.preview {
  margin-top: 20px;
}
.preview img {
  max-width: 100%;
  height: auto;
  border: 1px solid #ddd;
  border-radius: 4px;
}
</style>
