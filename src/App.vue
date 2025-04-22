<script>
import Navbar from "./components/partials/Navbar.vue";
import Header from "./components/main/Header.vue";
import Footer from "./components/partials/Footer.vue";


export default {
  components: {
    Navbar, Footer, Header
  },
  data() {
    return {
      isDarkMode: false // default value for dark mode
    };
  },
};
</script>

<template>
  <div id="app">
    <Navbar/>
    <Header></Header>
    <router-view />
    <Footer />
  </div>
</template>
