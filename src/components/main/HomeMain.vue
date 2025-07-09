<script>
import linksData from "./../../data/links.json";

export default {
  name: "HomeMain",
  data() {
    return {
      collections: [],
      featuredLinks: [
        {
          title: "QGIS Certification",
          url: "https://certification.qgis.org/en/",
          description: "Official QGIS certification resources.",
        },
        {
          title: "Deepnote",
          url: "https://deepnote.com/docs/getting-started",
          description: "Collaborative data science notebooks.",
        },
        {
          title: "How to use Google Colab",
          url: "https://www.geeksforgeeks.org/how-to-use-google-colab/",
          description:
            "A comprehensive guide on using Google Colab for data science.",
        },
        {
          title: "PyQGIS Masterclass",
          url: "https://courses.spatialthoughts.com/pyqgis-masterclass.html#introduction",
          description: "Advanced QGIS automation with Python.",
        },
      ],
      utilities: [
        {
          title: "QGIS Certification",
          url: "https://deepnote.com/docs/getting-started",
          description: "Official QGIS certification resources.",
        },
        {
          title: "Free Geodata APIs",
          url: "https://www.freepublicapis.com/tags/geodata",
          description: "Explore APIs for geospatial data.",
        },
        {
          title: "How to use Google Colab",
          url: "https://www.geeksforgeeks.org/how-to-use-google-colab/",
          description:
            "A comprehensive guide on using Google Colab for data science.",
        }
      ],
      games: [
        {
          title: "OpenGuesser",
          url: "https://openguessr.com/",
          description: "A geography trivia game based on Google Maps.",
        },
        {
          title: "World Geography Games",
          url: "https://world-geography-games.com/index.html",
          description:
            "Test your knowledge of world geography with these fun games.",
        },
        {
          title: "Toporopa",
          url: "https://www.toporopa.eu/en/",
          description: "A geography trivia game to test your knowledge.",
        },
        {
          title: "GeoGrid",
          url: "https://www.geogridgame.com/",
          description:
            "Test your geography knowledge with this engaging grid-based game.",
        },
      ],
      curiosities: [
        {
          title: "Old Maps Online",
          url: "https://www.oldmapsonline.org/it/Alps#position=5.7815/44.52/8.94&year=1935",
          description: "Explore historical maps of the Alps.",
        },
        {
          title: "Rare Maps",
          url: "https://www.raremaps.com/",
          description: "A collection of rare and antique maps.",
        },
        {
          title: "AirNav Radar",
          url: "https://www.airnavradar.com/@48.80300,2.26690,z6",
          description: "Live flight tracking and radar information.",
        },
        {
          title: "Go-Cart",
          url: "https://go-cart.io/",
          description: "A fun and interactive online go-kart racing game.",
        },
      ],
    };
  },
  created() {
    this.extractCollections();
  },
  methods: {
    extractCollections() {
      if (Array.isArray(linksData.links)) {
        this.collections = linksData.links.map((section) => {
          return {
            name: section.collection,
            count: section.data.length, // conteggio dei link
          };
        });
      }
    },
  },
};
</script>

