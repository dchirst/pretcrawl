<script>
	import { onMount, onDestroy } from 'svelte'
	import { Map, Marker, SourceFeatureState } from 'maplibre-gl';
    import {startPoint, endPoint} from "../stores.js";
	import 'maplibre-gl/dist/maplibre-gl.css';
  
	let map;
	let apiKey;
    let startMarker;
    let endMarker;
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
                    if (!(url.endsWith(".geojson") || url.endsWith(".png"))) {
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
                map.addImage('star', image);
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
                        'icon-image': 'star',
                        'icon-size': 0.1,
                    }
            })

            })


            map.on('click', function(e) {
            // The event object (e) contains information like the
            // coordinates of the point on the map that was clicked.
            if (!startPoint) {
                startMarker = new Marker({
                    draggable: true
                })
                    .setLngLat(e.lngLat)
                .addTo(map);

                $startPoint = e.lngLat

            } else if (!endPoint) {
                endMarker = new Marker({
                    draggable: true
                })
                    .setLngLat(e.lngLat)
                .addTo(map);
                $endPoint = e.lngLat
            }

            });

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