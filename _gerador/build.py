#!/usr/bin/env python3
"""
Gerador do site estático da Tango Fantasias.

USO (opcional — o site já vem gerado):
  1. Edite o bloco CONFIG abaixo (domínio, e-mail, horário, redes sociais...).
  2. Rode:  python3 build.py   (Python 3.12+)
  3. Os arquivos são gravados na pasta-mãe (raiz do site).
Se editar os .html à mão, não rode o gerador depois (ele sobrescreve as páginas).
"""
import json, os, re, datetime, html
from urllib.parse import quote

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.dirname(HERE)

# =====================================================================
# CONFIG — PERSONALIZAR
# =====================================================================
CONFIG = {
    "site_url": "https://www.seudominio.com.br/",   # PREENCHER: domínio final COM barra no fim.
                                                    # Sem domínio: https://SEUUSUARIO.github.io/NOMEDOREPO/
    "nome": "Tango Fantasias",
    "razao": "Industria e Comercio Tango Fantasias Ltda.",
    "cnpj": "44.356.735/0001-28",
    "ie": "133.565.666.119",
    "tel_exibicao": "(11) 99238-2902",
    "tel_link": "+5511992382902",
    "whatsapp": "5511992382902",
    "whatsapp_exibicao": "(11) 99238-2902",
    "email": "contato@seudominio.com.br",           # PREENCHER: e-mail de contato
    "rua": "Rua Coronel Emídio Piedade, 73",
    "bairro": "Brás",
    "cidade": "São Paulo",
    "uf": "SP",
    "cep": "03018-010",
    "geo": (-23.5432, -46.6178),                    # aproximado (Brás) — confira no Google Maps
    # PREENCHER/CONFIRMAR horário real
    "horario_texto": "Seg. a sex., 8h às 17h · Sáb., 8h às 13h",
    "horario_schema": [
        (["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"], "08:00", "17:00"),
        (["Saturday"], "08:00", "13:00"),
    ],
    "instagram": "",       # PREENCHER: https://www.instagram.com/...
    "facebook": "",
    "tiktok": "",
    "google_perfil": "",
}

MSG_WA = "Olá! Vim pelo site e gostaria de um orçamento de fantasias."
HOJE = datetime.date.today().isoformat()

from content_categorias import CATEGORIAS      # noqa: E402
from content_paginas import PAGINAS            # noqa: E402
from content_blog import POSTS                 # noqa: E402

# =====================================================================
# ÍCONES SVG
# =====================================================================
def _svg(paths, fill=False):
    attrs = 'fill="currentColor"' if fill else 'fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"'
    return f'<svg viewBox="0 0 24 24" {attrs} aria-hidden="true" focusable="false">{paths}</svg>'

