<template>
  <div class="flex justify-end items-end">
    <QBtn
      v-if="userData || token"
      class="ma-5"
      label="Cerrar sesión"
      color="red"
      @click="logoutUser" />
  </div>

  <div class="flex justify-center items-center h-screen w-screen">
    <div class="h-full flex items-center">
      <PageView />
    </div>
  </div>
</template>

<script setup lang="ts">
import { isFinished, serverUrl, token, userData, voteData } from '@/store/globals';
import { watch } from 'vue';
import { useRouter } from 'vue-router/auto';

const router = useRouter();

/**
 * Logs out the user
 */
async function logoutUser(): Promise<void> {
  await fetch(`${serverUrl.value}/gateway/authentication/logout`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({
      token: token.value
    })
  });
  token.value = '';
  userData.value = undefined;
}
/**
 * Redirects to the ended page whenever the voting is finished
 */
watch(isFinished, async (value) => {
  if (value) {
    await router.replace(`/voting/${voteData.value.voting.id}/ended`);
  }
});
</script>
