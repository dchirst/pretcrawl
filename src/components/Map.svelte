<script lang="ts">
    // @ts-ignore
    import * as L from 'leaflet';
    // If you're playing with this in the Svelte REPL, import the CSS using the
    // syntax in svelte:head instead. For normal development, this is better.
    import 'leaflet/dist/leaflet.css';
    export let apiKey: string;
    
    let map: L.Map;

    // Map Config
    const map_style = "Light_3857";
    const attribution =
    "Contains OS data &copy Crown copyright and database rights 2022";
    const datahubEndpoint = `https://api.os.uk/maps/raster/v1/zxy/${map_style}/{z}/{x}/{y}.png?key=${apiKey}`;

  
    function createMap(container) {
      let m = L.map(container).setView([51.505, -0.09], 13);
      L.tileLayer(
        datahubEndpoint,
      {
          attribution: attribution,
        }
      ).addTo(m);
  
      return m;
    }
  
    function mapAction(container) {
      map = createMap(container);
      return {
        destroy: () => {
          map.remove();
        },
      };
    }
  </script>
  
  <svelte:head>
     <!-- In the REPL you need to do this. In a normal Svelte app, use a CSS Rollup plugin and import it from the leaflet package. -->
     <link rel="stylesheet" href="https://unpkg.com/leaflet@1.6.0/dist/leaflet.css"
     integrity="sha512-xwE/Az9zrjBIphAcBb3F6JVqxf46+CDLwfLMHloNu6KEQCAWi6HcDUbeOfBIptF7tcCzusKFjFw2yuvEpDL9wQ=="
     crossorigin=""/>
  </svelte:head>
  
  <div use:mapAction class="w-screen h-screen"/>