ICONS = {
    "whatsapp": _svg('<path d="M12.04 2C6.58 2 2.13 6.45 2.13 11.91c0 1.75.46 3.45 1.32 4.95L2.05 22l5.25-1.38a9.9 9.9 0 0 0 4.74 1.21h.01c5.46 0 9.9-4.45 9.9-9.91A9.86 9.86 0 0 0 12.04 2Zm0 18.15h-.01a8.2 8.2 0 0 1-4.19-1.15l-.3-.18-3.12.82.83-3.04-.2-.31a8.2 8.2 0 0 1-1.26-4.38c0-4.54 3.7-8.23 8.25-8.23a8.2 8.2 0 0 1 8.24 8.24c0 4.54-3.7 8.23-8.24 8.23Zm4.52-6.16c-.25-.12-1.47-.72-1.69-.81-.23-.08-.39-.12-.56.13-.16.24-.64.8-.78.97-.14.16-.29.18-.54.06-.25-.12-1.05-.39-1.99-1.23-.74-.66-1.23-1.47-1.38-1.72-.14-.25-.01-.38.11-.5.11-.11.25-.29.37-.43.13-.15.17-.25.25-.42.08-.16.04-.31-.02-.43-.06-.12-.56-1.34-.76-1.84-.2-.48-.41-.42-.56-.42h-.48a.92.92 0 0 0-.66.31c-.23.25-.87.85-.87 2.07 0 1.22.89 2.4 1.01 2.56.12.17 1.75 2.67 4.24 3.74.59.26 1.05.41 1.41.52.59.19 1.13.16 1.56.1.48-.07 1.47-.6 1.67-1.18.21-.58.21-1.07.15-1.18-.06-.1-.22-.16-.47-.28Z"/>', fill=True),
    "phone": _svg('<path d="M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3.1 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2.1 4.2 2 2 0 0 1 4.1 2h3a2 2 0 0 1 2 1.7c.1.9.4 1.8.7 2.7a2 2 0 0 1-.5 2.1L8 9.8a16 16 0 0 0 6 6l1.3-1.3a2 2 0 0 1 2.1-.4c.9.3 1.8.6 2.7.7a2 2 0 0 1 1.7 2Z"/>'),
    "mail": _svg('<rect x="3" y="5" width="18" height="14" rx="2"/><path d="m3 7 9 6 9-6"/>'),
    "pin": _svg('<path d="M12 22s7-6.2 7-12a7 7 0 1 0-14 0c0 5.8 7 12 7 12Z"/><circle cx="12" cy="10" r="2.5"/>'),
    "clock": _svg('<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/>'),
    "menu": _svg('<path d="M4 7h16M4 12h16M4 17h16"/>'),
    "up": _svg('<path d="m6 15 6-6 6 6"/>'),
    "check": _svg('<circle cx="12" cy="12" r="9"/><path d="m8 12 3 3 5-6"/>'),
    "factory": _svg('<path d="M3 21V10l6 4V10l6 4V6l6 4v11H3Z"/><path d="M7 17h2M12 17h2M17 17h1"/>'),
    "store": _svg('<path d="M4 9h16l-1.5-5h-13L4 9Z"/><path d="M5 9v11h14V9M10 20v-5h4v5"/>'),
    "box": _svg('<path d="m3 7 9-4 9 4-9 4-9-4Z"/><path d="M3 7v10l9 4 9-4V7M12 11v10"/>'),
    "truck": _svg('<path d="M3 6h11v10H3zM14 10h4l3 3v3h-7"/><circle cx="7" cy="17.5" r="1.8"/><circle cx="17" cy="17.5" r="1.8"/>'),
    "tag": _svg('<path d="M3 12V4h8l10 10-8 8L3 12Z"/><circle cx="7.5" cy="8.5" r="1.3"/>'),
    "scissors": _svg('<circle cx="6" cy="7" r="3"/><circle cx="6" cy="17" r="3"/><path d="m8.5 8.5 11.5 9M8.5 15.5 20 6.5"/>'),
    "ruler": _svg('<rect x="2" y="8" width="20" height="8" rx="1.5"/><path d="M6 8v3M10 8v4M14 8v3M18 8v4"/>'),
    "star": _svg('<path d="m12 3 2.7 5.6 6.1.9-4.4 4.3 1 6.1L12 17l-5.4 2.9 1-6.1L3.2 9.5l6.1-.9L12 3Z"/>'),
    "child": _svg('<circle cx="12" cy="6" r="3"/><path d="M12 9v6M8 12l4-2 4 2M9.5 21l2.5-6 2.5 6"/>'),
    "mask": _svg('<path d="M2 8c3-1 6-1 10 1 4-2 7-2 10-1-.3 5-2.8 8-6 8-2 0-3-1.5-4-3-1 1.5-2 3-4 3-3.2 0-5.7-3-6-8Z"/><circle cx="7.5" cy="11" r="1.2"/><circle cx="16.5" cy="11" r="1.2"/>'),
    "confetti": _svg('<path d="M4 20 9 7l8 8-13 5Z"/><path d="M14 4v2M19 9h2M17 3l-1 2M20 6l-2 1M12 8l1-1"/>'),
    "pumpkin": _svg('<path d="M12 7c-5-2-9 1-9 6.5S7 21 12 20c5 1 9-1 9-6.5S17 5 12 7Z"/><path d="M12 7c-1.5 3-1.5 9 0 13M12 7c1.5 3 1.5 9 0 13M12 7V4l2-1"/>'),
    "flag": _svg('<path d="M2 5c6 3 14 3 20 0"/><path d="m5 6 1.5 5L8 6.7M11 7.5l1 5 1-5M16 6.7l1.5 4.3L19 6"/>'),
    "theater": _svg('<path d="M3 4h9v6a4.5 4.5 0 0 1-9 0V4Z"/><path d="M12 8h9v6a4.5 4.5 0 0 1-9 0"/><path d="M5.5 7.5h.01M9.5 7.5h.01M5.5 11c1 1 3 1 4 0M14.5 11.5h.01M18.5 11.5h.01M14.5 15.5c1-1 3-1 4 0"/>'),
    "crown": _svg('<path d="m3 8 4.5 4L12 5l4.5 7L21 8l-2 11H5L3 8Z"/><path d="M5 19h14"/>'),
    "instagram": _svg('<rect x="3" y="3" width="18" height="18" rx="5"/><circle cx="12" cy="12" r="4"/><circle cx="17.5" cy="6.5" r=".8" fill="currentColor"/>'),
    "facebook": _svg('<path d="M14 8h3V4h-3a4 4 0 0 0-4 4v2H7v4h3v8h4v-8h3l1-4h-4V8Z"/>'),
    "tiktok": _svg('<path d="M14 3v11.5a3.5 3.5 0 1 1-3.5-3.5M14 3c.5 2.5 2.5 4.5 5 4.8"/>'),
    "google": _svg('<path d="M20 12.2c0-.6-.1-1.2-.2-1.7H12v3.3h4.5a3.9 3.9 0 0 1-1.7 2.5v2.1h2.7c1.6-1.5 2.5-3.7 2.5-6.2Z"/><path d="M12 20.5c2.3 0 4.2-.8 5.5-2.1l-2.7-2.1c-.7.5-1.7.8-2.8.8-2.2 0-4-1.5-4.7-3.4H4.6v2.2A8.4 8.4 0 0 0 12 20.5Z"/>'),
}

