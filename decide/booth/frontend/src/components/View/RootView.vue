<template>
  <TransitionView :transition-key="route.meta.layout">
    <SuspenseView>
      <DefaultLayout />
    </SuspenseView>
  </TransitionView>
</template>

<script setup lang="ts">
import DefaultLayout from '@/layouts/default.vue';
import { useRoute } from 'vue-router/auto';

const route = useRoute();
</script>
