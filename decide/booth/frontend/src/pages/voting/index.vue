<template>
  <div class="flex justify-center flex-col">
    <h6>No se ha encontrado el identificador de la votación. Introdúcelo a continuación</h6>
    <QInput
      v-model="id"
      outlined
      type="number"
      label="Identificador de la votación" />

    <QBtn
      class="mt-2"
      label="Continuar"
      rounded
      color="primary"
      :loading="loading"
      @click="async () => fetchVoting()" />
  </div>
</template>

<script setup lang="ts">
import { serverUrl, voteData } from '@/store/globals';
import { useQuasar } from 'quasar';
import { ref, watch } from 'vue';
import { useRoute, useRouter } from 'vue-router/auto';

const id = ref();
const loading = ref(false);
const route = useRoute();
const router = useRouter();
const quasar = useQuasar();

/**
 * Gets the voting data from the server, from params or the user input
 *
 * @param load - Check for parameters in the ID
 */
async function fetchVoting(paramCheck = false): Promise<void> {
  try {
    loading.value = true;

    if (!('id' in route.params) && paramCheck) {
      throw new TypeError('No parameter id in route');
    }

    const response =
      await fetch(`${serverUrl.value}/api/${paramCheck ? (route.params as { id: string }).id : id.value}`, {
        method: 'GET',
        headers: {
          'Content-Type': 'application/json'
        }
      });

    if (response.status === 200) {
      const payload = await response.json();

      if (payload.voting.id) {
        voteData.value = await response.json();
      }
    }

    throw new Error();
  } catch {
    quasar.notify({
      message: 'Votación no encontrada',
      color: 'red'
    });
  } finally {
    loading.value = false;
  }
}

/**
 * Runs the redirection logic and middleware
 */
async function redirect(): Promise<void> {
  if (voteData.value.voting?.end_date && Date.parse(voteData.value.voting.end_date) < Date.now()) {
    await router.replace(`/voting/${voteData.value.voting.id}/ended`);
  } else if (voteData.value) {
    await router.replace(`/voting/${voteData.value.id.voting.id}/login`);
  }
}

watch(() => route.params, async () => {
  loading.value = true;
  await fetchVoting(true);
});

watch(voteData, redirect);

await fetchVoting(true);
await redirect();
</script>
