<script setup>
import TabMenu from '@/components/TabMenu.vue'
import axios from 'axios'
</script>

<script>
const Responde = await axios.get(import.meta.env.VITE_BACK_URL + '/route_requests/')
const statuses = ['Новый', 'Построен', 'Пройден']
const colors = ['bg-white texxt-black', 'bg-green', 'bg-grey']

function formatDate(date) {
  let dd = date.getDate()
  if (dd < 10) dd = '0' + dd

  let mm = date.getMonth() + 1
  if (mm < 10) mm = '0' + mm

  let yyyy = date.getFullYear()

  return dd + '.' + mm + '.' + yyyy
}
</script>

<template>
  <v-app>
    <v-app-bar>
      <v-container>
        <TabMenu />
      </v-container>
    </v-app-bar>

    <v-main class="">
      <v-row dense class="pa-10">
        <v-col v-for="route_request in Responde.data" :key="route_request.id" cols="12" md="4">
          <v-card
            variant="outlined"
            v-bind:key="route_request.id"
            class="bg-indigo pa-3 rounded-xl"
            color="white"
          >
            <p class="rounded-pill d-inline pa-2" :class="colors[route_request.status]">
              {{ statuses[route_request.status] }}
            </p>
            <p>
              Начальная точка {{ route_request.starting_point }}, конечная точка
              {{ route_request.destination_point }}
            </p>
            <p>Корабль {{ route_request.ship_id }}</p>
            <p>
              Дата готовности к отправки
              {{ formatDate(new Date(Date.parse(route_request.starting_date))) }}
            </p>
            <v-card-actions>
              <v-btn to="/map" :disabled="route_request.status != 1" class="bg-green"
                >Открыть маршрут</v-btn
              >
            </v-card-actions>
          </v-card>
        </v-col>
      </v-row>
    </v-main>
  </v-app>
</template>

<style></style>
