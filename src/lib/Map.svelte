<script>
    import {onMount, onDestroy} from 'svelte'
    import {startPoint, endPoint, route, loading} from "../stores.js";
    import 'mapbox-gl/dist/mapbox-gl.css';
    import mapboxgl from 'mapbox-gl'; // or "const mapboxgl = require('mapbox-gl');"

    let map;
    let startMarker;
    let endMarker;
    let dark;


    onMount(() => {

        function getStyle(isDark) {
            return isDark ? 'mapbox://styles/mapbox/dark-v11' : 'mapbox://styles/mapbox/light-v11';
        }

        function changeStyle(isDark) {

            const style = getStyle(isDark)
            if (map) {

                map.setStyle(style)
            }
        }


        if (localStorage.theme === 'dark' || (!('color-theme' in localStorage) && window.matchMedia('(prefers-color-scheme: dark)').matches)) {
            dark = true
        } else {
            dark = false
        }
        window.matchMedia('(prefers-color-scheme: dark)').addEventListener('change', event => {
            dark = event.matches;
            changeStyle(dark)
        });


        mapboxgl.accessToken = 'pk.eyJ1IjoiZGNoaXJzdCIsImEiOiJjbGRjM2cwYWMwNnJyNDBucjR0YTV1bTY5In0.JCC3YtBQrvDiG_JjAuaB9w';
        map = new mapboxgl.Map({
            container: 'map', // container ID
            // Choose from Mapbox's core styles, or make your own style with Mapbox Studio
            style: getStyle(dark), // style URL
            center: [-0.110281, 51.519787], // starting position [lng, lat]
            zoom: 14 // starting zoom
        });
        map.once("load", () => {
            $loading = false
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
                    'icon-size': 0.2,
                }
            });

            map.on('click', function (e) {
                // The event object (e) contains information like the
                // coordinates of the point on the map that was clicked.
                console.log($startPoint)
                console.log($endPoint)
                if (!$startPoint) {
                    startMarker = new mapboxgl.Marker({
                        draggable: true
                    })
                        .setLngLat(e.lngLat)
                        .addTo(map);
                    startMarker.on("dragend", onDragEndStartPoint)

                    $startPoint = e.lngLat

                } else if (!$endPoint) {
                    endMarker = new mapboxgl.Marker({
                        draggable: true
                    })
                        .setLngLat(e.lngLat)
                        .addTo(map);
                    endMarker.on('dragend', onDragEndEndPoint)
                    $endPoint = e.lngLat
                }


            });

            function onDragEndStartPoint() {
                $startPoint = startMarker.getLngLat();
            }

            function onDragEndEndPoint() {
                $endPoint = endMarker.getLngLat();
            }

            map.on('click', 'selectedPrets', function (e) {
                const name = e.features[0].properties.name;
                const coordinates = e.features[0].geometry.coordinates.slice();
                new mapboxgl.Popup()
                    .setLngLat(coordinates)
                    .setHTML(name)
                    .addTo(map);
            })

        })


        route.subscribe(r => {
            if (r) {
                if (map.getSource("route")) {
                    map.getSource("route").setData(r)
                    map.getSource("selectedPrets").setData(r.properties.selectedPrets)
                } else {
                    map.addSource("route", {
                        type: "geojson",
                        data: r
                    })
                    map.addLayer({
                        id: 'route',
                        source: 'route',
                        type: 'line',
                        paint: {
                            "line-color": "#bb5c5c",
                            "line-width": 10
                        }
                    }, "Prets");
                    map.addSource("selectedPrets", {
                        type: "geojson",
                        data: r.properties.selectedPrets
                    })
                    map.addLayer({
                        id: "selectedPrets",
                        type: "symbol",
                        source: "selectedPrets",
                        layout: {
                            'icon-image': 'star',
                            'icon-size': 0.4,
                        }
                    });
                }

                var coordinates = r.geometry.coordinates;
                var bounds = coordinates.reduce(function (bounds, coord) {
                    return bounds.extend(coord);
                }, new mapboxgl.LngLatBounds(coordinates[0], coordinates[0]));

                map.fitBounds(bounds, {
                    padding: 50,
                });


            }

        })


        // })


    });

    onDestroy(() => {
        map.remove();
    });
</script>

<div id="map" style="position: fixed"/>

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