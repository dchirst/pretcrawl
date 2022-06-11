<script>
import { onMount } from "svelte";

    import Logo from "./Logo.svelte";

    let value;
    onMount(() => {
        fetch("/api/OsdatahubAuth", {
        method: "POST",
        body: JSON.stringify({
        key: "mgz99Gos1K50W1SpyQEOUqFujOxKpqyz"
    })
    }).then(response => response.json()).then(response => value = response)
    })

    $: value = value

</script>


<div class="w-96 h-screen">
    <Logo/>
    <p>Data is {JSON.stringify(value)}</p>
</div>