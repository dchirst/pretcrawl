<script lang="ts">
	export let name: string;
	// @ts-ignore
	const apiKey = OS_API_KEY;
</script>

<main>
	<h1 class="font-mono text-xl">Hello {name}</h1>
	<p>Visit the <a href="https://svelte.dev/tutorial">Svelte tutorial</a> to learn how to build Svelte apps.</p>
</main>

<style global lang="postcss">
	@tailwind base;
	@tailwind components;
	@tailwind utilities;

</style>