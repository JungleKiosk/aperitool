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
      searchTimeout: null,
      openedCategory: null,
      showCategoryModal: false,
    };
  },
  created() {
    this.filteredCollections = this.collections;
  },
  methods: {
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

            return matchesSearch && matchesTag;
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
  },
};
</script>

<template>
  <div class="container mt-5">
    <!-- Search Bar -->
    <div class="row mb-4">
      <div class="col-md-6">
        <input
          v-model="searchQuery"
          @input="onSearchInput"
          type="text"
          class="form-control"
          placeholder="Search..."
        />
      </div>
    </div>

    <!-- Category Slider -->
    <div class="row mb-4">
      <div class="col-12">
        <div class="category-slider d-flex overflow-auto py-2 bg-light">
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
              <h5 class="card-title">{{ item.title }}</h5>
              <p class="card-text flex-grow-1">{{ item.description }}</p>
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
      style="display: block; background: rgba(0, 0, 0, 0.5)"
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
            <span
              v-for="group in groupedTags"
              :key="group.category"
              v-if="group.category === openedCategory"
            >
              <span
                v-for="tag in group.tags"
                :key="tag.id"
                class="badge bg-info text-dark me-1 mb-1"
                style="cursor: pointer"
                @click="filterByTag(tag.name)"
              >
                {{ tag.name }}
              </span>
            </span>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.category-slider {
  white-space: nowrap;
}
.card {
  border: none;
}
</style>
