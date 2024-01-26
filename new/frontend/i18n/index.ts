import zh_tw from './zh_tw';
import en_us from './en_us';

export default defineI18nConfig(() => ({
  legacy: false,
  locale: 'zh_tw',
  messages: {
    en_us:en_us,
    zh_tw:zh_tw
  }
}))
