<script lang="ts">
	import { onMount } from "svelte";

	// @ts-ignore
	let apiKey: string = OS_API_KEY;

	import Map from "./components/Map.svelte";
	let startLocation = "";
    let endLocation = "";

	onMount(async () => {
		console.log("I am here")
        fetch(`/api/OsdatahubAuth`).then(response => response.text()).then(text => apiKey = text)
        
    })
</script>

<main>
	<Map apiKey={apiKey}/>
    <p>The API key is: <b>{apiKey}</b></p>
</main>

<style global lang="postcss">
	@tailwind base;
	@tailwind components;
	@tailwind utilities;

</style>