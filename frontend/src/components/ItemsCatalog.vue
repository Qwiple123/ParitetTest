<template>
  <div class="catalog">
    <div v-for="image in images" :key="image.id" class="image-container">
      <img :src="image.image_url" :alt="image.description">
      <p class="description">{{ image.description }}</p>
      <button class="delete-button" @click="deleteImage(image.id)">Удалить</button>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
import Cookies from 'js-cookie';

axios.defaults.headers.common['X-CSRFToken'] = Cookies.get('csrftoken');

export default {
  data() {
    return {
      images: []
    }
  },
  created() {
    this.fetchImages();
  },
  methods: {
    async fetchImages() {
      try {
        const response = await axios.get('http://localhost/api/api-auth/images/');
        this.images = response.data;
      } catch (error) {
        console.error('Error fetching images:', error);
      }
    },
    async deleteImage(imageId) {
      try {
        await axios.delete(`http://localhost/api/api-auth/images/${imageId}/`);
        this.images = this.images.filter(image => image.id !== imageId);
      } catch (error) {
        console.error('Error deleting image:', error);
      }
    }
  }
}
</script>

<style scoped>
.catalog {
  display: flex;
  flex-wrap: wrap;
  justify-content: space-between;
  padding: 0 100px;
}

.image-container {
  display: flex;
  margin: 20px 0;
  flex-direction: column;
  align-items: center;
  border: 1px solid #ddd;
  border-radius: 8px;
  overflow: hidden;
  background-color: #fff;
  width: 49%;
  height: auto;
  box-sizing: border-box;
}

.description {
  margin: 8px;
    text-align: center;
    overflow: hidden;
    text-overflow: ellipsis;
    width: 300px;
    overflow-wrap: break-word;
}

img {
  width: 100%;
  height: auto;
  max-height: 300px;
  object-fit: contain;
  margin: 5px;
}

.delete-button {
  display: inline-block;
  margin-top: 10px;
  padding: 10px 20px;
  color: white;
  background-color: red;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  margin-bottom: 5px;
}
</style>