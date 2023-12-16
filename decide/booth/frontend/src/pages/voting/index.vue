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
      label="Conectar"
      rounded
      color="primary"
      :loading="loading"
      @click="fetchVoting" />
  </div>
</template>

<script setup lang="ts">
import router from '@/plugins/router';
import { endpointUrl, voteData } from '@/store/globals';
import { ref, watch } from 'vue';
import { useRoute } from 'vue-router/auto';

const id = ref();
const loading = ref(false);
const route = useRoute();

/**
 *
 */
async function fetchVoting(): Promise<void> {
  try {
    loading.value = true;

    if (!('id' in route.params)) {
      throw new TypeError('No parameter id in route');
    }

    const response =
      await fetch(`${endpointUrl.value}/${route.params.id}`, {
        method: 'GET',
        headers: {
          'Content-Type': 'application/json'
        }
      });

      if (response.status === 200) {
        voteData.value = await response.json();
      }
  } catch {} finally {
    loading.value = false;
  }
}

watch(() => route.params, async () => {
  loading.value = true;
  await fetchVoting();
});

watch(voteData, async () => {
  await router.replace(`voting/${voteData.value.id.voting.id}`)
})
</script>
