<script lang="ts">
	import { onMount } from "svelte";

	// @ts-ignore
	let apiKey: string;

	import Map from "./components/Map.svelte";
	import Sidebar from "./components/Sidebar.svelte";
	let startLocation = "";
    let endLocation = "";

    onMount(async () => {
        await fetch("/api/OsdatahubAuth", {
        method: "POST",
        body: JSON.stringify({
        key: "mgz99Gos1K50W1SpyQEOUqFujOxKpqyz"
    })
    }).then(response => response.json()).then(response => apiKey = response.access_token)
    })

    $: apiKey = apiKey

</script>


<svelte:head>
	<link href="https://fonts.googleapis.com/css2?family=Truculenta:opsz,wght@12..72,200;12..72,400&display=swap" rel="stylesheet">

</svelte:head>

<main class="flex">
	<Sidebar/>
	<Map apiKey={apiKey}/>
</main>

<style global lang="postcss">
	@tailwind base;
	@tailwind components;
	@tailwind utilities;

</style>