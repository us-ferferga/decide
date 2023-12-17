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
        v-model="userServerUrl"
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
import { serverUrl } from '@/store/globals';
import { useQuasar } from 'quasar';
import { ref } from 'vue';
import { useRouter } from 'vue-router/auto';

const router = useRouter();
const protocol = ref('http://');
const userServerUrl = ref();
const loading = ref(false);
const options = ['http://', 'https://'];
const quasar = useQuasar();

/**
 * This page simply acts as a middleware
 */
async function fetchApi(): Promise<void> {
  try {
    const response = await fetch(`${serverUrl.value}/api`, {
      method: 'GET',
      headers: {
        'Content-Type': 'application/json'
      }
    });

    if (response.status === 200) {
      await router.replace('/voting');
    }
  } catch {
    quasar.notify({
      message: 'No se ha podido conectar con el servidor',
      color: 'red'
    });
    serverUrl.value = '';
  } finally {
    loading.value = false;
  }
}

/**
 * Connects to the given server
 */
async function connect(): Promise<void> {
  loading.value = true;
  serverUrl.value = `${protocol.value}${serverUrl.value}`;
  await fetchApi();
}

/**
 * This makes this page act as a redirection middleware
 */
await fetchApi();
</script>