def esc(s): return html.escape(s, quote=True)
def url_abs(path): return CONFIG["site_url"] + ("" if path == "index.html" else path)
def rel_root(path):
    d = path.count("/"); return "../" * d if d else ""
def wa_href(msg=MSG_WA): return f"https://wa.me/{CONFIG['whatsapp']}?text={quote(msg)}"

def btn_whats(texto="Chamar no WhatsApp", msg=MSG_WA, cls="btn btn--whats"):
    return (f'<a class="{cls} js-wa" href="{wa_href(msg)}" data-msg="{esc(msg)}" target="_blank" rel="noopener">'
            f'{ICONS["whatsapp"]}<span>{texto}</span></a>')
def btn_orc(texto="Pedir orçamento", cls="btn btn--primary"):
    return f'<a class="{cls}" href="@/orcamento.html">{texto}</a>'
def btn_tel(cls="btn btn--outline"):
    return f'<a class="{cls}" href="tel:{CONFIG["tel_link"]}">{ICONS["phone"]}<span>Ligar {CONFIG["tel_exibicao"]}</span></a>'

# ---------------------------------------------------------------- Schemas
def org_id(): return CONFIG["site_url"] + "#empresa"

def schema_website():
    return {"@context": "https://schema.org", "@type": "WebSite", "@id": CONFIG["site_url"] + "#website",
            "url": CONFIG["site_url"], "name": CONFIG["nome"], "inLanguage": "pt-BR", "publisher": {"@id": org_id()}}

def schema_localbusiness():
    c = CONFIG
    same = [u for u in (c["instagram"], c["facebook"], c["tiktok"], c["google_perfil"]) if u]
    d = {
        "@context": "https://schema.org", "@type": "ClothingStore", "@id": org_id(),
        "name": c["nome"], "legalName": c["razao"], "taxID": c["cnpj"],
        "description": "Fábrica de fantasias no Brás, São Paulo: confecção própria e venda no atacado e no varejo.",
        "url": c["site_url"], "logo": c["site_url"] + "assets/img/logo-tango-fantasias.png",
        "image": c["site_url"] + "assets/img/og-tango-fantasias.jpg",
        "telephone": c["tel_link"], "email": c["email"], "priceRange": "$$",
        "address": {"@type": "PostalAddress", "streetAddress": c["rua"], "addressLocality": c["cidade"],
                    "addressRegion": c["uf"], "postalCode": c["cep"], "addressCountry": "BR"},
        "geo": {"@type": "GeoCoordinates", "latitude": c["geo"][0], "longitude": c["geo"][1]},
        "openingHoursSpecification": [{"@type": "OpeningHoursSpecification", "dayOfWeek": d_, "opens": a, "closes": f}
                                      for d_, a, f in c["horario_schema"]],
        "areaServed": [{"@type": "City", "name": "São Paulo"}, {"@type": "State", "name": "São Paulo"}, {"@type": "Country", "name": "Brasil"}],
        "hasOfferCatalog": {"@type": "OfferCatalog", "name": "Fantasias e acessórios",
                            "itemListElement": [{"@type": "OfferCatalog", "name": s["nome"], "url": url_abs("fantasias/" + s["slug"] + ".html")} for s in CATEGORIAS]},
    }
    if same: d["sameAs"] = same
    return d

