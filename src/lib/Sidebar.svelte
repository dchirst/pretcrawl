<script>
    import {endPoint, route, startPoint} from "../stores.js"
    import Logo from "./Logo.svelte";

    const googleDirectionsURL = "https://www.google.com/maps/dir/?api=1&"
    function generateGoogleMapsLink(pretCrawlRoute) {
        pretCrawlRoute = [...pretCrawlRoute.geometry.coordinates]
        const params = {
            travelmode: "walking",
            origin: pretCrawlRoute[0].reverse(),
            destination: pretCrawlRoute[pretCrawlRoute.length - 1].reverse(),
            waypoints:  pretCrawlRoute.slice(1, 4).map(el => el.reverse()).join("|")
        };
        return googleDirectionsURL + new URLSearchParams(params)
    }

    let googleLink;
    let text = ""
    let pretNames = ""

    let googleUrl = ""
    let visibility = false
    function runPretCrawl() {
        if (!$startPoint || !$endPoint) {
            text = "You must set a start and end point first. Click the map to get started"
            return
        } else {
            text = "";
        }

        const params = {
            startPointLng: $startPoint.lng,
            startPointLat: $startPoint.lat,
            endPointLng: $endPoint.lng,
            endPointLat: $endPoint.lat
        }
        fetch("/api/runpretcrawl?" + new URLSearchParams(params))
        .then((response) => response.json())
        .then((response) => {
            $route = response;
            pretNames = $route.properties.selectedPrets.features.map(p => p.properties.name);
            googleUrl = generateGoogleMapsLink($route);
            visibility = true;
        })


    }
</script>

<div class="w-screen h-screen flex">
    <div class="w-full  h-auto absolute top-2/3 bg-white z-50 rounded-xl shadow-md p-10 pt-0 mx-auto
    sm:w-96 sm:m-0 sm:top-10 sm:left-10 sm:pt-10 dark:bg-neutral">
        <hr class="mx-auto my-8 w-1/2 h-1 bg-gray-200 rounded border-0 dark:bg-gray-700 sm:invisible sm:absolute">
        <Logo/>
        <button class="bg-primary text-white m-5" on:click={runPretCrawl}>Run</button>
        <p class="text-red-500">{text}</p>

        <p class="text-left"><strong>An app for those who want to always have a Pret in their hand.</strong> <br><br>
            Pick your start and end point, and the Pret Crawl will tell you the optimal Pret A Manger's to visit along your route. <br>
            This app is designed for folks who have the Pret Subscription, where you are allowed up to 5 free drinks a day with a 30 minute gap between each one.</p>
        {#if visibility}
            <hr class="mx-auto my-3 bg-gray-600 w-1/2">
            <p> You are visiting <strong>{pretNames.length}</strong> Prets along your journey. They are:</p>
            <div class="border-black border-primary rounded-md m-1 border-2">
                <ul>
                    {#each pretNames as pret}
                        <li>{pret}</li>
                    {/each}
                </ul>
            </div>
            <a href="{googleUrl}" target="_blank">Google Maps Directions</a>
            <p>Happy Pretting!</p>
        {/if}

        <span class="align-bottom inline-block mt-5">
                    <p class="text-gray-400 italic">This app is not in any way affiliated with Pret A Manger</p>
                    <p class="text-gray-400">Created by <a href="https://github.com/dchirst">Dan Hirst</a></p>
        </span>

    </div>
</div>


