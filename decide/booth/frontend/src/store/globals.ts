import { useMediaQuery, useNow } from '@vueuse/core';
import { computed, ref } from 'vue';

/**
 * Reactively tracks if the user wants animations (false) or not (true).
 */
export const prefersNoMotion = useMediaQuery('(prefers-reduced-motion)');
export const serverUrl = ref('');
const vote = ref();

export const voteData = computed({
  get() {
    return vote.value ? {
      ...vote.value,
      bigpk: {
        // @ts-expect-error - These are added at runtime
        p: BigInt.fromJSONObject(vote.value.voting.pub_key.p.toString()),
        // @ts-expect-error - These are added at runtime
        g: BigInt.fromJSONObject(vote.value.voting.pub_key.g.toString()),
        // @ts-expect-error - These are added at runtime
        y: BigInt.fromJSONObject(vote.value.voting.pub_key.y.toString())
      }
    } : undefined;
  },
  set(data) {
    if (data.voting.KEYBITS) {
      // @ts-expect-error - These are added at runtime
      ElGamal.BITS = data.voting.KEYBITS;
      vote.value = data;
    }
  }
});

export const userData = ref();
export const token = ref('');
const now = useNow();
export const isFinished = computed(() => {
  if (voteData.value?.voting?.end_date) {
    return now.value > new Date(voteData.value.voting.end_date);
  }

  return false;
});
