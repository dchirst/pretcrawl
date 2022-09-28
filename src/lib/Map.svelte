<script>
	import { onMount, onDestroy } from 'svelte'
	import { Map } from 'maplibre-gl';
	import 'maplibre-gl/dist/maplibre-gl.css';
  
	let map;
	let apiKey;
	function getToken() {
		return fetch("/api/osdatahubauth")
			.then((response) => response.json())
					.then(result => {
			  if(result.access_token) {
				  // Store this token
				  apiKey = result.access_token;
  
				  // Get a new token 30 seconds before this one expires
				  const timeoutMS = (result.expires_in - 30) * 1000;
				  setTimeout(getToken, timeoutMS);
			  } else {
				  // We failed to get the token
				  return Promise.reject();
			  }
		  })
		  .catch(error => {
			  return Promise.reject();
		  });
	}
  
  
	onMount(() => {

		getToken().then(() => {
			var serviceUrl = "https://api.os.uk/maps/vector/v1/vts";
			map = new Map({
				container: 'map',
				style: serviceUrl + '/resources/styles?',
				center: [-0.110281, 51.519787],
				zoom: 9,
				maxZoom: 15,
				transformRequest: url => {
                    if (!url.endsWith(".geojson")) {
                        url += '&srs=3857';
                    }
					return {
						url: url,
						headers: {'Authorization': 'Bearer ' + apiKey}
					}
				}
			});

            map.once("load", () => {

            map.loadImage('star.png', function (error, image) {
                if (error) throw error;
                map.addImage('Airport_icon', image);
            });
            map.addSource("prets", {
                type: "geojson",
                data: "prets.geojson" //"./GeoObs.json",
                /*cluster: true,
                clusterMaxZoom: 15, // Max zoom to cluster points on
                clusterRadius: 50 // Radius of each cluster when clustering points (defaults to 50)*/
            });

            map.addLayer({
                id: "Prets",
                type: "symbol",
                source: "prets",
                layout: {
                        'icon-image': 'Airport_icon',
                        'icon-size': 0.1,
                    }
            })

            })
  
		})


  
  
	});
  
	onDestroy(() => {
	  map.remove();
	});
  </script>
  
  <div id="map" style="position: fixed" />
  
  <style>
	#map {
	  position: absolute;
	  top: 0;
	  left: 0;
	  width: 100%;
	  height: 100%;
	  cursor: pointer;
	}
  </style>