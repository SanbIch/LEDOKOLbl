<template>
  <div id="map" ref="map"></div>
</template>

<script setup>
import { onMounted, watch } from 'vue'
const props = defineProps(['layers'])

async function GenerateRouteLayers() {
  let routes = (await axios.get(import.meta.env.VITE_BACK_URL + '/routes/')).data
  let layers = [
    new HeatmapLayer({
      id: 'HeatmapLayer',
      data: import.meta.env.VITE_BACK_URL + '/ice_data',

      visible: props.layers.includes('ice'),
      getPosition: (d) => d.COORDINATES,
      getWeight: (d) => d.ICE,
      colorRange: [
        [239, 243, 255],
        [198, 219, 239],
        [158, 202, 225],
        [107, 174, 214],
        [49, 130, 189],
        [8, 81, 156]
      ]
    })
  ]
  for (let route of routes) {
    console.log(route)
    layers.push(
      new PathLayer({
        id: 'Path' + route.id,
        data: import.meta.env.VITE_BACK_URL + '/routes/' + route.id,

        visible: props.layers.includes(route.id),
        getColor: (d) => {
          const hex = d.color
          // convert to RGB
          return hex.match(/[0-9a-f]{2}/g).map((x) => parseInt(x, 16))
        },
        getPath: (d) => d.path,
        widthScale: 300,
        getWidth: 100,
        pickable: true
      })
    )
  }
  return layers
}

onMounted(async () => {
  const MAPBOX_TOKEN =
    'pk.eyJ1IjoidGFiYnQiLCJhIjoiY2xwbHNhM251MDNjaTJ0cXlhN3N3dmpuaSJ9.GSLMLyUNHpGetm0TCjaMLg' //import.meta.env.VUE_APP_MAPBOX_TOKEN;

  // Стили:
  // 'mapbox://styles/mapbox/light-v9' - светлый бледный
  // 'mapbox://styles/mapbox/dark-v11' - темный

  const map = new mapboxgl.Map({
    container: 'map',
    projection: 'mercator',
    style: 'mapbox://styles/mapbox/dark-v11',
    accessToken: MAPBOX_TOKEN,
    center: [103.762016, 77.561587],
    zoom: 3.5
  })

  const language = new MapboxLanguage()
  map.addControl(language)

  let deckOverlay = new DeckOverlay({
    layers: await GenerateRouteLayers()
  })

  map.addControl(deckOverlay)
  map.addControl(new mapboxgl.NavigationControl())

  watch(props, async () => {
    deckOverlay.setProps({
      layers: await GenerateRouteLayers()
    })
  })
})
</script>
<script>
import { HeatmapLayer } from '@deck.gl/aggregation-layers'
import { PathLayer } from '@deck.gl/layers'
import mapboxgl from 'mapbox-gl'
import 'mapbox-gl/dist/mapbox-gl.css'
import { MapboxOverlay as DeckOverlay } from '@deck.gl/mapbox'
import MapboxLanguage from '@mapbox/mapbox-gl-language'
import axios from 'axios'

export default {
  components: {},
  mounted() {}
}
</script>

<style>
#map {
  width: 100%;
  height: 100%;
}
</style>
