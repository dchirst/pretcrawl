<script lang="ts">
	import { onMount } from "svelte";

	// @ts-ignore
	let apiKey: string = OS_API_KEY;

	import Map from "./components/Map.svelte";
	import Sidebar from "./components/Sidebar.svelte";
	let startLocation = "";
    let endLocation = "";

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