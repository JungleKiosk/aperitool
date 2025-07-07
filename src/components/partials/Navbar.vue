<script>
import lang from "../partials/LangSwitcher.vue"
export default {
  name: "Navbar",
  components: {
    lang
  },
  data() {
    return {
      isDarkMode: false
    };
  },
  mounted() {
    this.checkTheme();
    window.addEventListener("storage", this.syncTheme);
  },
  methods: {
    checkTheme() {
      const currentTheme = localStorage.getItem("theme");
      this.isDarkMode = currentTheme === "dark-mode";
    },
    syncTheme() {
      this.checkTheme();
    },
    toggleTheme() {
      this.isDarkMode = !this.isDarkMode;
      localStorage.setItem("theme", this.isDarkMode ? "dark-mode" : "light-mode");
      document.body.classList.toggle("dark-mode", this.isDarkMode);
      document.body.classList.toggle("light-mode", !this.isDarkMode);

    }
  }
};
</script>

<template>
  <nav class="navbar justify-content-center p-4">
    <ul>
      <li><router-link to="/">Home</router-link></li>
      <li><router-link to="/tools">Tools</router-link></li>
      <li><router-link to="/links">Links</router-link></li>
      <li>
        <!-- ✅ Bottone per cambiare tema -->
        <button @click="toggleTheme" class="theme-button rounded-5">
          {{ isDarkMode ? 'Light' : 'Dark' }}
        </button>
      </li>
<!--       <li>
        <lang></lang>
      </li> -->
    </ul>
  </nav>
</template>
