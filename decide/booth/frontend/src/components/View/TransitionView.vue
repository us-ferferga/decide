<template>
  <Transition
    v-if="!prefersNoMotion"
    name="scroll-x-reverse-transition"
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
.slide-y-transition-move {
    transition-property: transform!important;
    transition-duration: .5s!important;
    transition-timing-function: cubic-bezier(.4,0,.2,1)!important
}

.slide-y-transition-enter-from,.slide-y-transition-leave-to {
    opacity: 0;
    transform: translateY(-15px)
}

.slide-y-transition-enter-active,.slide-y-transition-leave-active {
  transition-duration: .3s!important;
    transition-timing-function: cubic-bezier(.4,0,.2,1)!important;
    transition-property: transform,opacity!important
}

.slide-y-reverse-transition-move {
    transition-property: transform!important;
    transition-duration: .5s!important;
    transition-timing-function: cubic-bezier(.4,0,.2,1)!important
}

.slide-y-reverse-transition-enter-from,.slide-y-reverse-transition-leave-to {
    opacity: 0;
    transform: translateY(15px)
}

.slide-y-reverse-transition-enter-active,.slide-y-reverse-transition-leave-active {
  transition-duration: .3s!important;
    transition-timing-function: cubic-bezier(.4,0,.2,1)!important;
    transition-property: transform,opacity!important
}

.scroll-y-transition-move {
    transition-property: transform!important;
    transition-duration: .5s!important;
    transition-timing-function: cubic-bezier(.4,0,.2,1)!important
}

.scroll-y-transition-enter-from,.scroll-y-transition-leave-to {
    opacity: 0
}

.scroll-y-transition-enter-from {
    transform: translateY(-15px)
}

.scroll-y-transition-leave-to {
    transform: translateY(15px)
}

.scroll-y-transition-enter-active,.scroll-y-transition-leave-active {
    transition-property: transform,opacity!important;
    transition-duration: .3s!important;
    transition-timing-function: cubic-bezier(.4,0,.2,1)!important;
}

.scroll-y-reverse-transition-move {
    transition-property: transform!important;
    transition-duration: .5s!important;
    transition-timing-function: cubic-bezier(.4,0,.2,1)!important
}

.scroll-y-reverse-transition-enter-from,.scroll-y-reverse-transition-leave-to {
    opacity: 0
}

.scroll-y-reverse-transition-enter-from {
    transform: translateY(15px)
}

.scroll-y-reverse-transition-leave-to {
    transform: translateY(-15px)
}

.scroll-y-reverse-transition-enter-active,.scroll-y-reverse-transition-leave-active {
    transition-property: transform,opacity!important;
    transition-duration: .3s!important;
    transition-timing-function: cubic-bezier(.4,0,.2,1)!important;
}

.scroll-x-transition-move {
    transition-property: transform!important;
    transition-duration: .5s!important;
    transition-timing-function: cubic-bezier(.4,0,.2,1)!important
}

.scroll-x-transition-enter-from,.scroll-x-transition-leave-to {
    opacity: 0
}

.scroll-x-transition-enter-from {
    transform: translate(-15px)
}

.scroll-x-transition-leave-to {
    transform: translate(15px)
}

.scroll-x-transition-enter-active,.scroll-x-transition-leave-active {
  transition-duration: .3s!important;
    transition-timing-function: cubic-bezier(.4,0,.2,1)!important;
    transition-property: transform,opacity!important
}

.scroll-x-reverse-transition-move {
    transition-property: transform!important;
    transition-duration: .5s!important;
    transition-timing-function: cubic-bezier(.4,0,.2,1)!important
}

.scroll-x-reverse-transition-enter-from,.scroll-x-reverse-transition-leave-to {
    opacity: 0
}

.scroll-x-reverse-transition-enter-from {
    transform: translate(15px)
}

.scroll-x-reverse-transition-leave-to {
    transform: translate(-15px)
}

.scroll-x-reverse-transition-enter-active,.scroll-x-reverse-transition-leave-active {
  transition-duration: .3s!important;
    transition-timing-function: cubic-bezier(.4,0,.2,1)!important;
    transition-property: transform,opacity!important
}

.slide-x-transition-move {
    transition-property: transform!important;
    transition-duration: .5s!important;
    transition-timing-function: cubic-bezier(.4,0,.2,1)!important
}

.slide-x-transition-enter-from,.slide-x-transition-leave-to {
    opacity: 0;
    transform: translate(-15px)
}

.slide-x-transition-enter-active,.slide-x-transition-leave-active {
  transition-duration: .3s!important;
    transition-timing-function: cubic-bezier(.4,0,.2,1)!important;
    transition-property: transform,opacity!important
}

.slide-x-reverse-transition-move {
    transition-property: transform!important;
    transition-duration: .5s!important;
    transition-timing-function: cubic-bezier(.4,0,.2,1)!important
}

.slide-x-reverse-transition-enter-from,.slide-x-reverse-transition-leave-to {
    opacity: 0;
    transform: translate(15px)
}

.slide-x-reverse-transition-enter-active,.slide-x-reverse-transition-leave-active {
  transition-duration: .3s!important;
    transition-timing-function: cubic-bezier(.4,0,.2,1)!important;
    transition-property: transform,opacity!important
}

.fade-transition-move {
    transition-property: transform!important;
    transition-duration: .5s!important;
    transition-timing-function: cubic-bezier(.4,0,.2,1)!important
}

.fade-transition-enter-from,.fade-transition-leave-to {
    opacity: 0!important
}

.fade-transition-enter-active,.fade-transition-leave-active {
    transition-property: opacity!important;
    transition-duration: .3s!important;
    transition-timing-function: cubic-bezier(.4,0,.2,1)!important
}
</style>
