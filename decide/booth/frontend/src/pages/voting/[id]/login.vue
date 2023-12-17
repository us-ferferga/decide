<template>
  <div class="flex justify-center flex-col">
    <h2>Iniciar sesión</h2>
    <QBtn
      class="mt-2 mb-2 pa-2"
      color="primary"
      disable
      :href="`/accounts/github/login/?next=${fullPath}`">
      <IMdiGitHub />
      <div>
        Iniciar sesión con GitHub
      </div>
    </QBtn>
    <hr class="w-full" />
    <QInput
      v-model="user"
      outlined
      label="Usuario" />
    <QInput
      v-model="password"
      outlined
      class="mt-2"
      label="Contraseña" />
    <QBtn
      class="mt-2"
      color="blue"
      rounded
      @click="setSubmit">
      Iniciar sesión
    </QBtn>
  </div>
</template>

<script setup lang="ts">
import { serverUrl, token, userData, voteData } from '@/store/globals';
import { useQuasar } from 'quasar';
import IMdiGitHub from 'virtual:icons/mdi/github';
import { ref, watch } from 'vue';
import { useRouter } from 'vue-router/auto';

const user = ref('');
const password = ref('');
const router = useRouter();
const loading = ref(false);
const quasar = useQuasar();
const fullPath = window.location.href;

/**
 * Submits the login data
 */
async function setSubmit(): Promise<void> {
  try {
    loading.value = true;

    const response = await fetch(`${serverUrl.value}/gateway/authentication/login/`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        username: user.value,
        password: password.value
      })
    });

    const payload = await response.json();

    if (payload.token) {
      token.value = payload.token;
    }

    const responseGetUser = await fetch(`${serverUrl.value}/gateway/authentication/getuser/`,
                                        {
                                          headers:{
                                            'Authorization': `Token ${token.value}`,
                                            'Content-Type': 'application/json'
                                          }
                                        });

    userData.value = await responseGetUser.json();
  } catch {
    quasar.notify({
      message: 'Usuario o contraseña incorrectos',
      color: 'red'
    });
  } finally {
    loading.value = false;
  }
}

/**
 * Runs the middleware logic of the component
 */
async function middleware(): Promise<void> {
  if (userData.value && voteData.value && token.value) {
    await router.replace(`/voting/${voteData.value.voting.id}/answer`);
  } else if (!voteData.value) {
    await router.replace('/voting');
  }
}

watch([userData, voteData], middleware);

await middleware();
</script>