def schema_breadcrumb(crumbs):
    return {"@context": "https://schema.org", "@type": "BreadcrumbList",
            "itemListElement": [{"@type": "ListItem", "position": i + 1, "name": n, "item": url_abs(p)} for i, (n, p) in enumerate(crumbs)]}

def schema_faq(faqs):
    return {"@context": "https://schema.org", "@type": "FAQPage",
            "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": re.sub(r"<[^>]+>", "", a)}} for q, a in faqs]}

def schema_colecao(s, path):
    return {"@context": "https://schema.org", "@type": "CollectionPage", "name": s["h1"], "description": s["desc"],
            "url": url_abs(path), "inLanguage": "pt-BR", "image": CONFIG["site_url"] + "assets/img/" + s["img"],
            "isPartOf": {"@id": CONFIG["site_url"] + "#website"},
            "about": {"@type": "Thing", "name": s["nome"]},
            "provider": {"@type": "ClothingStore", "@id": org_id(), "name": CONFIG["nome"], "telephone": CONFIG["tel_link"],
                         "address": {"@type": "PostalAddress", "addressLocality": CONFIG["cidade"], "addressRegion": CONFIG["uf"], "addressCountry": "BR"}}}

def schema_post(p, path):
    return {"@context": "https://schema.org", "@type": "BlogPosting", "headline": p["h1"], "description": p["desc"],
            "image": CONFIG["site_url"] + "assets/img/" + p["img"], "datePublished": p["data"], "dateModified": p["data"],
            "inLanguage": "pt-BR", "mainEntityOfPage": url_abs(path),
            "author": {"@type": "Organization", "name": CONFIG["nome"], "url": CONFIG["site_url"]},
            "publisher": {"@type": "Organization", "name": CONFIG["nome"],
                          "logo": {"@type": "ImageObject", "url": CONFIG["site_url"] + "assets/img/logo-tango-fantasias.png"}}}

# ---------------------------------------------------------------- Componentes
def faq_html(faqs):
    out = ['<div class="faq">']
    for q, a in faqs:
        body = a if a.strip().startswith("<") else f"<p>{a}</p>"
        out.append(f'<details><summary>{q}</summary><div class="faq__body">{body}</div></details>')
    out.append("</div>")
    return "\n".join(out)

NAV = [("Início", "index.html"), ("Fantasias", "fantasias.html"), ("Atacado", "atacado.html"),
       ("Como comprar", "como-comprar.html"), ("Sobre", "sobre.html"), ("Blog", "blog.html"), ("Contato", "contato.html")]

def header(active):
    items = "".join(f'<li><a href="@/{h}"{" aria-current=\"page\"" if active == h else ""}>{n}</a></li>' for n, h in NAV)
    return f'''<a class="skip-link" href="#conteudo">Pular para o conteúdo</a>
<header class="site-header">
  <div class="container">
    <a class="logo" href="@/index.html" aria-label="Tango Fantasias — página inicial">
      <img src="@/assets/img/logo-tango-fantasias.svg" alt="Tango Fantasias" width="168" height="40">
    </a>
    <button class="nav-toggle" type="button" aria-expanded="false" aria-controls="menu-principal" aria-label="Abrir menu">{ICONS["menu"]}</button>
    <nav class="main-nav" id="menu-principal" aria-label="Menu principal">
      <ul>{items}</ul>
      <div class="nav-cta">
        <a class="btn btn--outline header-call" href="tel:{CONFIG["tel_link"]}">{ICONS["phone"]}<span>{CONFIG["tel_exibicao"]}</span></a>
        {btn_orc("Orçamento")}
      </div>
    </nav>
  </div>
</header>'''

