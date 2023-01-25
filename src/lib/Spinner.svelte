
<script>
    import { loading } from "../stores.js";
    import { fade } from 'svelte/transition'
</script>

{#if $loading}
    <div out:fade style="transform: translate(-50%, -50%);" class="bg-white dark:bg-neutral flex align-center shadow-md rounded-xl w-32 h-32 absolute top-1/2 left-1/2">
        <div class="loader ease-linear rounded-full border-8 border-t-8 border-gray-200 h-16 w-16 m-auto"></div>
    </div>
{/if}

<style>
.loader {
  border-top-color: rgb(132, 24, 43, 0.5);
  -webkit-animation: spinner 1.5s linear infinite;
  animation: spinner 1.5s linear infinite;
}

@-webkit-keyframes spinner {
  0% { -webkit-transform: rotate(0deg); }
  100% { -webkit-transform: rotate(360deg); }
}

@keyframes spinner {
  0% { transform: rotate(0deg); }
  100% { transform: rotate(360deg); }
}
</style>

