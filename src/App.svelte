<script lang="ts">
	// @ts-ignore
	const apiKey: string = OS_API_KEY;

	import Map from "./components/Map.svelte";
	import Sidebar from "./components/Sidebar.svelte";
	let startLocation = "";
    let endLocation = "";
</script>

<main class="flex">
	<Sidebar/>
	<Map apiKey={apiKey}/>
</main>

<style global lang="postcss">
	@tailwind base;
	@tailwind components;
	@tailwind utilities;

</style>