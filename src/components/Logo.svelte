<script>
    import { onMount } from "svelte";
    import * as THREE from "three";
    import { GLTFLoader } from 'three/examples/jsm/loaders/GLTFLoader.js';


    import * as SC from "svelte-cubed";

    const modelURL = "newscene.gltf"
    let model = null;
    let spin=0

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

</script>

<div class="w-full h-screen m-auto align-middle flex">
    <h1 class="z-50 m-auto">PRET CRAWL</h1>
    <!-- <div class="flex h-screen">
        <div class="m-auto">
          <h3>title</h3>
          <button>button</button>
        </div>
      </div> -->
    <div id="star" class="z-40">
        <SC.Canvas antialias background={new THREE.Color("papayawhip")}>
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
            <SC.PerspectiveCamera position={[0, 10, 0]} />
            <SC.OrbitControls enableZoom={false} />
        
        </SC.Canvas>
    </div>
</div>

