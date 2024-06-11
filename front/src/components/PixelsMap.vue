<template>
  <div id="container">
      <div id="map" ref="map"></div>
      <canvas id="deck-canvas"></canvas>
  </div>
</template>

<script>
  import {GridLayer} from '@deck.gl/aggregation-layers';
  import mapboxgl from 'mapbox-gl';
  import {MapboxOverlay as DeckOverlay} from '@deck.gl/mapbox';
  import MapboxLanguage from '@mapbox/mapbox-gl-language';

  const layer = new GridLayer({
      id: 'GridLayer',
      data: 'https://raw.githubusercontent.com/visgl/deck.gl-data/master/website/sf-bike-parking.json',

      extruded: true,
      getPosition: d => d.COORDINATES,
      getColorWeight: d => d.SPACES,
      getElevationWeight: d => d.SPACES,
      elevationScale: 4,
      cellSize: 200,
      pickable: true
  });

export default {
  components: {},
  mounted() {

      const MAPBOX_TOKEN = 'pk.eyJ1IjoidGFiYnQiLCJhIjoiY2xwbHNhM251MDNjaTJ0cXlhN3N3dmpuaSJ9.GSLMLyUNHpGetm0TCjaMLg' //import.meta.env.VUE_APP_MAPBOX_TOKEN;
      
      // Стили:
      // 'mapbox://styles/mapbox/light-v9' - светлый бледный
      // 'mapbox://styles/mapbox/dark-v11' - темный

      const map = new mapboxgl.Map({
          container: 'map',
          style: 'mapbox://styles/mapbox/dark-v11',
          accessToken: MAPBOX_TOKEN,
          center: [-482.429066, 37.750222],
          zoom: 12,
          bearing: 0,
          pitch: 30
      });

      const language = new MapboxLanguage();
      map.addControl(language);

      const deckOverlay = new DeckOverlay({
      layers: [
          new GridLayer({
              id: 'GridLayer',
              data: 'https://raw.githubusercontent.com/visgl/deck.gl-data/master/website/sf-bike-parking.json',

              extruded: true,
              opacity: 0.2,
              getPosition: d => d.COORDINATES,
              getColorWeight: d => d.SPACES,
              getElevationWeight: d => d.SPACES,
              colorAggregation: 'MEAN',
              colorScaleType: 'quantile',  //'quantize', 'linear', 'quantile', 'ordinal'
              elevationRange: [
                  0,
                  3000
              ],
              elevationScale: 0.001,
              cellSize: 200,
              pickable: true,
              colorRange: [[255,255,178],[254,217,118],[254,178,76],[253,141,60],[240,59,32],[189,0,38]],
          })
      ]
      });

      map.addControl(deckOverlay);
      map.addControl(new mapboxgl.NavigationControl());
  }
}
</script>

<style>
  body {
      margin: 0;
      padding: 0;
      font-family: UberMove, Helvetica, Arial, sans-serif;
  }
  #map {
    position: fixed;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
  }
</style>
