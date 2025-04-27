<script>
import toolsData from "../../data/tools.json";

export default {
  name: "ToolsMain",
  data() {
    return {
      tools: toolsData,
      filteredTools: toolsData,
      searchQuery: "",
      selectedTag: "",
    };
  },
  computed: {
    allTags() {
      const tags = new Set();
      this.tools.forEach((tool) => {
        tool.tags.forEach((t) => tags.add(t));
      });
      return Array.from(tags);
    },
  },
  methods: {
    filterByTag(tag) {
      this.selectedTag = this.selectedTag === tag ? "" : tag;
      this.applyFilters();
    },
    onSearchInput() {
      this.applyFilters();
    },
    resetAllFilters() {
      this.searchQuery = "";
      this.selectedTag = "";
      this.applyFilters();
    },
    applyFilters() {
      const q = this.searchQuery.toLowerCase();
      this.filteredTools = this.tools.filter((tool) => {
        const matchesText =
          tool.name.toLowerCase().includes(q) ||
          tool.description.toLowerCase().includes(q);
        const matchesTag =
          !this.selectedTag || tool.tags.includes(this.selectedTag);
        return matchesText && matchesTag;
      });
    },
  },
};
</script>

<template>
  <div class="container mt-5">
    <h1>Tools</h1>

    <!-- Search & Reset -->
    <div class="d-flex mb-3">
      <input
        v-model="searchQuery"
        @input="onSearchInput"
        type="text"
        class="form-control me-2"
        placeholder="Cerca tool..."
      />
      <button class="btn btn-secondary" @click="resetAllFilters">Reset</button>
    </div>

    <!-- Tag Slider -->
    <div class="d-flex overflow-auto mb-4">
      <button
        v-for="tag in allTags"
        :key="tag"
        class="btn mx-1"
        :class="selectedTag === tag ? 'btn-primary' : 'btn-outline-primary'"
        @click="filterByTag(tag)"
      >
        {{ tag }}
      </button>
    </div>

    <!-- Tool Cards -->
    <div class="row g-4">
      <div
        class="col-6 col-md-4 col-lg-3"
        v-for="tool in filteredTools"
        :key="tool.id"
      >
        <div class="card h-100 shadow-sm">
          <div class="card-body d-flex flex-column">
            <h5 class="card-title">{{ tool.name }}</h5>
            <p class="card-text flex-grow-1">{{ tool.description }}</p>
            <!-- External Link -->
            <a
              v-if="tool.links"
              :href="tool.links"
              target="_blank"
              class="mb-2"
            >
              Source
            </a>
            <div class="mb-2">
              <span
                v-for="t in tool.tags"
                :key="t"
                class="badge bg-info text-dark me-1"
              >
                {{ t }}
              </span>
            </div>
            <!-- Download ZIP file -->
            <a
              v-if="tool.filename"
              class="btn btn-primary btn-sm mb-2"
              :href="`/tools/${tool.filename.replace('.py', '.zip')}`"
              download
            >
              Download ZIP 📦
            </a>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.card {
  border: none;
}
</style>
