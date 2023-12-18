<template>
  <div class="flex justify-center flex-col">
    <h2>Esta votación ya ha finalizado</h2>
  </div>
</template>

<script setup lang="ts">
import { isFinished } from '@/store/globals';
import { watch } from 'vue';
import { useRouter } from 'vue-router/auto';

const router = useRouter();

/**
 * Acts as a middleware for the page
 */
async function middleware(): Promise<void> {
  if (!isFinished.value) {
    await router.replace('/');
  }
}

watch(isFinished, middleware);
await middleware();
</script>