def footer():
    c = CONFIG
    cats = "".join(f'<li><a href="@/fantasias/{s["slug"]}.html">{s["nome_curto"]}</a></li>' for s in CATEGORIAS)
    social = []
    for k, label in (("instagram", "Instagram"), ("facebook", "Facebook"), ("tiktok", "TikTok"), ("google_perfil", "Perfil da Empresa no Google")):
        if c[k]:
            social.append(f'<a href="{c[k]}" target="_blank" rel="noopener" aria-label="{label} da Tango Fantasias">{ICONS["google" if k == "google_perfil" else k]}</a>')
    social_html = f'<div class="social">{"".join(social)}</div>' if social else \
        '<!-- PREENCHER: redes sociais — configure instagram/facebook/tiktok/google_perfil no build.py ou insira os links aqui -->'
    return f'''<footer class="site-footer">
  <div class="container">
    <div class="footer-grid">
      <div>
        <img class="footer-logo" src="@/assets/img/logo-tango-fantasias-branco.svg" alt="Tango Fantasias" width="168" height="40" loading="lazy">
        <p class="legal"><strong>{c["razao"]}</strong><br>CNPJ: {c["cnpj"]}<br>Inscrição Estadual: {c["ie"]}</p>
        <p class="legal">Fábrica e venda de fantasias no atacado e no varejo, no Brás, em São Paulo.</p>
        {social_html}
      </div>
      <div>
        <h2>Fantasias</h2>
        <ul>{cats}</ul>
      </div>
      <div>
        <h2>Institucional</h2>
        <ul>
          <li><a href="@/sobre.html">Sobre a Tango</a></li>
          <li><a href="@/atacado.html">Atacado para lojistas</a></li>
          <li><a href="@/como-comprar.html">Como comprar</a></li>
          <li><a href="@/faq.html">Perguntas frequentes</a></li>
          <li><a href="@/blog.html">Blog</a></li>
          <li><a href="@/orcamento.html">Pedir orçamento</a></li>
          <li><a href="@/contato.html">Contato</a></li>
          <li><a href="@/politica-de-privacidade.html">Política de Privacidade</a></li>
          <li><a href="@/termos-de-uso.html">Termos de Uso</a></li>
        </ul>
      </div>
      <div>
        <h2>Atendimento</h2>
        <ul>
          <li><a class="js-wa" href="{wa_href()}" data-msg="{esc(MSG_WA)}">WhatsApp {c["whatsapp_exibicao"]}</a></li>
          <li><a href="tel:{c["tel_link"]}">Ligar {c["tel_exibicao"]}</a></li>
          <li><a href="mailto:{c["email"]}">{c["email"]}</a></li>
          <li>{c["rua"]}<br>{c["bairro"]}, {c["cidade"]} - {c["uf"]}<br>CEP {c["cep"]}</li>
          <li>{c["horario_texto"]}</li>
        </ul>
      </div>
    </div>
    <div class="footer-bottom">
      <span>© <span class="js-year">{datetime.date.today().year}</span> {c["nome"]}. Todos os direitos reservados.</span>
      <span>Brás · São Paulo - SP</span>
    </div>
  </div>
</footer>
<a class="whats-float js-wa" href="{wa_href()}" data-msg="{esc(MSG_WA)}" target="_blank" rel="noopener" aria-label="Conversar no WhatsApp">{ICONS["whatsapp"]}</a>
<div class="call-bar"><a href="tel:{c["tel_link"]}">{ICONS["phone"]}<span>Ligar agora</span></a></div>
<button class="to-top" type="button" aria-label="Voltar ao topo">{ICONS["up"]}</button>
<div class="cookie-banner" role="region" aria-label="Aviso de cookies" hidden>
  <p>Usamos cookies para melhorar sua experiência e medir o desempenho do site, conforme a <a href="@/politica-de-privacidade.html">Política de Privacidade</a>.</p>
  <div class="btn-row">
    <button class="btn btn--primary" type="button" data-consent="aceito">Aceitar</button>
    <button class="btn btn--outline" type="button" data-consent="recusado">Recusar</button>
  </div>
</div>'''

