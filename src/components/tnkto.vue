<script>
import tanksto from "../data/tnksto.json";

export default {
  name: "tanksto",
  data() {
    return {
      pages: tanksto,
      filteredPages: tanksto,
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
    <h1 class="mb-4">Many Thanks 🍉</h1>
    <p>
      This page is a small tribute to the amazing LinkedIn community for all the
      shared resources. <br>
      Below is a personal thank you to the people and profiles
      from whom I’ve drawn most of the content found here in Aperitool.
    </p>

    <!-- Filtro + Ricerca -->
    <!--     <div class="row container_filters_tools mb-4">
      <div class="col-12 col-md-6">
        <div class="mb-2 text-center tool_count">
          Total items: {{ filteredPages.length }} / {{ pages.length }}
        </div>
        <div class="d-flex mb-2">
          <input
            v-model="searchQuery"
            @input="onSearchInput"
            type="text"
            class="form-control me-2"
            placeholder="Search..."
          />
          <button class="btn btn_all" @click="resetAllFilters">All</button>
        </div>
        <div class="d-flex overflow-auto p-2 category-slider">
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
    </div> -->

    <!-- Tabella -->
    <div class="table-responsive">
      <table class="table table-striped table-bordered">
        <thead class="table-light">
          <tr>
            <th scope="col">Name</th>
            <th scope="col">Topic</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="(page, index) in filteredPages" :key="index">
            <td>{{ page.name }}</td>
            <td>
              <span
                v-for="(cat, i) in page.categories"
                :key="i"
                class="tags_page rounded-5 px-2 mx-2 small"
              >
                {{ cat }}
              </span>
            </td>

            <!-- <td>
                <a :href="page.url" target="_blank" rel="noopener noreferrer">
                  Visit 🔗
                </a>
              </td> -->
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<style scoped></style>
