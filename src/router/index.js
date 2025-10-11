import { createRouter, createWebHistory } from "vue-router";

import home from "../views/Home.vue";
import linkedin_pages from "../components/linkedin_pages.vue";
import tnkto from "../components/tnkto.vue";
import tools from "../components/main/ToolsMain.vue";
import links from "../components/main/LinksMain.vue";

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: "/",
      name: "home",
      component: home,
    },
    {
      path: "/linkedin_pages",
      name: "linkedin_pages",
      component: linkedin_pages,
    },
    {
      path: "/tnkto",
      name: "tnkto",
      component: tnkto,
    },
    {
      path: "/tools",
      name: "tools",
      component: tools,
    },
    {
      path: "/links",
      name: "links",
      component: links,
    },
  ],
  scrollBehavior(to, from, savedPosition) {
    return { top: 0, behavior: "instant" };
  },
});

export default router;