ANALYTICS = '''  <!-- =========================================================
       PREENCHER: Google Tag Manager / GA4 / Google Ads
       Descomente UM dos blocos abaixo e troque os IDs.
       Os eventos (clique_whatsapp, clique_telefone, envio_orcamento,
       envio_contato) já são disparados pelo assets/js/main.js.
       =========================================================
  <script>
    window.dataLayer = window.dataLayer || [];
    function gtag(){dataLayer.push(arguments);}
    gtag('consent', 'default', {analytics_storage:'denied', ad_storage:'denied', ad_user_data:'denied', ad_personalization:'denied'});
  </script>

  Opção A — Google Tag Manager (GTM-XXXXXXX):
  <script>(function(w,d,s,l,i){w[l]=w[l]||[];w[l].push({'gtm.start':new Date().getTime(),event:'gtm.js'});var f=d.getElementsByTagName(s)[0],j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src='https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);})(window,document,'script','dataLayer','GTM-XXXXXXX');</script>

  Opção B — GA4 + Google Ads direto (G-XXXXXXXXXX e AW-XXXXXXXXX):
  <script async src="https://www.googletagmanager.com/gtag/js?id=G-XXXXXXXXXX"></script>
  <script>
    gtag('js', new Date());
    gtag('config', 'G-XXXXXXXXXX');
    gtag('config', 'AW-XXXXXXXXX');
  </script>
  ========================================================= -->'''

def head(page, r):
    canonical = url_abs(page["path"])
    img = CONFIG["site_url"] + "assets/img/" + page.get("og_img", "og-tango-fantasias.jpg")
    schemas = [schema_website()] + page.get("schemas", [])
    if page.get("crumbs"): schemas.append(schema_breadcrumb(page["crumbs"]))
    ld = "\n".join(f'  <script type="application/ld+json">{json.dumps(s, ensure_ascii=False)}</script>' for s in schemas)
    return f'''<!DOCTYPE html>
<html lang="pt-BR" class="no-js">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{esc(page["title"])}</title>
  <meta name="description" content="{esc(page["desc"])}">
  <meta name="robots" content="{page.get("robots", "index,follow")}">
  <link rel="canonical" href="{canonical}">
  <meta name="theme-color" content="#1f0f33">
  <meta property="og:type" content="{page.get("og_type", "website")}">
  <meta property="og:locale" content="pt_BR">
  <meta property="og:site_name" content="{CONFIG["nome"]}">
  <meta property="og:title" content="{esc(page["title"])}">
  <meta property="og:description" content="{esc(page["desc"])}">
  <meta property="og:url" content="{canonical}">
  <meta property="og:image" content="{img}">
  <meta property="og:image:alt" content="{esc(page.get("og_alt", "Tango Fantasias — fábrica de fantasias no Brás, São Paulo"))}">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="{esc(page["title"])}">
  <meta name="twitter:description" content="{esc(page["desc"])}">
  <meta name="twitter:image" content="{img}">
  <link rel="icon" href="{r}favicon.ico" sizes="32x32">
  <link rel="icon" href="{r}assets/img/favicon.svg" type="image/svg+xml">
  <link rel="apple-touch-icon" href="{r}assets/img/apple-touch-icon.png">
  <link rel="manifest" href="{r}manifest.json">
  {page.get("preload", "")}
  <link rel="stylesheet" href="{r}assets/css/style.css">
{ANALYTICS}
{ld}
</head>
<body>'''

def breadcrumb_html(crumbs):
    if not crumbs or len(crumbs) < 2: return ""
    li = [f'<li aria-current="page">{n}</li>' if i == len(crumbs) - 1 else f'<li><a href="@/{p}">{n}</a></li>' for i, (n, p) in enumerate(crumbs)]
    return f'<nav class="breadcrumb" aria-label="Você está em"><div class="container"><ol>{"".join(li)}</ol></div></nav>'

def render(page):
    r = CONFIG["site_url"] if page.get("absolute_root") else rel_root(page["path"])
    body = (head(page, r) + "\n" + header(page.get("active")) + "\n<main id=\"conteudo\">\n" + breadcrumb_html(page.get("crumbs"))
            + "\n" + page["body"] + "\n</main>\n" + footer() + f'\n<script src="{r}assets/js/main.js" defer></script>\n</body>\n</html>\n')
    body = body.replace('"@/index.html"', f'"{r or "./"}"').replace("@/", r)
    dest = os.path.join(OUT, page["path"])
    os.makedirs(os.path.dirname(dest), exist_ok=True)
    open(dest, "w", encoding="utf-8").write(body)

