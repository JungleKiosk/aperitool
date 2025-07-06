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
          title: "Free Geodata APIs",
          url: "https://www.freepublicapis.com/tags/geodata",
          description: "Explore APIs for geospatial data.",
        },
        {
          title: "Free Online Courses",
          url: "https://www.freecodecamp.org/news/most-popular-free-online-courses/",
          description: "Top free courses from FreeCodeCamp.",
        },
        {
          title: "PyQGIS Masterclass",
          url: "https://courses.spatialthoughts.com/pyqgis-masterclass.html#introduction",
          description: "Advanced QGIS automation with Python.",
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
        <p class="display-1 text-center text-lg-start">
          Explore tools and resources
        </p>
        <p class="display-6 text-center text-lg-start">
          Download ZIP with scripts and documentation
        </p>
        <p>
          Aperitools is a collection of useful tools for data analysis in
          agronomy, forestry, and environmental sciences. It also includes
          Python scripts, QGIS extensions, document converters, and even
          practical techniques for remote fieldwork and survival.
        </p>
      </div>
      <!--     <div class="col-12 col-lg-6 d-flex align-items-center justify-content-center">
        <img src="../../assets/img/home/3_hand.png" alt="Aperitools logo" />
      </div> -->

      <!--       <h2 class="text-center my-4">Link Collections</h2> -->

      <div class="col-12 col-lg-6 d-flex flex-wrap justify-content-center gap-3">
        <router-link
          class="col-3 border rounded shadow-sm text-center text-decoration-none text-dark p-2"
          v-for="(item, index) in collections"
          :key="index"
          :to="{ path: '/links', query: { collection: item.name } }"
        >
          <h6 class="fw-bold">{{ item.name }}</h6>
          <small>{{ item.count }} links</small>
        </router-link>
      </div>
    </div>

    <!-- Featured Links -->

    <h2 class="text-center">Featured Resources</h2>
    <div class="row">
      <div
        class="col-12 col-md-6 col-lg-3"
        v-for="(item, index) in featuredLinks"
        :key="index"
      >
        <div class="card">
          <div class="card-body">
            <h5 class="card-title">{{ item.title }}</h5>
            <p class="card-text">{{ item.description }}</p>
            <a :href="item.url" class="btn btn-outline-primary" target="_blank"
              >Visit</a
            >
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
img {
  width: 90%;
}
</style>
