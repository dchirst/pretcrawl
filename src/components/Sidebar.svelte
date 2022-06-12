<script>
import { onMount } from "svelte";

    import Logo from "./Logo.svelte";

</script>


<div class="w-96 h-screen">
    <Logo/>
    <p>Data is {JSON.stringify(value)}</p>
</div>