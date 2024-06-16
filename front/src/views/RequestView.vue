<template>
  <v-app>
    <v-app-bar>
      <v-container>
        <TabMenu />
      </v-container>
    </v-app-bar>

    <v-main class="">
      <v-row dense class="pa-10">
        <v-col v-for="route_request in requests" :key="route_request.id" cols="12" md="4">
          <v-card
            variant="outlined"
            v-bind:key="route_request.id"
            class="pa-3 rounded-xl"
            color="white"
            style="background-color: #23224E;"
          >
            <p class="rounded-pill d-inline pa-2" style="background-color: #5A58BB88;">
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
              <v-btn to="/map" :disabled="route_request.status != 1" style="background-color: #5A58BB;"
                >Открыть маршрут</v-btn
              >
            </v-card-actions>
          </v-card>
        </v-col>
      </v-row>
    </v-main>
  </v-app>
</template>

  <script>
  import axios from 'axios';
  import TabMenu from '@/components/TabMenu.vue'

  export default {
    components: {TabMenu},
    data() {
      return {
        requests: [], 
        statuses: ['Новый', 'Построен', 'Пройден'],
      };
    },
    mounted() {
      this.fetchItems();
    },
    methods: {
      fetchItems() {
        axios.get(import.meta.env.VITE_BACK_URL + '/route_requests/') // Replace with your API endpoint
          .then(response => {
            this.requests = response.data;
          })
          .catch(error => {
            console.error('Error fetching requests', error);
          });
      },
      formatDate(date) {
        let dd = date.getDate()
        if (dd < 10) dd = '0' + dd

        let mm = date.getMonth() + 1
        if (mm < 10) mm = '0' + mm

        let yyyy = date.getFullYear()

        return dd + '.' + mm + '.' + yyyy
      }
    }
  };
  </script>
  