<template>
  <div class="container py-4">
    <!-- Header -->
    <div class="row justify-content-center mb-5">
      <div class="col-12 col-lg-6">
        <p class="display-1 text-lg-start">Explore tools and resources</p>
        <p class="display-6 text-lg-start">
          Download ZIP with scripts and documentation
        </p>
        <p>
          Aperitool is a versatile and growing knowledge base for data analysis
          in agronomy, forestry, and environmental sciences.
          <br />
          It offers Python scripts, QGIS plugins, transcription tools (like
          Whisper), and other practical utilities to support both fieldwork and
          data preprocessing tasks — from raw text cleanup to remote sensing and
          survival strategies.
        </p>
      </div>
      <div
        class="col-12 col-lg-6 d-flex flex-wrap justify-content-center gap-3"
      >
        <router-link
          class="collection-card col-3 text-center text-decoration-none p-2"
          v-for="(item, index) in collections"
          :key="index"
          :to="{ path: '/links', query: { collection: item.name } }"
        >
          <h6 class="fw-bold">{{ item.name }}</h6>
          <small class="items_links">{{ item.count }} links</small>
        </router-link>
      </div>
    </div>

    <!-- Featured Links -->

    <div class="row align-items-center mb-5">
      <!-- CARD CONTAINER -->
      <div class="col-12 col-lg-4">
        <h2 class="my-4">Featured Resources</h2>
        <div class="row g-3">
          <div
            class="col-12 col-lg-6"
            v-for="(item, index) in featuredLinks"
            :key="index"
          >
            <div class="card h-100 shadow-sm featured-resources">
              <div class="card-body d-flex flex-column">
                <h5 class="card-title fw-bold">{{ item.title }}</h5>
                <p class="card-text flex-grow-1">{{ item.description }}</p>
                <a :href="item.url" class="btn btn_fr" target="_blank">
                  Website
                </a>
              </div>
            </div>
          </div>
        </div>
      </div>
      <!-- IMMAGINE -->
      <div
        class="col-12 col-lg-4 text-center d-flex justify-content-center mt-4-sm"
      >
        <img
          src="../../assets/img/icons/3_lime_clip.png"
          alt="Aperitools Logo"
          class="img-fluid"
        />
      </div>
      <!-- CARD CONTAINER -->
      <div class="col-12 col-lg-4">
        <div class="row g-3">
          
        </div>
      </div>
    </div>

    <h2 class="">Utilities</h2>
    <div class="row justify-content-center align-items-center gap-2 mb-5">
      <!-- IMMAGINE -->
      <div class="col-12 col-lg-6 text-center">
        <img
          src="../../assets/img/icons/5_lime2.png"
          alt="Aperitools Logo"
          class=""
        />
      </div>
      <!-- CARD CONTAINER -->

      <div class="row justify-content-center gap-3">
        <div
          class="col-12 col-lg-3"
          v-for="(item, index) in utilities"
          :key="index"
        >
          <div class="card h-100 shadow-sm featured-resources">
            <div class="card-body">
              <h5 class="card-title fw-bold">{{ item.title }}</h5>
              <p class="card-text flex-grow-1">{{ item.description }}</p>
              <a :href="item.url" class="btn btn_fr" target="_blank">
                Website
              </a>
            </div>
          </div>
        </div>
      </div>
    </div>

    <h2 class="">Games</h2>
    <p class="">
      Explore our collection of featured games designed for learning and
      engagement.
    </p>

    <div class="row justify-content-center align-items-center gap-2 mb-5">
      <!-- IMMAGINE -->
      <div class="col-12 col-lg-6 text-center">
        <img
          src="../../assets/img/icons/5_lime2.png"
          alt="Aperitools Logo"
          class=""
        />
      </div>
      <!-- CARD CONTAINER -->

      <div class="row justify-content-center gap-3">
        <div
          class="col-12 col-lg-3"
          v-for="(item, index) in games"
          :key="index"
        >
          <div class="card h-100 shadow-sm featured-resources">
            <div class="card-body">
              <h5 class="card-title fw-bold">{{ item.title }}</h5>
              <p class="card-text flex-grow-1">{{ item.description }}</p>
              <a :href="item.url" class="btn btn_fr" target="_blank">
                Website
              </a>
            </div>
          </div>
        </div>
      </div>
    </div>

    

    <h2 class="">Curiosities</h2>
    <p class="">
      Explore our collection of featured games designed for learning and
      engagement.
    </p>

    <div class="row justify-content-center align-items-center gap-2">
      <!-- IMMAGINE -->
      <div class="col-12 col-lg-6 text-center">
        <img
          src="../../assets/img/icons/6_pata2.png"
          alt="Aperitools Logo"
          class="pata"
        />
      </div>
      <!-- CARD CONTAINER -->

      <div class="row justify-content-center gap-3">
        <div
          class="col-12 col-lg-3"
          v-for="(item, index) in curiosities"
          :key="index"
        >
          <div
            class="card h-100 shadow-sm featured-resources align-items-center"
          >
            <div class="card-body">
              <h5 class="card-title fw-bold">{{ item.title }}</h5>
              <p class="card-text flex-grow-1">{{ item.description }}</p>
              <a :href="item.url" class="btn btn_fr" target="_blank">
                Website
              </a>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
img {
  width: 70%;
}

.pata {
  width: 40%;
}
</style>
