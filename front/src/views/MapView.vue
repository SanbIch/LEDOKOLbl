<script setup>
import PixelsMap from '@/components/PixelsMap.vue'
import TabMenu from '@/components/TabMenu.vue'
import axios from 'axios'
</script>
<script>
export default {
  data: () => ({
    check: ['ice'],
    checkboxes: null
  }),
  async beforeCreate() {
    this.checkboxes = (await axios.get(import.meta.env.VITE_BACK_URL + '/routes/')).data
  }
}
</script>

<template>
  <v-app>
    <v-app-bar>
      <v-container>
        <TabMenu />
      </v-container>
    </v-app-bar>

    <v-navigation-drawer location="right">
      <v-checkbox label="Льды" v-model="check" value="ice"></v-checkbox>
      <v-checkbox
        :label="`Маршрут ` + checkbox.id"
        v-model="check"
        :value="checkbox.id"
        v-for="checkbox in checkboxes"
        v-bind:key="checkbox.id"
      ></v-checkbox>
    </v-navigation-drawer>

    <v-main>
      <PixelsMap :layers="check" />
    </v-main>
  </v-app>
</template>

<style scoped></style>
