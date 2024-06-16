<script setup>
import { RouterLink } from 'vue-router'
import MapView from './MapView.vue'
</script>
<script>
export default {
  data: () => ({
    tab: null
  })
}
</script>

<template>
  <!-- <header>
    <div class="wrapper">
      <nav>
        <RouterLink to="/map">Map</RouterLink>
        <RouterLink to="/request">Request</RouterLink>
        <v-btn variant="outlined"> Button </v-btn>
      </nav>
    </div>
  </header> -->
  <!-- <div class="d-flex flex-column h-screen">
    <v-tabs v-model="tab" align-tabs="center" color="deep-purple-accent-4">
      <v-tab :value="1">Льды</v-tab>
      <v-tab :value="2">Корабли</v-tab>
      <v-tab :value="3">Караваны</v-tab>
    </v-tabs>

    <v-tabs-window v-model="tab" class="h-100">
      <v-tabs-window-item v-for="n in 3" :key="n" :value="n">
        <MapView />
      </v-tabs-window-item>
    </v-tabs-window>
  </div> -->
  <div></div>
</template>

<style scoped>
.asd {
  position: relative;
}
</style>
