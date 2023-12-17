import { Notify, QuasarPluginOptions } from 'quasar';
import quasarLang from 'quasar/lang/es';
import quasarIconSet from './material-icons';

export default {
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
} as Partial<QuasarPluginOptions>;
