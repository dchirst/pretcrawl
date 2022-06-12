<script>
import { onMount } from "svelte";

    import Logo from "./Logo.svelte";

    let value;
    onMount(async () => {
        await fetch("/api/OsdatahubAuth", {
        method: "POST",
        body: JSON.stringify({
        key: "xoUemUjfnXOdzwCBK6XpHsqJXXHe3T79"
    })
    }).then(response => response.json()).then(response => value = response)
    })

    $: value = value

</script>


<div class="w-96 h-screen">
    <Logo/>
    <p>Data is {JSON.stringify(value)}</p>
</div>