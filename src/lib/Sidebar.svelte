
<script>
    import {startPoint, endPoint} from "../stores.js"

    let text = ""
    function runPretCrawl() {

        text = `start point: ${JSON.stringify($startPoint)}\nend point: ${JSON.stringify($endPoint)}`
        const params = {
            startPointLng: $startPoint.lng,
            startPointLat: $startPoint.lat,
            endPointLng: $endPoint.lng,
            endPointLat: $endPoint.lat
        }
        fetch("/api/runpretcrawl?" + new URLSearchParams(params))
        .then((response) => response.json())
        .then((response) => console.log(response))
    }
</script>

<div class="w-96 h-1/2 absolute inset-10 bg-white z-50 rounded-md shadow-md">
<h1>Pret Crawl</h1>

<button class="bg-primary text-white" on:click={runPretCrawl}>Run</button>
<p>{text}</p>
</div>

