<template>
  <div class="flex justify-center flex-col">
    <h2>{{ voteData.voting.name }}</h2>
    <h1 class="text-subtitle1">
      {{ voteData.voting.question.desc }}
    </h1>
    <QForm class="flex flex-col">
      <template
        v-for="opt, index in voteData.voting.question.options"
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
        @click="selection = undefined">
        Restablecer respuesta
      </QBtn>
      <QBtn
        class="mt-2"
        color="green"
        rounded
        @click.prevent="submit">
        Enviar
      </QBtn>
    </div>
  </div>
</template>

<script setup lang="ts">
import { serverUrl, token, userData, voteData } from '@/store/globals';
import { ref } from 'vue';
import { useRouter } from 'vue-router/auto';

const selection = ref();
const router = useRouter();
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
    const cipher = ElGamal.encrypt(voteData.value.voting.bigPk, bigmsg);
    const data = {
      vote: {a: cipher.alpha.toString(), b: cipher.beta.toString()},
      voting: voteData.value.voting.id,
      voter: userData.value.id,
      token: token.value
    };

    await fetch(`${serverUrl.value}/gateway/store/`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'Authorization': `Token ${token.value}`
      },
      body: JSON.stringify(data)
    });

    await router.replace(`/voting/${voteData.value.voting.id}/thankyou`);
  } catch {} finally {
    loading.value = false;
  }

}
</script>
