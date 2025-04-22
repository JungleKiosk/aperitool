<script>
import linksData from '../../data/links.json';
import { groupedTags } from '../../data/tags.js';

export default {
  name: 'LinksView',
  data() {
    return {
      searchQuery: '',
      links: linksData,
      filteredLinks: linksData,
      groupedTags,
      selectedTag: '',
      selectedStato: '',
      selectedCu: '',
      selectedInspire: '',
      selectedInspireDetails: null,
      showModal: false,
      stati: [
        'Noti e Accessibili',
        'Noti ma non accessibili',
        'Non Noti'
      ],
      debounceTimeout: null,
      tagSearchQuery: '',
      openedCategory: null,
      showCategoryModal: false,
      sidebarOpen: false
    };
  },
  created() {
    fetch('/src/data/links.json')
      .then(response => response.json())
      .then(data => {
        this.links = data;
        this.filteredLinks = data;
      })
      .catch(error => console.error('Errore nel caricamento dei dati:', error));
  },
  methods: {
    openCategoryModal(category) {
      this.openedCategory = category;
      this.showCategoryModal = true;
    },
    closeCategoryModal() {
      this.showCategoryModal = false;
      this.openedCategory = null;
    },
    toggleSidebar() {
      this.sidebarOpen = !this.sidebarOpen;
    },
    debounceFilter() {
      if (this.debounceTimeout) {
        clearTimeout(this.debounceTimeout);
      }
      this.debounceTimeout = setTimeout(() => {
        this.filterLinks();
      }, 800);
    },
    onSearchInput() {
      this.selectedTag = '';
      this.debounceFilter();
    },
    filterLinks() {
      const query = this.searchQuery.toLowerCase();
      this.filteredLinks = this.links.filter(link => {
        const matchesQuery =
          link.title.toLowerCase().includes(query) ||
          link.description.toLowerCase().includes(query) ||
          link.tags.some(tag => tag.toLowerCase().includes(query));

        const matchesTag = !this.selectedTag || link.tags.includes(this.selectedTag);
        const matchesStato = !this.selectedStato || link.stato === this.selectedStato;
        const matchesCu =
          !this.selectedCu ||
          (Array.isArray(link.cu)
            ? link.cu.includes(this.selectedCu)
            : link.cu === this.selectedCu);
        const matchesInspire =
          !this.selectedInspire ||
          (Array.isArray(link.inspire)
            ? link.inspire.includes(this.selectedInspire)
            : link.inspire === this.selectedInspire);

        return (
          matchesQuery &&
          matchesTag &&
          matchesStato &&
          matchesCu &&
          matchesInspire
        );
      });
    },
    filterByTag(tag) {
      this.searchQuery = '';
      this.selectedTag = this.selectedTag === tag ? '' : tag;
      this.filterLinks();
    },
    onStatoChange() {
      this.filterLinks();
    },
    resetSearchQuery() {
      this.searchQuery = '';
      this.filterLinks();
    },
    resetSelectedStato() {
      this.selectedStato = '';
      this.filterLinks();
    },
    resetSelectedCu() {
      this.selectedCu = '';
      this.filterLinks();
    },
    resetSelectedInspire() {
      this.selectedInspire = '';
      this.filterLinks();
    },
    resetAllFilters() {
      this.searchQuery = '';
      this.selectedStato = '';
      this.selectedCu = '';
      this.selectedInspire = '';
      this.filterLinks();
    },
    openInspireModal(inspire) {
      const found = inspireData.find(item => item.term === inspire);
      if (found) {
        this.selectedInspireDetails = found;
        this.showModal = true;
      }
    },
    closeInspireModal() {
      this.showModal = false;
      this.selectedInspireDetails = null;
    }
  },
  computed: {
    uniqueCu() {
      const cuValues = new Set();
      this.links.forEach(link => {
        if (Array.isArray(link.cu)) {
          link.cu.forEach(cu => cuValues.add(cu));
        } else {
          cuValues.add(link.cu);
        }
      });
      return Array.from(cuValues);
    },
    uniqueInspire() {
      const inspireValues = new Set();
      this.links.forEach(link => {
        if (Array.isArray(link.inspire)) {
          link.inspire.forEach(ins => inspireValues.add(ins));
        } else {
          inspireValues.add(link.inspire);
        }
      });
      return Array.from(inspireValues);
    }
  }
};
</script>

