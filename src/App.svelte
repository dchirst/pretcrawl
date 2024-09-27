<script>
	import Map from "./lib/Map.svelte";
	import Sidebar from "./lib/Sidebar.svelte";
    import Spinner from "./lib/Spinner.svelte";
    import SvelteSeo from "svelte-seo";

</script>

<SvelteSeo
  title="Pret Crawl"
  description="Pret Crawl is a tool for those who love to walk with a coffee in their hand.
    Simply choose your route, and the Pret Crawl will find the optimal Pret A Manger's to visit throughout your journey",
  keywords="Pret,Pret A Manger, Map, Crawl"
  openGraph={{
    title: 'Make your own Pret Crawl',
    description: 'Forever walk through London with a Pret in your hand',
    url: 'pretcrawl.danhirst.me',
    type: 'website',
    images: [
      {
        url: 'https://raw.githubusercontent.com/dchirst/pretcrawl/master/media/pretcrawl-logo.jpg',
        width: 850,
        height: 650,
        alt: 'Pret Crawl Logo'
      },
      {
        url: 'https://raw.githubusercontent.com/dchirst/pretcrawl/master/media/app-screenshot.png',
        width: 850,
        height: 650,
        alt: 'Pret Crawl Screenshot'
      }
     ]
  }}
/>

<Sidebar/>
<Map/>
<Spinner/>
