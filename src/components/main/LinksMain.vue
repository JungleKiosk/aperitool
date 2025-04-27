<script>
import linksData from "../../data/links.json";
import { groupedTags } from "../../data/tags.js";

export default {
  name: "LinksView",
  data() {
    return {
      searchQuery: "",
      collections: linksData.links,
      filteredCollections: [],
      groupedTags,
      selectedTag: "",
      filterDownloadOnly: false, // <- nuovo stato per toggle
      searchTimeout: null,
      openedCategory: null,
      showCategoryModal: false,
    };
  },
  created() {
    this.filteredCollections = this.collections;
  },
  methods: {
    getTagsForOpenedCategory() {
      const group = this.groupedTags.find(
        (g) => g.category === this.openedCategory
      );
      return group ? group.tags : [];
    },
    onSearchInput() {
      clearTimeout(this.searchTimeout);
      this.searchTimeout = setTimeout(this.applyFilters, 500);
    },
    filterByTag(tag) {
      this.selectedTag = this.selectedTag === tag ? "" : tag;
      this.applyFilters();
      this.closeCategoryModal();
    },
    applyFilters() {
      const q = this.searchQuery.toLowerCase();
      this.filteredCollections = this.collections
        .map((col) => {
          const filteredData = col.data.filter((item) => {
            const matchesTitle = item.title?.toLowerCase().includes(q);
            const matchesDescription = item.description
              ?.toLowerCase()
              .includes(q);
            const matchesUrl = item.url?.toLowerCase().includes(q);
            const matchesTags = item.tags?.some((tag) =>
              tag.toLowerCase().includes(q)
            );
            const matchesSearch =
              matchesTitle || matchesDescription || matchesUrl || matchesTags;
            const matchesTag =
              !this.selectedTag || item.tags.includes(this.selectedTag);
            const matchesDownload =
              !this.filterDownloadOnly || item.download === 1;

            return matchesSearch && matchesTag && matchesDownload;
          });
          return { ...col, data: filteredData };
        })
        .filter((col) => col.data.length > 0);
    },
    openCategoryModal(category) {
      this.openedCategory = category;
      this.showCategoryModal = true;
    },
    closeCategoryModal() {
      this.showCategoryModal = false;
      this.openedCategory = null;
    },
    toggleDownloadFilter() {
      this.filterDownloadOnly = !this.filterDownloadOnly;
      this.applyFilters();
    },
    resetAllFilters() {
      this.searchQuery = "";
      this.selectedTag = "";
      this.filterDownloadOnly = false;
      this.applyFilters();
    },
  },
};
</script>

<template>
  <div class="container mt-5">
    <!-- Fixed Search and Download Filter -->
    <div class="container_filters">
      <div class="col-2 filter-bar">
        <div class="flex-grow-1 d-flex">
          <input
            v-model="searchQuery"
            @input="onSearchInput"
            type="text"
            class="form-control me-2"
            placeholder="Search..."
          />
          <button class="btn btn-warning mx-2" @click="resetAllFilters">
            Reset 🔄
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

      <!-- Category Slider -->
      <div class="row">
        <div class="col-12 filter-slider">
          <div class="category-slider d-flex overflow-auto p-2">
            <button
              v-for="group in groupedTags"
              :key="group.category"
              class="btn btn-outline-primary mx-1"
              @click="openCategoryModal(group.category)"
            >
              {{ group.category }}
            </button>
          </div>
        </div>
      </div>
    </div>

    <!-- Collections and Cards -->
    <div v-for="col in filteredCollections" :key="col.name" class="mb-5">
      <h3 class="mb-3">{{ col.name }}</h3>
      <div class="row g-4">
        <div
          v-for="item in col.data"
          :key="item.id"
          class="col-12 col-md-6 col-lg-4"
        >
          <div class="card h-100 shadow-sm">
            <div class="card-body d-flex flex-column">
              <h5 class="card-title text-info">{{ item.title }}</h5>
              <p class="card-text flex-grow-1">{{ item.description }}</p>
              <div v-if="item.download === 1" class="fw-bold mb-2">
                Download: {{ item.download_mode }}
              </div>
              <div class="mb-2">
                <span
                  v-for="tag in item.tags"
                  :key="tag"
                  class="badge bg-info text-dark me-1"
                >
                  {{ tag }}
                </span>
              </div>
              <a
                v-if="item.url"
                :href="item.url"
                target="_blank"
                class="btn btn-primary btn-sm mt-auto"
              >
                Visit Site
              </a>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- Modal for Tags -->
    <div
      v-if="showCategoryModal"
      class="modal fade show"
      tabindex="-1"
      style="display: block; background: rgba(0, 0, 0, 0.5); z-index: 1050"
      @click.self="closeCategoryModal"
    >
      <div class="modal-dialog modal-dialog-scrollable">
        <div class="modal-content">
          <div class="modal-header">
            <h5 class="modal-title">Tags: {{ openedCategory }}</h5>
            <button
              type="button"
              class="btn-close"
              @click="closeCategoryModal"
            ></button>
          </div>
          <div class="modal-body">
            <div v-for="tag in getTagsForOpenedCategory()" :key="tag.id">
              <span
                class="badge bg-info text-dark me-1 mb-1"
                style="cursor: pointer"
                @click="filterByTag(tag.name)"
              >
                {{ tag.name }}
              </span>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- Backdrop -->
    <div
      v-if="showCategoryModal"
      class="modal-backdrop fade show"
      style="z-index: 1040"
    ></div>
  </div>
</template>

<style scoped>
.container_filters {
  background-color: #0e2339;
  position: fixed;
  top: 220px;
  z-index: 999;
}

.category-slider {
  white-space: nowrap;
}
.card {
  border: none;
  background-color: rgb(0, 0, 0);
  color: white;
}

.modal {
  z-index: 1050;
}
.modal-backdrop {
  z-index: 1040;
}
</style>
