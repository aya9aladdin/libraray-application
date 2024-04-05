import { createRouter, createWebHistory } from "vue-router";
import AppHeader from "../components/books.vue";
const routes = [
  {
    path: "/",
    name: "booksApp",
    component: AppHeader,
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;
