<template>
  <div class="flex justify-center flex-col">
    <h6>No se ha encontrado el servidor de Decide. Introduce la URL del servidor a continuación para conectar:</h6>
    <div class="flex flex-row justify-center">
      <QSelect
        v-model="protocol"
        class="flex-1"
        outlined
        :options="options" />
      <QInput
        v-model="serverUrl"
        class="ml-2"
        style="flex: 5;"
        outlined
        label="URL del servidor" />
    </div>
    <QBtn
      class="mt-2"
      label="Conectar"
      rounded
      color="primary"
      :loading="loading"
      @click="connect" />
  </div>
</template>

<script setup lang="ts">
import { endpointUrl } from '@/store/globals';
import { ref } from 'vue';
import { useRouter } from 'vue-router/auto';

const router = useRouter();
const protocol = ref('http://');
const serverUrl = ref();
const loading = ref(false);
const options = ['http://', 'https://'];

/**
 * This page simply acts as a middleware
 */
async function fetchApi(): Promise<void> {
  try {
    const response = await fetch(endpointUrl.value, {
      method: 'GET',
      headers: {
        'Content-Type': 'application/json'
      }
    });

    if (response.status === 200) {
      await router.replace('/voting');
    }
  } catch {} finally {
    loading.value = false;
  }
}

/**
 *
 */
async function connect(): Promise<void> {
  loading.value = true;
  endpointUrl.value = `${protocol.value}${serverUrl.value}`;
  await fetchApi();
}

/**
 * This makes this page act as a redirection middleware
 */
await fetchApi();
</script>
