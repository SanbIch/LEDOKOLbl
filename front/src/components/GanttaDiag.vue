<template>
  <g-gantt-chart
    chart-start="2022-03-01 00:00"
    chart-end="2022-03-10 00:00"
    precision="day"
    bar-start="myBeginDate"
    bar-end="myEndDate"
  >
    <g-gantt-row
      v-for="icebreaker in icebreakers"
      v-bind:key="icebreaker.id"
      :label="icebreaker.name"
      :bars="rowBarList(icebreaker.id)"
    />
  </g-gantt-chart>
</template>

<script setup>
import axios from 'axios'

const icebreakers = (await axios.get(import.meta.env.VITE_BACK_URL + '/icebreakers/')).data

function rowBarList(aid) {
  return [
    {
      myBeginDate: '2022-03-05 13:00',
      myEndDate: '2022-03-07 19:00',
      ganttBarConfig: {
        // each bar must have a nested ganttBarConfig object ...
        id: 'unique-id' + aid, // ... and a unique "id" property
        label: 'Lorem ipsum dolor'
      }
    }
  ]
}
</script>
