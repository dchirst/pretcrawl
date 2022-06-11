<script>
    import { onMount } from "svelte";
    import * as THREE from "three";
    import { GLTFLoader } from 'three/examples/jsm/loaders/GLTFLoader.js';


    import * as SC from "svelte-cubed";

    const modelURL = "/newscene.gltf"
    let model = null;
    let spin=0
    let logoWidth;
    let logoHeight;

    SC.onFrame(() => {
        spin += 0.01;
    });

    function loadGLTF() {
        const loader = new GLTFLoader();
        return loader.loadAsync(modelURL)
        }

    onMount(() => {
        loadGLTF().then(_model => model = _model.scene.children[0].geometry);
    })

    var mat001 = new THREE.MeshPhysicalMaterial();
    mat001.color = new THREE.Color(0x910826);
    mat001.reflectivity = 1.0;
    mat001.roughness = 0.0;
    mat001.envMapIntensity = 1.0;

    var offset = 0.7
</script>

<div bind:clientWidth={logoWidth} bind:clientHeight={logoHeight} class="w-96 h-32 m-auto align-middle" id="logo">
    <div class="h-full w-full flex" id="title">
        <div class="z-50 flex h-full w-full">
            <div class="h-full w-full">
                <h1 class="font-title  my-8 text-6xl ml-4 align-text-middle ">PRET</h1>
            </div>
            <div class="h-full w-full">
                <h1 class="font-title text-6xl text-right mr-4 my-8">CRAWL</h1>
            </div>

        </div>
    </div>

    <div id="star" class="z-40 w-96 h-32">
        <SC.Canvas class="w-96 h-32" antialias background={new THREE.Color("papayawhip")} >
            <SC.AmbientLight intensity={0.9}/>
            <SC.DirectionalLight intensity={0.6} position={[-2, 3, 2]}/>
            {#if model}
            <SC.Mesh
                geometry={model}
                scale={[.05,.05,.05]}
                material={mat001}
                rotation={[0, 0, spin]}
            />
            {/if}
            <SC.PerspectiveCamera position={[offset, 5, 0]} target={[offset, 0, 0]}/>
            <SC.OrbitControls enableZoom={false} enablePan={false}/>
        
        </SC.Canvas>
    </div>
</div>

