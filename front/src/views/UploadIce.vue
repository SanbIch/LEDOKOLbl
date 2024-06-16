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

    <v-main
      ><v-file-input label="File input"></v-file-input>
      <v-btn to="/map">Отправить льды</v-btn></v-main
    >
  </v-app>
</template>

<style lang="scss" scoped></style>
