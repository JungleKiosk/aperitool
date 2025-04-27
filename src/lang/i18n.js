import { createI18n } from "vue-i18n";

const messages = {
  en: {
    navbar: {
      home: "Home",
      tools: "Tools",
      links: "Links"
    },
    header: {
      title: "AperiTools"
    },
    home: {
      subtitle: "Test IT lang ",
    },
    about: {
      subtitle: "Test IT lang ",
    }
  },
  it: {
    navbar: {
      home: "home",
      tools: "Tools",
      links: "Links"
    },
    header: {
      title: "AperiTools"
    },
    home: {
      subtitle: "Test EN lang ",
    },
    about: {
      subtitle: "Test EN lang ",
    }
  },
};


const userLocale = localStorage.getItem("language");
const locale = userLocale && ['en', 'it'].includes(userLocale) ? userLocale : 'en';

const i18n = createI18n({
  legacy: false, // Usa API Composition se necessario
  locale: locale, // Lingua principale
  fallbackLocale: "en", // Se una chiave manca, usa l'inglese
  messages,
});

export default i18n;