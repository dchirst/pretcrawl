<script>
    import Logo from "./Logo.svelte";

    let value;
    fetch("/api/OsdatahubAuth", {
        method: "POST",
        data: JSON.stringify({
    key: "mgz99Gos1K50W1SpyQEOUqFujOxKpqyz"
})
    }).then(response => response.json()).then(response => value = response)
</script>


<div class="w-96 h-screen">
    <Logo/>
    <p>Data is {value}</p>
</div>