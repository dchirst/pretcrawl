<script>
	import { onMount, onDestroy } from 'svelte'
	import { Map } from 'maplibre-gl';
	import 'maplibre-gl/dist/maplibre-gl.css';
  
	let map;
	let apiKey;
	function getToken() {
		return fetch("/api/OsdatahubAuth")
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
				center: [-1.608411, 54.968004],
				zoom: 9,
				maxZoom: 15,
				transformRequest: url => {
					url += '&srs=3857';
					return {
						url: url,
						headers: {'Authorization': 'Bearer ' + apiKey}
					}
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