# =====================================================================
# PÁGINAS DE CATEGORIA (template)
# =====================================================================
def categoria_page(s):
    path = f'fantasias/{s["slug"]}.html'
    rel = [x for x in CATEGORIAS if x["slug"] in s["relacionados"]]
    rel_html = "".join(f'''<article class="card"><div class="icon-circle">{ICONS[x["icone"]]}</div>
<h3><a href="@/fantasias/{x["slug"]}.html">{x["nome"]}</a></h3><p>{x["resumo"]}</p></article>''' for x in rel)
    destaques = "".join(f"<li>{x}</li>" for x in s["destaques"])
    side = "".join(f'<li><a href="@/fantasias/{x["slug"]}.html"{" aria-current=\"page\"" if x is s else ""}>{x["nome_curto"]}</a></li>' for x in CATEGORIAS)
    steps = "".join(f"<li><h3>{t}</h3><p>{d}</p></li>" for t, d in s["passos"])
    msg = f"Olá! Vim pelo site e gostaria de um orçamento de {s['nome_curto'].lower()}."
    body = f'''<section class="page-hero">
  <div class="container">
    <h1>{s["h1"]}</h1>
    <p>{s["lead"]}</p>
    <div class="btn-row">{btn_whats(msg=msg)}{btn_orc("Pedir orçamento", "btn btn--outline")}</div>
  </div>
</section>
<div class="section">
  <div class="container content-layout">
    <article class="prose">
      <h2>{s["oque_titulo"]}</h2>
      {s["oque"]}
      <figure>
        <img src="@/assets/img/{s["img"]}" alt="{s["img_alt"]}" width="1200" height="675" loading="lazy" decoding="async">
        <figcaption>{s["img_cap"]}</figcaption>
      </figure>
      <h2>{s["destaques_titulo"]}</h2>
      <ul class="check-list">{destaques}</ul>
      <!-- PREENCHER: insira aqui fotos reais dos modelos (galeria) com alt descritivo, sem usar personagens licenciados sem autorização. -->
      <h2>Como comprar</h2>
      <ol class="steps steps--5">{steps}</ol>
      <h2>{s["qualidade_titulo"]}</h2>
      {s["qualidade"]}
      <h2>Para quem vendemos</h2>
      {s["publico"]}
      <ul class="chips"><li>Lojas de fantasias</li><li>Lojas de festas e presentes</li><li>Revendedores</li><li>Escolas e grupos de dança</li><li>Blocos e escolas de samba</li><li>Eventos e animação</li><li>Consumidor final</li></ul>
      <h2>Tamanhos, prazos e condições</h2>
      {s["condicoes"]}
      <!-- PREENCHER: grade de tamanhos, pedido mínimo de atacado e prazos reais desta categoria. -->
      <h2>Perguntas frequentes sobre {s["faq_titulo"]}</h2>
      {faq_html(s["faq"])}
      <div class="cta-box" style="margin-top:32px">
        <h2>Quer {s["nome_curto"].lower()} para revenda ou para o seu evento?</h2>
        <p>Fale com a Tango pelo WhatsApp ou envie seu pedido pelo formulário. Atendemos lojistas e consumidor final.</p>
        <div class="btn-row">{btn_whats(msg=msg)}{btn_orc("Pedir orçamento", "btn btn--light")}</div>
      </div>
    </article>
    <aside class="sidebar" aria-label="Atalhos">
      <div class="cta-box">
        <h2>Orçamento rápido</h2>
        <p>Diga os modelos, tamanhos e quantidades pelo WhatsApp.</p>
        {btn_whats("WhatsApp", msg)}
        <a class="btn btn--light" href="@/atacado.html">Comprar no atacado</a>
      </div>
      <div class="card"><h2 style="font-size:1.1rem">Categorias</h2><ul>{side}</ul></div>
      <div class="card"><h2 style="font-size:1.1rem">Onde estamos</h2><p>{CONFIG["rua"]}, {CONFIG["bairro"]} — São Paulo/SP, no polo atacadista de confecção do Brás.</p><a class="card__link" href="@/contato.html">Ver mapa e contato</a></div>
    </aside>
  </div>
</div>
<section class="section section--alt">
  <div class="container">
    <h2>Veja também</h2>
    <div class="grid grid--3">{rel_html}</div>
    <p style="margin-top:20px">Dicas de tamanhos e conservação no nosso <a href="@/blog.html">blog</a> e nas <a href="@/faq.html">perguntas frequentes</a>.</p>
  </div>
</section>'''
    return {"path": path, "title": s["title"], "desc": s["desc"], "active": "fantasias.html",
            "crumbs": [("Início", "index.html"), ("Fantasias", "fantasias.html"), (s["nome"], path)],
            "schemas": [schema_colecao(s, path), schema_faq(s["faq"])], "body": body,
            "og_img": s["img"].replace(".webp", ".jpg"), "og_alt": s["img_alt"], "priority": "0.9"}

