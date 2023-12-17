/**
 * Top-level await requires ES2022 (at least) as target and module
 * for TypeScript compiler (check tsconfig.json)
 * https://caniuse.com/mdn-javascript_operators_await_top_level
 */

import Root from '@/App.vue';
import { Notify, Quasar } from 'quasar';
import quasarLang from 'quasar/lang/es';
import { createApp } from 'vue';
/* eslint-disable @typescript-eslint/no-restricted-imports */
import quasarIconSet from '@/plugins/quasar/material-icons';
import router from '@/plugins/router';
/* eslint-enable @typescript-eslint/no-restricted-imports */

/**
 * - GLOBAL STYLES -
 */
import '@/index.css';
import '@fontsource/jost';
import '@unocss/reset/normalize.css';
import '@unocss/reset/sanitize/assets.css';
import '@unocss/reset/sanitize/sanitize.css';
import '@unocss/reset/tailwind.css';
import 'quasar/dist/quasar.css';
import 'virtual:uno.css';


const app = createApp(Root);

app.use(router);
app.use(Quasar, {
  plugins: {
    Notify
  },
  config: {
    brand: {
      primary: '#000000',
      secondary: '#0d8276',
      accent: '#9C27B0',
      dark: '#1d1d1d',
      positive: '#21BA45',
      negative: '#C10015',
      info: '#1a6473',
      warning: '#F2C037'
    }
  },
  lang: quasarLang,
  iconSet: quasarIconSet
});

await router.isReady();
app.mount('#app');
