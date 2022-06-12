<script>
import { onMount } from "svelte";

    import Logo from "./Logo.svelte";

    let value;
    onMount(async () => {
        await fetch("/api/OsdatahubAuth", {
        method: "POST",
        body: JSON.stringify({
        key: process.env.OS_API_KEY
    })
    }).then(response => response.json()).then(response => value = response)
    })

    $: value = value

</script>


<div class="w-96 h-screen">
    <Logo/>
    <p>Data is {JSON.stringify(value)}</p>
</div>