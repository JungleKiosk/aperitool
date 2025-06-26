<script>
export default {
  name: "HomeMain",
  data() {
    return {
      keywords: [
        "Agronomy", "Forestry", "GIS", "QGIS", "Remote Sensing", "Python", "Soil Data",
        "OCR", "Web Development", "Data Cleaning", "Environmental Analysis", "Survival"
      ],
    };
  },
};
</script>

<template>
  <div class="container">
    <!-- Keywords Slider -->
    <!--     <div class="keyword-slider text-center">
      <div class="scrolling-keywords">
        <span v-for="(word, index) in keywords" :key="index" class="badge bg-info text-dark mx-2 p-2 rounded-pill">
          {{ word }}
        </span>
      </div>
    </div> -->

    <div class="row justify-content-center">
      <div class="col-12 col-lg-6">
        <p class="display-1 text-center text-lg-start">
          Explore tools and resources
        </p>
        <p class="display-6 text-center text-lg-start">
          Download ZIP with scripts and documentation
        </p>
        <p class="">
          Aperitools is a collection of useful tools for data analysis in agronomy, forestry, and environmental
          sciences. It also includes Python scripts, QGIS extensions, document converters, and even practical techniques
          for remote fieldwork and survival. Ideal for researchers, developers, students, geeks, nerds and tech lovers.
        </p>
      </div>
      <div class="col-12 col-lg-6">
        <img src="../../assets/img/home/3_hand.png" alt="">
      </div>
    </div>


  </div>
</template>

<style scoped>
img {
  width: 90%;
}


.keyword-slider {
  overflow-x: none;
  white-space: nowrap;
}

.scrolling-keywords {
  display: inline-block;
  animation: scroll 30s linear infinite;
}

@keyframes scroll {
  0% {
    transform: translateX(100%);
  }

  100% {
    transform: translateX(-100%);
  }
}
</style>
