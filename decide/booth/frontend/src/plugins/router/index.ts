import { useTitle } from '@vueuse/core';
import { computed } from 'vue';
import {
  createRouter,
  createWebHashHistory
} from 'vue-router/auto';
import metaGuard from './middlewares/meta';

const router = createRouter({
  history: createWebHashHistory()
});

/**
 * Middlewares
 */
router.beforeEach(metaGuard);

/**
 * Handle page title changes
 */
const pageTitle = computed(() => {
  const title = router.currentRoute.value.meta.title?.trim();

  return title ? `${title} | Decide: Cabina de votación` : 'Decide: Cabina de votación';
});

useTitle(pageTitle);

export default router;
