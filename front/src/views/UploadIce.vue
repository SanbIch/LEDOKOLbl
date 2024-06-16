<script setup>
import TabMenu from '@/components/TabMenu.vue'
</script>

<template>
  <v-app>
    <v-app-bar>
      <v-container>
        <TabMenu />
      </v-container>
    </v-app-bar>

    <v-main >
        <v-file-input @change="handleFileUpload" label="Выберите XLSX файл с толщиной льдов..."></v-file-input>
        <v-btn v-if="!loading" @click="uploadFile">Отправить льды</v-btn>
        <div v-if="loading">Файл загружается...</div>
    </v-main>
  </v-app>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      loading: false,
      file: null
    };
  },

  methods: {
    handleFileUpload(event) {
      this.file = event.target.files[0];
    },
    async uploadFile() {
      this.loading = true;

      let formData = new FormData();
      formData.append('file', this.file);

      try {
        await axios.post(import.meta.env.VITE_BACK_URL + '/ice/', formData, {
          headers: {
            'Content-Type': 'multipart/form-data'
          }
        });
        alert('Прогноз льдов успешно обновлен!');
      } catch (error) {
        console.error(error);
        alert('Ошибка при загрузке файла');
      } finally {
        this.loading = false;
      }
    }
  }
};
</script>

<style lang="scss" scoped></style>