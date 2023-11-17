import { computed } from 'vue';
import {
  createRouter,
  createWebHashHistory
} from 'vue-router/auto';
import { useTitle } from '@vueuse/core';

const router = createRouter({
  history: createWebHashHistory()
});

/**
 * Handle page title changes
 */
const pageTitle = computed(() => {
  const title = router.currentRoute.value.meta.title?.trim();

  return title ? `${title} | Decide: Cabina de votación` : 'Decide: Cabina de votación';
});

useTitle(pageTitle);

export default router;
