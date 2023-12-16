<template>
  <Transition
    v-if="!prefersNoMotion"
    mode="out-in">
    <!-- This div is required because <transition> requires a single children node -->
    <div
      :key="transitionKey"
      v-bind="$attrs"
      style="transform-origin: center">
      <slot />
    </div>
  </Transition>
  <slot v-else />
</template>

<script setup lang="ts">
import { prefersNoMotion } from '@/store/globals';

defineProps<{
  transitionKey: string;
}>();
</script>

<style scoped>
.v-enter-active,
.v-leave-active {
  transition-duration: 0.3s ease !important;
  transition-property: transform, opacity !important;
  transition-timing-function: cubic-bezier(0.4, 0, 0.2, 1) !important;
}

.v-leave-to {
  opacity: 0;
  transform: translateX(-15px);
}

.v-enter-from {
  opacity: 0;
  transform: translateX(15px);
}
</style>
