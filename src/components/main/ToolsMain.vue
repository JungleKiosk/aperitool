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
      filterDownloadOnly: false,
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
      this.filterDownloadOnly = false;
      this.applyFilters();
    },
    toggleDownloadFilter() {
      this.filterDownloadOnly = !this.filterDownloadOnly;
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
        const matchesDownload =
          !this.filterDownloadOnly || (tool.filename && tool.filename !== 0);

        return matchesText && matchesTag && matchesDownload;
      });
    },
  },
};
</script>

<template>
  <div class="container mt-5">
    <div class="container_filters_tools">
      <div class="col-12 col-lg-6">
        <div class="flex-grow-1 d-flex">
          <input
            v-model="searchQuery"
            @input="onSearchInput"
            type="text"
            class="form-control me-2"
            placeholder="Search..."
          />
          <button class="btn btn-warning mx-2" @click="resetAllFilters">
            Reset
          </button>
        </div>
        <div class="form-check ms-3">
          <input
            type="checkbox"
            id="download-only"
            v-model="filterDownloadOnly"
            @change="applyFilters"
            class="form-check-input me-2"
          />
          <label for="download-only" class="form-check-label">
            Show Only Downloadable
          </label>
        </div>
      </div>
      <div class="row">
        <div class="category_slider_tools">
          <div class="col-12">
            <div class="d-flex overflow-auto mb-2 p-2">
              <button
                v-for="tag in allTags"
                :key="tag"
                class="btn mx-1"
                :class="selectedTag === tag ? 'btn-primary' : 'btn_blulight'"
                @click="filterByTag(tag)"
              >
                {{ tag }}
              </button>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- Tag Slider -->

    <!-- Tools Cards -->
    <div class="row g-4 mt-5">
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
              v-if="tool.filename && tool.filename !== 0"
              class="btn btn-primary btn-sm mt-auto"
              :href="`/tools/${tool.filename}`"
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

.category-slider {
  white-space: nowrap;
}
</style>
