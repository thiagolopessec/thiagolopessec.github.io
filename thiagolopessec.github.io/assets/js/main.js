"use strict";
(function(){
  const translations = {
    pt: {
      bio: "Bem-vindo ao portfólio Blue Team.",
      edu_title: "01. Formação & Certificações"
    },
    en: {
      bio: "Welcome to the Blue Team portfolio.",
      edu_title: "01. Education & Certs"
    }
  };

  const app = {
    lang: localStorage.getItem('lang') || 'pt',
    setLang(lang){
      this.lang = lang; localStorage.setItem('lang', lang);
      document.querySelectorAll('[data-translate]')?.forEach(el => {
        const key = el.getAttribute('data-translate');
        if (translations[this.lang] && translations[this.lang][key]) {
          el.innerHTML = translations[this.lang][key];
        }
      });
    }
  };

  window.app = app;
  document.addEventListener('DOMContentLoaded', function(){ app.setLang(app.lang); });
})();
