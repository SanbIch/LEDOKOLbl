<script setup>
import TabMenu from '@/components/TabMenu.vue'
import GanttaDiag from '@/components/GanttaDiag.vue'
</script>

<template>
  <v-app>
    <v-app-bar>
      <v-container>
        <TabMenu />
      </v-container>
    </v-app-bar>

    <v-main>
      <GanttaDiag />
    </v-main>
  </v-app>
</template>

<style lang="scss" scoped></style>
