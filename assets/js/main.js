/* =========================================================
   Elbatec Controle de Pragas — main.js
   JavaScript puro, sem dependências.
   ========================================================= */
(function () {
  'use strict';

  /* ---------------------------------------------------------
     CONFIGURAÇÃO — PERSONALIZAR AQUI
     whatsapp: somente números, com 55 + DDD + número.
     IMPORTANTE: o número também aparece fixo nos links do HTML
     (procure por 5511000000000 e substitua em todos os arquivos).
     --------------------------------------------------------- */
  var CONFIG = {
    whatsapp: '5511000000000', // PREENCHER: número do WhatsApp (ex.: 5511912345678)
    mensagemPadrao: 'Olá! Vim pelo site e gostaria de um orçamento.',
    usarFormspree: false,       // true = envia formulário por e-mail via Formspree
    formspreeId: 'SEU_ID_FORMSPREE' // PREENCHER: ex.: xyzabcd (https://formspree.io)
  };

  document.documentElement.classList.remove('no-js');

  function waLink(msg) {
    return 'https://wa.me/' + CONFIG.whatsapp + '?text=' + encodeURIComponent(msg || CONFIG.mensagemPadrao);
  }

  /* ---------- Rastreamento de conversões (GA4 / Ads / GTM) ---------- */
  // As tags ficam comentadas no <head> de cada página. Quando ativadas,
  // esta função envia os eventos para dataLayer (GTM) e gtag (GA4/Ads).
  function track(evento, dados) {
    dados = dados || {};
    try {
      window.dataLayer = window.dataLayer || [];
      window.dataLayer.push(Object.assign({ event: evento }, dados));
      if (typeof window.gtag === 'function') {
        window.gtag('event', evento, dados);
        // PREENCHER: conversão do Google Ads (descomente e troque AW-XXXXXXXXX/YYYYYYYY)
        // window.gtag('event', 'conversion', { send_to: 'AW-XXXXXXXXX/YYYYYYYY' });
      }
    } catch (e) { /* silencioso */ }
  }
  window.elbatecTrack = track;

  /* ---------- Links de WhatsApp ---------- */
  document.querySelectorAll('a.js-wa').forEach(function (a) {
    a.href = waLink(a.getAttribute('data-msg'));
    a.setAttribute('target', '_blank');
    a.setAttribute('rel', 'noopener');
  });
  document.addEventListener('click', function (ev) {
    var a = ev.target.closest && ev.target.closest('a');
    if (!a) return;
    var href = a.getAttribute('href') || '';
    if (href.indexOf('wa.me') > -1) track('clique_whatsapp', { link_url: href });
    else if (href.indexOf('tel:') === 0) track('clique_telefone', { link_url: href });
  });

  /* ---------- Menu mobile ---------- */
  var toggle = document.querySelector('.nav-toggle');
  var nav = document.getElementById('menu-principal');
  if (toggle && nav) {
    var setMenu = function (open) {
      toggle.setAttribute('aria-expanded', String(open));
      toggle.setAttribute('aria-label', open ? 'Fechar menu' : 'Abrir menu');
      nav.classList.toggle('is-open', open);
      document.body.classList.toggle('nav-open', open);
    };
    toggle.addEventListener('click', function () {
      setMenu(toggle.getAttribute('aria-expanded') !== 'true');
    });
    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && toggle.getAttribute('aria-expanded') === 'true') { setMenu(false); toggle.focus(); }
    });
    nav.querySelectorAll('a').forEach(function (a) { a.addEventListener('click', function () { setMenu(false); }); });
    window.addEventListener('resize', function () { if (window.innerWidth >= 1024) setMenu(false); });
  }

  /* ---------- Ano automático ---------- */
  document.querySelectorAll('.js-year').forEach(function (el) { el.textContent = new Date().getFullYear(); });

  /* ---------- Voltar ao topo ---------- */
  var topBtn = document.querySelector('.to-top');
  if (topBtn) {
    var onScroll = function () { topBtn.classList.toggle('is-visible', window.scrollY > 600); };
    window.addEventListener('scroll', onScroll, { passive: true });
    onScroll();
    topBtn.addEventListener('click', function () {
      var reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
      window.scrollTo({ top: 0, behavior: reduce ? 'auto' : 'smooth' });
      var skip = document.getElementById('conteudo');
      if (skip) { skip.setAttribute('tabindex', '-1'); skip.focus({ preventScroll: true }); }
    });
  }

  /* ---------- Animações ao rolar ---------- */
  var reveals = document.querySelectorAll('.reveal');
  var reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  if (!reduceMotion && 'IntersectionObserver' in window) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (en.isIntersecting) { en.target.classList.add('is-visible'); io.unobserve(en.target); }
      });
    }, { rootMargin: '0px 0px -8% 0px', threshold: 0.08 });
    reveals.forEach(function (el) { io.observe(el); });
  } else {
    reveals.forEach(function (el) { el.classList.add('is-visible'); });
  }

  /* ---------- Banner de cookies (LGPD) ---------- */
  var COOKIE_KEY = 'elbatec_consent';
  function getConsent() { try { return localStorage.getItem(COOKIE_KEY); } catch (e) { return null; } }
  function setConsent(v) { try { localStorage.setItem(COOKIE_KEY, v); } catch (e) { /* modo privado */ } }
  function aplicarConsentimento(v) {
    // Se usar Google Consent Mode v2, atualize aqui:
    if (typeof window.gtag === 'function') {
      window.gtag('consent', 'update', {
        analytics_storage: v === 'aceito' ? 'granted' : 'denied',
        ad_storage: v === 'aceito' ? 'granted' : 'denied',
        ad_user_data: v === 'aceito' ? 'granted' : 'denied',
        ad_personalization: v === 'aceito' ? 'granted' : 'denied'
      });
    }
  }
  var banner = document.querySelector('.cookie-banner');
  var consent = getConsent();
  if (consent) aplicarConsentimento(consent);
  if (banner && !consent) {
    banner.hidden = false;
    banner.querySelector('[data-consent="aceito"]').addEventListener('click', function () { setConsent('aceito'); aplicarConsentimento('aceito'); banner.hidden = true; });
    banner.querySelector('[data-consent="recusado"]').addEventListener('click', function () { setConsent('recusado'); aplicarConsentimento('recusado'); banner.hidden = true; });
  }

  /* ---------- Formulários (orçamento e contato) ---------- */
  var regexEmail = /^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/;
  function soDigitos(v) { return (v || '').replace(/\D/g, ''); }

  function validarCampo(campo) {
    var erroEl = document.getElementById(campo.id + '-erro');
    var msg = '';
    var v = (campo.type === 'checkbox') ? campo.checked : campo.value.trim();
    if (campo.required && (campo.type === 'checkbox' ? !v : !v)) {
      msg = campo.type === 'checkbox' ? 'É preciso aceitar a Política de Privacidade.' : 'Preencha este campo.';
    } else if (campo.type === 'email' && v && !regexEmail.test(v)) {
      msg = 'Informe um e-mail válido.';
    } else if (campo.type === 'tel' && v) {
      var d = soDigitos(v);
      if (d.length < 10 || d.length > 13) msg = 'Informe telefone com DDD (ex.: 11 91234-5678).';
    } else if (campo.name === 'area' && v && (isNaN(Number(v)) || Number(v) < 0)) {
      msg = 'Informe um número válido.';
    }
    campo.setAttribute('aria-invalid', msg ? 'true' : 'false');
    if (erroEl) erroEl.textContent = msg;
    return !msg;
  }

  // Máscara simples de telefone
  document.querySelectorAll('input[type="tel"]').forEach(function (inp) {
    inp.addEventListener('input', function () {
      var d = soDigitos(inp.value).slice(0, 11);
      var f = d;
      if (d.length > 2) f = '(' + d.slice(0, 2) + ') ' + d.slice(2);
      if (d.length > 7) f = '(' + d.slice(0, 2) + ') ' + d.slice(2, d.length - 4) + '-' + d.slice(-4);
      inp.value = f;
    });
  });

  document.querySelectorAll('form[data-form]').forEach(function (form) {
    var status = form.querySelector('.form-status');
    var campos = form.querySelectorAll('input, select, textarea');
    campos.forEach(function (c) {
      c.addEventListener('blur', function () { if (c.value || c.type === 'checkbox') validarCampo(c); });
    });

    form.addEventListener('submit', function (ev) {
      ev.preventDefault();
      // Honeypot anti-spam
      var hp = form.querySelector('input[name="_gotcha"]');
      if (hp && hp.value) return;

      var ok = true, primeiroInvalido = null;
      campos.forEach(function (c) {
        if (c.name === '_gotcha' || c.type === 'hidden' || c.type === 'submit') return;
        if (!validarCampo(c)) { ok = false; if (!primeiroInvalido) primeiroInvalido = c; }
      });
      if (!ok) {
        status.className = 'form-status erro';
        status.textContent = 'Confira os campos destacados.';
        primeiroInvalido.focus();
        return;
      }

      var tipo = form.getAttribute('data-form');
      var linhas = [tipo === 'orcamento' ? '*Pedido de orçamento — site Elbatec*' : '*Contato pelo site Elbatec*', ''];
      campos.forEach(function (c) {
        if (!c.name || c.name === '_gotcha' || c.type === 'checkbox' || c.type === 'submit') return;
        var val = c.tagName === 'SELECT' ? (c.options[c.selectedIndex] || {}).text : c.value.trim();
        if (!val || (c.tagName === 'SELECT' && c.value === '')) return;
        var label = c.getAttribute('data-label') || c.name;
        if (c.name === 'area') val += ' m²';
        linhas.push('*' + label + ':* ' + val);
      });
      linhas.push('', 'Aceito a Política de Privacidade.');
      var mensagem = linhas.join('\n');

      track(tipo === 'orcamento' ? 'envio_orcamento' : 'envio_contato', { form_id: tipo });

      if (CONFIG.usarFormspree) {
        /* ---- Envio alternativo por e-mail via Formspree ----
           1. Crie conta em https://formspree.io e um formulário.
           2. Coloque o ID em CONFIG.formspreeId e usarFormspree: true. */
        status.className = 'form-status';
        status.textContent = 'Enviando...';
        fetch('https://formspree.io/f/' + CONFIG.formspreeId, {
          method: 'POST',
          headers: { 'Accept': 'application/json' },
          body: new FormData(form)
        }).then(function (r) {
          if (!r.ok) throw new Error('falha');
          status.className = 'form-status ok';
          status.textContent = 'Recebemos sua mensagem! Retornaremos em breve.';
          form.reset();
        }).catch(function () {
          status.className = 'form-status erro';
          status.textContent = 'Não foi possível enviar. Tente pelo WhatsApp ou telefone (11) 3232-2206.';
        });
        return;
      }

      // Padrão: abre o WhatsApp com a mensagem formatada
      var url = waLink(mensagem);
      var win = window.open(url, '_blank', 'noopener');
      if (!win) window.location.href = url;
      status.className = 'form-status ok';
      status.textContent = 'Abrimos o WhatsApp com seus dados. É só tocar em "Enviar" na conversa.';
    });
  });
})();
