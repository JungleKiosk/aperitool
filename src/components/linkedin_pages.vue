<script>
import linkedinPages from "../data/linkedin_pages.json";

export default {
  name: "LinkedinPages",
  data() {
    return {
      pages: linkedinPages,
      filteredPages: linkedinPages,
      searchQuery: "",
      selectedType: "",
    };
  },
  computed: {
    allTypes() {
      const types = new Set();
      this.pages.forEach((p) => types.add(p.type));
      return Array.from(types);
    },
  },
  methods: {
    filterByType(type) {
      this.selectedType = this.selectedType === type ? "" : type;
      this.applyFilters();
    },
    onSearchInput() {
      this.applyFilters();
    },
    resetAllFilters() {
      this.searchQuery = "";
      this.selectedType = "";
      this.applyFilters();
    },
    applyFilters() {
      const q = this.searchQuery.toLowerCase();
      this.filteredPages = this.pages.filter((page) => {
        const matchesText = page.title.toLowerCase().includes(q);
        const matchesType =
          !this.selectedType || page.type === this.selectedType;
        return matchesText && matchesType;
      });
    },
  },
};
</script>

<template>
  <div class="container my-5">
    <h1 class="mb-4">LinkedIn pages</h1>

    <!-- Filtro + Ricerca -->
    <div class="row container_filters_tools">
      <div class="col-4">
        <div class="mb-2 text-center tool_count">
          Total items: {{ filteredPages.length }} / {{ pages.length }}
        </div>
        <div class="d-flex mb-3">
          <input
            v-model="searchQuery"
            @input="onSearchInput"
            type="text"
            class="form-control me-2"
            placeholder="Search..."
          />
          <button class="btn btn_all mx-2" @click="resetAllFilters">All</button>
        </div>
        <div class="d-flex overflow-auto mb-2 p-2 category-slider">
          <button
            v-for="type in allTypes"
            :key="type"
            class="badge rounded-3 border-0 tags_page mx-1"
            :class="{ active: selectedType === type }"
            @click="filterByType(type)"
          >
            {{ type }}
          </button>
        </div>
      </div>
    </div>

    <!-- Cards -->
    <div class="row g-4 mt-4">
      <div
        class="col-12 col-md-4 col-lg-3"
        v-for="(page, index) in filteredPages"
        :key="index"
      >
        <div class="card card_color h-100 shadow-sm">
          <div class="card-body d-flex flex-column">
            <h5 class="card-title">{{ page.title }}</h5>
            <p class="card-text">
              <strong>{{ page.type }}</strong>
            </p>
            <a :href="page.url" class="btn btn_fr mt-auto" target="_blank">
              Visit Page
            </a>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped></style>
