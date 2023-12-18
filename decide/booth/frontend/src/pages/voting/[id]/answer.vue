<template>
  <div class="flex justify-center flex-col">
    <h2 v-if="voteData?.voting?.name">
      {{ voteData.voting.name }}
    </h2>
    <h2
      v-if="voteData?.voting?.desc"
      class="text-subtitle1">
      {{ voteData.voting.desc }}
    </h2>
    <h3
      v-if="voteData?.voting?.question?.desc"
      class="text-subtitle2">
      {{ voteData.voting.question.desc }}
    </h3>
    <QForm class="flex flex-col">
      <template
        v-for="opt, index in voteData?.voting.question.options"
        :key="`${opt.number}-${index}`">
        <QRadio
          v-model="selection"
          class="mt-2 mb-2"
          dense
          :val="opt.number"
          :label="opt.option" />
      </template>
    </QForm>
    <div class="flex flex-row justify-between">
      <QBtn
        class="mt-2 text-black"
        color="yellow"
        rounded
        :disable="loading"
        @click="selection = undefined">
        Restablecer respuesta
      </QBtn>
      <QBtn
        class="mt-2"
        color="green"
        rounded
        :loading="loading"
        @click.prevent="submit">
        Enviar
      </QBtn>
    </div>
  </div>
</template>

<script setup lang="ts">
import { serverUrl, token, userData, voteData } from '@/store/globals';
import { useQuasar } from 'quasar';
import { ref, watch } from 'vue';
import { useRouter } from 'vue-router/auto';

const selection = ref();
const router = useRouter();
const quasar = useQuasar();
const loading = ref(false);

/**
 * Submits the form data
 */
async function submit(): Promise<void> {
  try {
    loading.value = true;

    // @ts-expect-error - Added at runtime
    const bigmsg = BigInt.fromJSONObject(selection.value.toString());
    // @ts-expect-error - Added at runtime
    // eslint-disable-next-line no-undef
    const cipher = ElGamal.encrypt(voteData.value.voting.bigpk, bigmsg);
    const data = {
      vote: {a: cipher.alpha.toString(), b: cipher.beta.toString()},
      voting: voteData.value?.voting.id,
      voter: userData.value.id,
      token: token.value
    };

    const responsePost = await fetch(`${serverUrl.value}/gateway/store/`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'Authorization': `Token ${token.value}`
      },
      body: JSON.stringify(data)
    });

    if (responsePost.status === 200) {
      await router.replace(`/voting/${voteData.value?.voting.id}/thankyou`);
    } else {
      throw new Error();
    }
  } catch {
    quasar.notify({
      message: 'Error al enviar la votación',
      color: 'red'
    });
  } finally {
    loading.value = false;
  }
}

/**
 * Acts as a middleware for the page
 */
async function middleware(): Promise<void> {
  if (!token.value || !userData.value || !voteData.value) {
    await router.replace('/');
  }
}

watch([serverUrl, token, userData, voteData], middleware);
await middleware();
</script>