<template>
  <div class="container-fluid text-black mt-5">
    <!-- Toggle Sidebar Button -->
    <button class="btn btn-primary toggle-btn" @click="toggleSidebar">
      ☰ Filtri
    </button>

    <!-- Category Slider -->
    <div class="row mt-4">
      <div class="category-slider d-flex overflow-auto py-2 bg-light w-100">
        <button
          v-for="group in groupedTags"
          :key="group.category"
          class="btn btn-outline-primary mx-1 flex-shrink-0"
          @click="openCategoryModal(group.category)"
        >
          {{ group.category }}
        </button>
      </div>
    </div>

    <!-- Sidebar Filters -->
    <div class="sidebar margin_top_sidbar p-4" :class="{ open: sidebarOpen }">
      <div class="d-flex justify-content-between align-items-center mb-3">
        <span class="btn btn-secondary" @click="resetAllFilters">Cancella filtri &#8634;</span>
        <button class="btn btn-sm btn-outline-secondary" @click="toggleSidebar">✕</button>
      </div>
      <p><em>ATTENZIONE: i filtri sono incrociati!</em></p>

      <!-- Search -->
      <div class="mb-4">
        <h6>Filtra Parola</h6>
        <div class="input-group">
          <input
            type="text"
            class="form-control"
            v-model="searchQuery"
            placeholder="Cerca..."
            @input="onSearchInput"
          />
          <button class="btn btn-outline-secondary" type="button" @click="resetSearchQuery">&#8634;</button>
        </div>
      </div>

      <!-- Stato -->
      <div class="mb-4">
        <h6>Filtra Stato</h6>
        <div class="input-group">
          <select class="form-select" v-model="selectedStato" @change="onStatoChange">
            <option value="">Tutti gli stati</option>
            <option v-for="stato in stati" :key="stato" :value="stato">{{ stato }}</option>
          </select>
          <button class="btn btn-outline-secondary" type="button" @click="resetSelectedStato">&#8634;</button>
        </div>
      </div>

      <!-- CU -->
      <div class="mb-4">
        <h6>Filtra CU</h6>
        <div class="input-group">
          <select class="form-select" v-model="selectedCu" @change="filterLinks">
            <option value="">Tutti i CU</option>
            <option v-for="cu in uniqueCu" :key="cu" :value="cu">{{ cu }}</option>
          </select>
          <button class="btn btn-outline-secondary" type="button" @click="resetSelectedCu">&#8634;</button>
        </div>
      </div>
    </div>

    <!-- Main Content Area -->
    <div class="content-area mt-5">
      <div class="row g-4">
        <div class="col-6 col-md-4 col-lg-2" v-for="link in filteredLinks" :key="link.id">
          <div class="card h-100 shadow-sm">
            <div class="card-body d-flex flex-column">
              <h5 class="card-title">{{ link.title }}</h5>
              <p class="card-text flex-grow-1">{{ link.description }}</p>
              <a
                v-if="link.url"
                :href="link.url"
                target="_blank"
                class="btn btn-primary btn-sm mt-2"
              >Visita Sito</a>
              <p v-else class="text-muted mt-2">N/A</p>
              <p class="mt-2 mb-1">
                <strong>Note:</strong>
                <span class="badge bg-secondary">{{ link.cu }}</span>
              </p>
              <div>
                <strong>Tags:</strong>
                <span
                  v-for="tag in link.tags"
                  :key="tag"
                  class="badge bg-info text-dark me-1"
                >
                  {{ tag }}
                </span>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- Category Modal -->
    <div
      v-if="showCategoryModal"
      class="modal fade show"
      tabindex="-1"
      style="display: block; background: rgba(0,0,0,0.5);"
    >
      <div class="modal-dialog modal-dialog-scrollable">
        <div class="modal-content">
          <div class="modal-header">
            <h5 class="modal-title">Tags: {{ openedCategory }}</h5>
            <button type="button" class="btn-close" @click="closeCategoryModal"></button>
          </div>
          <div class="modal-body">
            <span
              v-for="tag in groupedTags.find(g => g.category === openedCategory).tags"
              :key="tag.id"
              class="badge bg-info text-dark me-1 mb-1"
              style="cursor: pointer;"
              @click="filterByTag(tag.name); closeCategoryModal()"
            >
              {{ tag.name }}
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
.margin_top_sidbar {
  margin-top: 4rem;
}
.sidebar {
  position: fixed;
  top: 0;
  left: -350px;
  width: 300px;
  height: 100%;
  background-color: rgba(99, 177, 255, 0.9);
  transition: left 0.3s ease;
  z-index: 1050;
  overflow-y: auto;
}
.sidebar.open {
  left: 0;
}
.toggle-btn {
  position: fixed;
  top: 1rem;
  right: 1rem;
  z-index: 1100;
}
.card {
  border: none;
}
</style>