def post_page(p):
    path = f'blog/{p["slug"]}.html'
    outros = "".join(f'<li><a href="@/blog/{x["slug"]}.html">{x["h1"]}</a></li>' for x in POSTS if x is not p)
    data_br = datetime.date.fromisoformat(p["data"]).strftime("%d/%m/%Y")
    citadas = "".join(f'<li><a href="@/fantasias/{x}.html">{next(s["nome_curto"] for s in CATEGORIAS if s["slug"] == x)}</a></li>' for x in p["categorias"])
    body = f'''<section class="page-hero"><div class="container"><h1>{p["h1"]}</h1><p>{p["lead"]}</p></div></section>
<div class="section">
  <div class="container content-layout">
    <article class="prose">
      <p class="post-meta">Publicado em <time datetime="{p["data"]}">{data_br}</time> · Tango Fantasias</p>
      <figure><img src="@/assets/img/{p["img"]}" alt="{p["img_alt"]}" width="1200" height="675" loading="lazy" decoding="async"></figure>
      {p["corpo"]}
      <div class="cta-box" style="margin-top:32px">
        <h2>Precisa de fantasias?</h2>
        <p>A Tango Fantasias fabrica e vende no atacado e no varejo, no Brás, em São Paulo.</p>
        <div class="btn-row">{btn_whats()}{btn_orc("Pedir orçamento", "btn btn--light")}</div>
      </div>
    </article>
    <aside class="sidebar" aria-label="Leia também">
      <div class="card"><h2 style="font-size:1.1rem">Leia também</h2><ul>{outros}</ul></div>
      <div class="card"><h2 style="font-size:1.1rem">Categorias citadas</h2><ul>{citadas}</ul></div>
    </aside>
  </div>
</div>'''
    return {"path": path, "title": p["title"], "desc": p["desc"], "active": "blog.html", "og_type": "article",
            "crumbs": [("Início", "index.html"), ("Blog", "blog.html"), (p["h1"], path)],
            "schemas": [schema_post(p, path)], "body": body, "og_img": p["img"].replace(".webp", ".jpg"), "og_alt": p["img_alt"], "priority": "0.6"}

def sitemap(pages):
    urls = [f'  <url><loc>{url_abs(p["path"])}</loc><lastmod>{HOJE}</lastmod><changefreq>{p.get("freq", "monthly")}</changefreq><priority>{p.get("priority", "0.7")}</priority></url>'
            for p in pages if not p.get("robots", "").startswith("noindex")]
    open(os.path.join(OUT, "sitemap.xml"), "w", encoding="utf-8").write(
        '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + "\n".join(urls) + "\n</urlset>\n")
    open(os.path.join(OUT, "robots.txt"), "w", encoding="utf-8").write(
        f"User-agent: *\nAllow: /\nDisallow: /_gerador/\n\nSitemap: {CONFIG['site_url']}sitemap.xml\n")

def main():
    ctx = dict(CONFIG=CONFIG, ICONS=ICONS, CATEGORIAS=CATEGORIAS, POSTS=POSTS, btn_whats=btn_whats, btn_orc=btn_orc,
               btn_tel=btn_tel, faq_html=faq_html, schema_localbusiness=schema_localbusiness, schema_faq=schema_faq,
               wa_href=wa_href, MSG_WA=MSG_WA)
    pages = PAGINAS(ctx) + [categoria_page(s) for s in CATEGORIAS] + [post_page(p) for p in POSTS]
    for p in pages: render(p)
    sitemap(pages)
    manifest = {"name": CONFIG["nome"], "short_name": "Tango", "lang": "pt-BR", "start_url": "./", "scope": "./",
                "display": "standalone", "background_color": "#ffffff", "theme_color": "#1f0f33",
                "icons": [{"src": "assets/img/icon-192.png", "sizes": "192x192", "type": "image/png"},
                          {"src": "assets/img/icon-512.png", "sizes": "512x512", "type": "image/png"},
                          {"src": "assets/img/icon-512.png", "sizes": "512x512", "type": "image/png", "purpose": "maskable"}]}
    json.dump(manifest, open(os.path.join(OUT, "manifest.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=2)
    print(f"{len(pages)} páginas geradas em {OUT}")

if __name__ == "__main__":
    main()
