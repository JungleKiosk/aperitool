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
      showCodeModal: false,
      currentTool: null,
    };
  },
  computed: {
    // Unico array con tutti i tag disponibili
    allTags() {
      const set = new Set();
      this.tools.forEach((tool) => {
        tool.tags.forEach((tag) => set.add(tag));
      });
      return Array.from(set);
    },
  },
  methods: {
    // Filtro per ricerca testuale
    onSearchInput() {
      this.filterTools();
    },
    // Filtro per tag
    filterByTag(tag) {
      this.selectedTag = this.selectedTag === tag ? "" : tag;
      this.filterTools();
    },
    // Resetta sia la text‐search che il tag
    resetAllFilters() {
      this.searchQuery = "";
      this.selectedTag = "";
      this.filterTools();
    },
    // Applica davvero il filtro su entrambi
    filterTools() {
      const q = this.searchQuery.toLowerCase();
      this.filteredTools = this.tools.filter((t) => {
        const matchesText =
          t.name.toLowerCase().includes(q) ||
          t.description.toLowerCase().includes(q);
        const matchesTag =
          !this.selectedTag || t.tags.includes(this.selectedTag);
        return matchesText && matchesTag;
      });
    },
    // Apre la finestra modale per vedere il codice
    openCodeModal(tool) {
      this.currentTool = tool;
      this.showCodeModal = true;
    },
    closeCodeModal() {
      this.showCodeModal = false;
      this.currentTool = null;
    },
  },
};
</script>

<template>
  <div class="container mt-5">
    <h1>Tools</h1>

    <!-- Search + Reset -->
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

    <!-- Slider Tag -->
    <div class="d-flex overflow-auto mb-4">
      <button
        v-for="tag in allTags"
        :key="tag"
        class="btn"
        :class="selectedTag === tag ? 'btn-primary' : 'btn-outline-primary'"
        @click="filterByTag(tag)"
      >
        {{ tag }}
      </button>
    </div>

    <!-- Cards -->
    <div class="row g-4">
      <div
        class="col-6 col-md-4 col-lg-3"
        v-for="tool in filteredTools"
        :key="tool.id"
      >
        <div class="card h-100">
          <div class="card-body d-flex flex-column">
            <h5 class="card-title">{{ tool.name }}</h5>
            <p class="card-text flex-grow-1">
              {{ tool.description }}
            </p>
            <div class="mb-2">
              <span
                v-for="t in tool.tags"
                :key="t"
                class="badge bg-info text-dark me-1"
              >
                {{ t }}
              </span>
            </div>
            <button
              class="btn btn-outline-secondary btn-sm mb-1"
              @click="openCodeModal(tool)"
            >
              Vedi Codice
            </button>
            <a
              class="btn btn-primary btn-sm"
              :href="`/tools/${tool.filename}`"
              download
            >
              Scarica .py
            </a>
          </div>
        </div>
      </div>
    </div>

    <!-- Modal Preview Codice -->
    <div
      v-if="showCodeModal"
      class="modal fade show"
      tabindex="-1"
      style="display: block; background: rgba(0, 0, 0, 0.5)"
    >
      <div class="modal-dialog modal-lg">
        <div class="modal-content">
          <div class="modal-header">
            <h5 class="modal-title">{{ currentTool.name }} - Codice</h5>
            <button class="btn-close" @click="closeCodeModal"></button>
          </div>
          <div class="modal-body">
            <pre><code>{{ currentTool.codePreview }}</code></pre>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
