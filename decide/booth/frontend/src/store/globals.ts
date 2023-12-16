import { useMediaQuery } from '@vueuse/core';
import { computed, ref } from 'vue';

/**
 * Reactively tracks if the user wants animations (false) or not (true).
 */
export const prefersNoMotion = useMediaQuery('(prefers-reduced-motion)');
const serverUrl = ref('');
export const endpointUrl = computed({
  get() {
    return serverUrl.value ? `${serverUrl.value}/booth/api/` : '/api';
  },
  set(value: string) {
    serverUrl.value = value;
  }
});

export const voteData = ref();
