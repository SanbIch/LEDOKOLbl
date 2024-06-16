<script setup></script>
<script>
export default {
  data: () => ({
    tab: null
  })
}
</script>
<template>
  <v-tabs v-model="tab" align-tabs="center" color="deep-purple-accent-4" class="overflow-visible">
    <v-tab to="/map">Карта</v-tab>
    <v-tab to="/request">Заявки</v-tab>
    <v-tab to="/icebreakers">Ледоколы</v-tab>
    <v-tab to="/upload_ice">Загрузить льды</v-tab>
  </v-tabs>
</template>

<style lang="css" scoped></style>
