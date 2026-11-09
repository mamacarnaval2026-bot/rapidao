#!/usr/bin/env python3
"""
Gerador do site estático da Elbatec Controle de Pragas.

USO (opcional — o site já vem gerado):
  1. Edite o bloco CONFIG abaixo (WhatsApp, e-mail, domínio, horário...).
  2. Rode:  python3 build.py
  3. Os arquivos são gravados na pasta-mãe (raiz do site).

Você também pode editar os .html diretamente; este script só facilita
trocar dados em todas as páginas de uma vez.
"""
import json, os, re, shutil, datetime, html

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.environ.get("ELBATEC_OUT", os.path.dirname(HERE))

# =====================================================================
# CONFIG — PERSONALIZAR
# =====================================================================
CONFIG = {
    "site_url": "https://www.seudominio.com.br/",   # PREENCHER: domínio final COM barra no fim.
                                                    # Sem domínio: https://SEUUSUARIO.github.io/NOMEDOREPO/
    "nome": "Elbatec Controle de Pragas",
    "razao": "Elbatec Controle de Pragas e Servicos LTDA",
    "cnpj": "37.491.092/0001-60",
    "ie": "241.135.700.117",
    "tel_exibicao": "(11) 3232-2206",
    "tel_link": "+551132322206",
    "whatsapp": "5511000000000",                    # PREENCHER: 55 + DDD + número
    "whatsapp_exibicao": "(11) 00000-0000",         # PREENCHER: como o número aparece no site
    "email": "contato@seudominio.com.br",           # PREENCHER: e-mail de contato
    "rua": "Rua das Palmas, 235, Sala 04",
    "bairro": "Ipês (Polvilho)",
    "cidade": "Cajamar",
    "uf": "SP",
    "cep": "07791-655",
    "geo": (-23.3990, -46.8370),                    # aproximado (Polvilho, Cajamar) — ajuste pelo Google Maps
    # PREENCHER/CONFIRMAR horário real. Formato schema.org: dias + abre + fecha
    "horario_texto": "Seg. a sex., 8h às 18h · Sáb., 8h às 12h",
    "horario_schema": [
        (["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"], "08:00", "18:00"),
        (["Saturday"], "08:00", "12:00"),
    ],
    # PREENCHER: redes sociais (deixe vazio "" se não tiver)
    "instagram": "",
    "facebook": "",
    "google_perfil": "",
}

MSG_WA = "Olá! Vim pelo site e gostaria de um orçamento."
HOJE = datetime.date.today().isoformat()

AREAS = [
    ("Cajamar", ["Polvilho", "Jordanésia", "Centro", "Ipês"]),
    ("Santana de Parnaíba", []), ("Pirapora do Bom Jesus", []), ("Caieiras", []),
    ("Franco da Rocha", []), ("Cabreúva", []), ("Jundiaí", []), ("Barueri", []),
    ("Osasco", []), ("Perus (São Paulo)", []), ("Pirituba (São Paulo)", []),
    ("Região noroeste de São Paulo", []),
]
AREA_SERVED = ["Cajamar", "Santana de Parnaíba", "Pirapora do Bom Jesus", "Caieiras", "Franco da Rocha",
               "Cabreúva", "Jundiaí", "Barueri", "Osasco", "São Paulo"]

# =====================================================================
# ÍCONES SVG (inline, sem dependências)
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
    "shield": _svg('<path d="M12 3 4 6v6c0 4.5 3.4 8.3 8 9 4.6-.7 8-4.5 8-9V6l-8-3Z"/><path d="m9 12 2 2 4-4"/>'),
    "bolt": _svg('<path d="M13 2 4 14h7l-1 8 9-12h-7l1-8Z"/>'),
    "doc": _svg('<path d="M14 3H6a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V9l-6-6Z"/><path d="M14 3v6h6M8 13h8M8 17h5"/>'),
    "building": _svg('<rect x="4" y="3" width="16" height="18" rx="1"/><path d="M9 7h1M14 7h1M9 11h1M14 11h1M9 15h1M14 15h1M10 21v-3h4v3"/>'),
    "home": _svg('<path d="m3 11 9-7 9 7"/><path d="M5 10v10h14V10"/><path d="M10 20v-5h4v5"/>'),
    "bug": _svg('<ellipse cx="12" cy="14" rx="5" ry="6"/><path d="M12 8V5M9 5l1.5 2M15 5l-1.5 2M7 12H3M21 12h-4M7 16l-3 2M17 16l3 2M7.5 9 5 7M16.5 9 19 7M12 10v10"/>'),
    "rat": _svg('<path d="M3 16c0-4 3.5-7 8-7 3 0 5.5 1.3 6.7 3.4L21 13l-2.3 1.3c-.6 2-3 3.7-6.7 3.7H6"/><circle cx="16.5" cy="12.5" r=".6" fill="currentColor"/><path d="M14 9.4a2 2 0 1 1 3-2.4M6 18c-2 0-3 1-3 2"/>'),
    "wood": _svg('<rect x="3" y="6" width="18" height="12" rx="2"/><path d="M7 10h4M13 14h4M9 14h1M15 10h2"/><circle cx="12" cy="12" r=".8" fill="currentColor"/>'),
    "mosquito": _svg('<path d="M12 9v9M12 9l-6-4M12 9l6-4M12 13l-5 5M12 13l5 5M12 13l-6 1M12 13l6 1"/><circle cx="12" cy="7" r="1.6"/><path d="M12 5.4V2"/>'),
    "scorpion": _svg('<path d="M6 19c2 1 5 1 6-1s0-4-2-5-3-3-1-5 6-1 7 2-1 5-3 4"/><path d="M16 14c2-.5 3-2 3-4M3 13l3 1M3 17l3-1M5 10l2 2"/>'),
    "bird": _svg('<path d="M16 7a3 3 0 0 0-5.8 1.1L4 14c2 1 5 1.5 7 .5l2 4.5 1-5c2.2-1 3.5-3 3.5-5.5L20 8l-3-1Z"/><circle cx="15.5" cy="7.5" r=".6" fill="currentColor"/>'),
    "spray": _svg('<rect x="6" y="9" width="8" height="12" rx="2"/><path d="M8 9V6h4v3M12 6h2l1-2M17 5h.01M19 7h.01M19 3h.01M21 5h.01"/>'),
    "water": _svg('<path d="M12 3s6 6.6 6 11a6 6 0 0 1-12 0c0-4.4 6-11 6-11Z"/><path d="M9.5 15a2.5 2.5 0 0 0 2.5 2.5"/>'),
    "pipe": _svg('<path d="M4 4h6v4H8v4a2 2 0 0 0 2 2h4V12h4v8h-4v-2h-4a6 6 0 0 1-6-6V8H4V4Z"/>'),
    "flask": _svg('<path d="M9 3h6M10 3v6l-5 9a2 2 0 0 0 1.7 3h10.6A2 2 0 0 0 19 18l-5-9V3"/><path d="M7.5 15h9"/>'),
    "instagram": _svg('<rect x="3" y="3" width="18" height="18" rx="5"/><circle cx="12" cy="12" r="4"/><circle cx="17.5" cy="6.5" r=".8" fill="currentColor"/>'),
    "facebook": _svg('<path d="M14 8h3V4h-3a4 4 0 0 0-4 4v2H7v4h3v8h4v-8h3l1-4h-4V8Z"/>'),
    "google": _svg('<path d="M20 12.2c0-.6-.1-1.2-.2-1.7H12v3.3h4.5a3.9 3.9 0 0 1-1.7 2.5v2.1h2.7c1.6-1.5 2.5-3.7 2.5-6.2Z"/><path d="M12 20.5c2.3 0 4.2-.8 5.5-2.1l-2.7-2.1c-.7.5-1.7.8-2.8.8-2.2 0-4-1.5-4.7-3.4H4.6v2.2A8.4 8.4 0 0 0 12 20.5Z"/>'),
}

# =====================================================================
# SERVIÇOS (nome, slug, ícone) — conteúdo completo em content_servicos.py
# =====================================================================
from content_servicos import SERVICOS, PRODUTOS  # noqa: E402
from content_paginas import PAGINAS            # noqa: E402
from content_blog import POSTS                 # noqa: E402

def esc(s):
    return html.escape(s, quote=True)

def url_abs(path):
    return CONFIG["site_url"] + ("" if path == "index.html" else path)

def rel_root(path):
    depth = path.count("/")
    return "../" * depth if depth else ""

def wa_href(msg=MSG_WA):
    from urllib.parse import quote
    return f"https://wa.me/{CONFIG['whatsapp']}?text={quote(msg)}"

def btn_whats(texto="Chamar no WhatsApp", msg=MSG_WA, cls="btn btn--whats"):
    return (f'<a class="{cls} js-wa" href="{wa_href(msg)}" data-msg="{esc(msg)}" target="_blank" rel="noopener">'
            f'{ICONS["whatsapp"]}<span>{texto}</span></a>')

def btn_orc(texto="Pedir orçamento", cls="btn btn--primary"):
    return f'<a class="{cls}" href="@/orcamento.html">{texto}</a>'

def btn_tel(cls="btn btn--outline"):
    return f'<a class="{cls}" href="tel:{CONFIG["tel_link"]}">{ICONS["phone"]}<span>Ligar {CONFIG["tel_exibicao"]}</span></a>'

# ---------------------------------------------------------------------
# Schemas
# ---------------------------------------------------------------------
ORG_ID = None
def org_id():
    return CONFIG["site_url"] + "#empresa"

def schema_website():
    return {"@context": "https://schema.org", "@type": "WebSite", "@id": CONFIG["site_url"] + "#website",
            "url": CONFIG["site_url"], "name": CONFIG["nome"], "inLanguage": "pt-BR",
            "publisher": {"@id": org_id()}}

def schema_localbusiness():
    c = CONFIG
    same = [u for u in (c["instagram"], c["facebook"], c["google_perfil"]) if u]
    d = {
        "@context": "https://schema.org", "@type": "PestControlService", "@id": org_id(),
        "name": c["nome"], "legalName": c["razao"], "taxID": c["cnpj"],
        "url": c["site_url"], "logo": c["site_url"] + "assets/img/logo-elbatec.png",
        "image": c["site_url"] + "assets/img/og-elbatec.jpg",
        "telephone": c["tel_link"], "email": c["email"], "priceRange": "$$",
        "address": {"@type": "PostalAddress", "streetAddress": c["rua"], "addressLocality": c["cidade"],
                    "addressRegion": c["uf"], "postalCode": c["cep"], "addressCountry": "BR"},
        "geo": {"@type": "GeoCoordinates", "latitude": c["geo"][0], "longitude": c["geo"][1]},
        "openingHoursSpecification": [{"@type": "OpeningHoursSpecification", "dayOfWeek": d_, "opens": a, "closes": f}
                                      for d_, a, f in c["horario_schema"]],
        "areaServed": [{"@type": "City", "name": n} for n in AREA_SERVED],
        "hasOfferCatalog": {"@type": "OfferCatalog", "name": "Serviços de controle de pragas e saneamento",
                            "itemListElement": [{"@type": "Offer", "itemOffered": {"@type": "Service", "name": s["nome"],
                                                 "url": url_abs("servicos/" + s["slug"] + ".html")}} for s in SERVICOS]},
    }
    if same:
        d["sameAs"] = same
    return d

def schema_breadcrumb(crumbs):
    return {"@context": "https://schema.org", "@type": "BreadcrumbList",
            "itemListElement": [{"@type": "ListItem", "position": i + 1, "name": n, "item": url_abs(p)}
                                for i, (n, p) in enumerate(crumbs)]}

def schema_faq(faqs):
    return {"@context": "https://schema.org", "@type": "FAQPage",
            "mainEntity": [{"@type": "Question", "name": q,
                            "acceptedAnswer": {"@type": "Answer", "text": re.sub(r"<[^>]+>", "", a)}} for q, a in faqs]}

def schema_service(s, path):
    return {"@context": "https://schema.org", "@type": "Service", "name": s["nome"], "serviceType": s["nome"],
            "description": s["desc"], "url": url_abs(path),
            "provider": {"@type": "PestControlService", "@id": org_id(), "name": CONFIG["nome"],
                         "telephone": CONFIG["tel_link"],
                         "address": {"@type": "PostalAddress", "addressLocality": CONFIG["cidade"], "addressRegion": CONFIG["uf"], "addressCountry": "BR"}},
            "areaServed": [{"@type": "City", "name": n} for n in AREA_SERVED],
            "image": CONFIG["site_url"] + "assets/img/" + s["img"]}

def schema_post(p, path):
    return {"@context": "https://schema.org", "@type": "BlogPosting", "headline": p["h1"], "description": p["desc"],
            "image": CONFIG["site_url"] + "assets/img/" + p["img"], "datePublished": p["data"], "dateModified": p["data"],
            "inLanguage": "pt-BR", "mainEntityOfPage": url_abs(path),
            "author": {"@type": "Organization", "name": CONFIG["nome"], "url": CONFIG["site_url"]},
            "publisher": {"@type": "Organization", "name": CONFIG["nome"],
                          "logo": {"@type": "ImageObject", "url": CONFIG["site_url"] + "assets/img/logo-elbatec.png"}}}

# ---------------------------------------------------------------------
# Componentes compartilhados
# ---------------------------------------------------------------------
def faq_html(faqs):
    out = ['<div class="faq">']
    for q, a in faqs:
        body = a if a.strip().startswith("<") else f"<p>{a}</p>"
        out.append(f'<details><summary>{q}</summary><div class="faq__body">{body}</div></details>')
    out.append("</div>")
    return "\n".join(out)

NAV = [("Início", "index.html"), ("Serviços", "servicos.html"), ("Empresas", "empresas-e-condominios.html"),
       ("Áreas atendidas", "areas-atendidas.html"), ("Sobre", "sobre.html"), ("Blog", "blog.html"), ("Contato", "contato.html")]

def header(active):
    items = []
    for nome, href in NAV:
        cur = ' aria-current="page"' if active == href else ""
        items.append(f'<li><a href="@/{href}"{cur}>{nome}</a></li>')
    return f'''<a class="skip-link" href="#conteudo">Pular para o conteúdo</a>
<header class="site-header">
  <div class="container">
    <a class="logo" href="@/index.html" aria-label="Elbatec Controle de Pragas — página inicial">
      <img src="@/assets/img/logo-elbatec.svg" alt="Elbatec Controle de Pragas" width="168" height="40">
    </a>
    <button class="nav-toggle" type="button" aria-expanded="false" aria-controls="menu-principal" aria-label="Abrir menu">{ICONS["menu"]}</button>
    <nav class="main-nav" id="menu-principal" aria-label="Menu principal">
      <ul>
        {"".join(items)}
      </ul>
      <div class="nav-cta">
        <a class="btn btn--outline header-call" href="tel:{CONFIG["tel_link"]}">{ICONS["phone"]}<span>{CONFIG["tel_exibicao"]}</span></a>
        {btn_orc("Orçamento")}
      </div>
    </nav>
  </div>
</header>'''

def footer():
    c = CONFIG
    serv = "".join(f'<li><a href="@/servicos/{s["slug"]}.html">{s["nome_curto"]}</a></li>' for s in SERVICOS)
    social = []
    for k, label in (("instagram", "Instagram"), ("facebook", "Facebook"), ("google_perfil", "Perfil da Empresa no Google")):
        if c[k]:
            social.append(f'<a href="{c[k]}" target="_blank" rel="noopener" aria-label="{label} da Elbatec">{ICONS["google" if k=="google_perfil" else k]}</a>')
    social_html = f'<div class="social">{"".join(social)}</div>' if social else \
        '<!-- PREENCHER: redes sociais — configure instagram/facebook/google_perfil no build.py ou insira os links aqui -->'
    return f'''<footer class="site-footer">
  <div class="container">
    <div class="footer-grid">
      <div>
        <img class="footer-logo" src="@/assets/img/logo-elbatec-branco.svg" alt="Elbatec Controle de Pragas" width="168" height="40" loading="lazy">
        <p class="legal"><strong>{c["razao"]}</strong><br>CNPJ: {c["cnpj"]}<br>Inscrição Estadual: {c["ie"]}</p>
        <!-- PREENCHER: Licença sanitária / CVS e responsável técnico
        <p class="legal">Licença de Funcionamento (Vigilância Sanitária): Nº XXXXX<br>Responsável técnico: NOME — CRQ/CRBio/CREA Nº XXXXX</p>
        -->
        {social_html}
      </div>
      <div>
        <h2>Serviços</h2>
        <ul>{serv}<li><a href="@/produtos-saneantes.html">Produtos saneantes</a></li></ul>
      </div>
      <div>
        <h2>Institucional</h2>
        <ul>
          <li><a href="@/sobre.html">Sobre a Elbatec</a></li>
          <li><a href="@/empresas-e-condominios.html">Empresas e condomínios</a></li>
          <li><a href="@/areas-atendidas.html">Áreas atendidas</a></li>
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
          <li><a href="tel:{c["tel_link"]}">{c["tel_exibicao"]}</a></li>
          <li><a class="js-wa" href="{wa_href()}" data-msg="{esc(MSG_WA)}">WhatsApp {c["whatsapp_exibicao"]}</a></li>
          <li><a href="mailto:{c["email"]}">{c["email"]}</a></li>
          <li>{c["rua"]}<br>{c["bairro"]}, {c["cidade"]} - {c["uf"]}<br>CEP {c["cep"]}</li>
          <li>{c["horario_texto"]}</li>
        </ul>
      </div>
    </div>
    <div class="footer-bottom">
      <span>© <span class="js-year">{datetime.date.today().year}</span> {c["nome"]}. Todos os direitos reservados.</span>
      <span>Cajamar - SP e região</span>
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
    path = page["path"]
    canonical = url_abs(path)
    img = CONFIG["site_url"] + "assets/img/" + page.get("og_img", "og-elbatec.jpg")
    robots = page.get("robots", "index,follow")
    schemas = [schema_website()] + page.get("schemas", [])
    if page.get("crumbs"):
        schemas.append(schema_breadcrumb(page["crumbs"]))
    ld = "\n".join(f'  <script type="application/ld+json">{json.dumps(s, ensure_ascii=False)}</script>' for s in schemas)
    return f'''<!DOCTYPE html>
<html lang="pt-BR" class="no-js">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{esc(page["title"])}</title>
  <meta name="description" content="{esc(page["desc"])}">
  <meta name="robots" content="{robots}">
  <link rel="canonical" href="{canonical}">
  <meta name="theme-color" content="#0b2540">
  <meta property="og:type" content="{page.get("og_type", "website")}">
  <meta property="og:locale" content="pt_BR">
  <meta property="og:site_name" content="{CONFIG["nome"]}">
  <meta property="og:title" content="{esc(page["title"])}">
  <meta property="og:description" content="{esc(page["desc"])}">
  <meta property="og:url" content="{canonical}">
  <meta property="og:image" content="{img}">
  <meta property="og:image:alt" content="{esc(page.get("og_alt", "Elbatec Controle de Pragas em Cajamar - SP"))}">
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
    if not crumbs or len(crumbs) < 2:
        return ""
    li = []
    for i, (n, p) in enumerate(crumbs):
        if i == len(crumbs) - 1:
            li.append(f'<li aria-current="page">{n}</li>')
        else:
            li.append(f'<li><a href="@/{p}">{n}</a></li>')
    return f'<nav class="breadcrumb" aria-label="Você está em"><div class="container"><ol>{"".join(li)}</ol></div></nav>'

def render(page):
    path = page["path"]
    r = rel_root(path)
    if page.get("absolute_root"):         # 404: links absolutos (funciona em qualquer URL)
        r = CONFIG["site_url"]
    body = (head(page, r) + "\n" + header(page.get("active")) + "\n<main id=\"conteudo\">\n"
            + breadcrumb_html(page.get("crumbs")) + "\n" + page["body"] + "\n</main>\n" + footer()
            + f'\n<script src="{r}assets/js/main.js" defer></script>\n</body>\n</html>\n')
    body = body.replace('"@/index.html"', f'"{r or "./"}"') if not page.get("absolute_root") else body.replace('"@/index.html"', f'"{r}"')
    body = body.replace("@/", r)
    dest = os.path.join(OUT, path)
    os.makedirs(os.path.dirname(dest), exist_ok=True)
    with open(dest, "w", encoding="utf-8") as f:
        f.write(body)
    return body

# =====================================================================
# PÁGINAS DE SERVIÇO (template)
# =====================================================================
def service_page(s, path=None, crumbs=None):
    path = path or f'servicos/{s["slug"]}.html'
    rel = [x for x in SERVICOS if x["slug"] in s["relacionados"]]
    rel_html = "".join(f'''<article class="card"><div class="icon-circle">{ICONS[x["icone"]]}</div>
<h3><a href="@/servicos/{x["slug"]}.html">{x["nome"]}</a></h3><p>{x["resumo"]}</p></article>''' for x in rel)
    sinais = "".join(f"<li>{x}</li>" for x in s["sinais"])
    side_serv = "".join(f'<li><a href="@/servicos/{x["slug"]}.html"{" aria-current=\"page\"" if x is s else ""}>{x["nome_curto"]}</a></li>' for x in SERVICOS)
    steps = "".join(f"<li><h3>{t}</h3><p>{d}</p></li>" for t, d in s["passos"])
    body = f'''<section class="page-hero">
  <div class="container">
    <h1>{s["h1"]}</h1>
    <p>{s["lead"]}</p>
    <div class="btn-row">{btn_whats(msg=f"Olá! Vim pelo site e gostaria de um orçamento de {s['nome_curto'].lower()}.")}{btn_orc("Pedir orçamento", "btn btn--outline")}</div>
  </div>
</section>
<div class="section">
  <div class="container content-layout">
    <article class="prose">
      <h2>{s.get("oque_titulo") or "O que é " + s["nome_curto"].lower() + " e quando contratar"}</h2>
      {s["oque"]}
      <figure>
        <img src="@/assets/img/{s["img"]}" alt="{s["img_alt"]}" width="1200" height="675" loading="lazy" decoding="async">
        <figcaption>{s["img_cap"]}</figcaption>
      </figure>
      <h2>{s["sinais_titulo"]}</h2>
      <ul class="check-list">{sinais}</ul>
      {s.get("sinais_extra", "")}
      <h2>Como funciona o atendimento</h2>
      <ol class="steps">{steps}</ol>
      <h2>{s.get("seguranca_titulo", "Produtos registrados na ANVISA e cuidados com crianças e pets")}</h2>
      {s["seguranca"]}
      <h2>Para quem atendemos</h2>
      {s["publico"]}
      <ul class="chips"><li>Casas e sobrados</li><li>Apartamentos</li><li>Condomínios</li><li>Empresas e escritórios</li><li>Indústrias</li><li>Restaurantes e cozinhas</li><li>Comércios</li><li>Escolas</li><li>Galpões e centros de distribuição</li></ul>
      <h2>{s.get("garantia_titulo", "Garantia e certificado de execução")}</h2>
      {s["garantia"]}
      <!-- PREENCHER: prazo de garantia de {s["nome_curto"].lower()} (ex.: "garantia de XX dias"). Não publique prazo sem confirmar. -->
      <h2>Perguntas frequentes sobre {s["faq_titulo"]}</h2>
      {faq_html(s["faq"])}
      <div class="cta-box" style="margin-top:32px">
        <h2>Precisa de {s["nome_curto"].lower()} em {s.get("cta_local", "Cajamar e região")}?</h2>
        <p>Fale com a Elbatec pelo WhatsApp ou peça um orçamento pelo formulário. Atendemos residências, condomínios e empresas.</p>
        <div class="btn-row">{btn_whats(msg=f"Olá! Vim pelo site e gostaria de um orçamento de {s['nome_curto'].lower()}.")}{btn_orc("Pedir orçamento", "btn btn--light")}</div>
      </div>
    </article>
    <aside class="sidebar" aria-label="Atalhos">
      <div class="cta-box">
        <h2>Orçamento rápido</h2>
        <p>Envie fotos e o endereço pelo WhatsApp para agilizar a avaliação.</p>
        {btn_whats("WhatsApp")}
        <a class="btn btn--light" href="tel:{CONFIG["tel_link"]}">{ICONS["phone"]}<span>{CONFIG["tel_exibicao"]}</span></a>
      </div>
      <div class="card"><h2 class="h3" style="font-size:1.1rem">Outros serviços</h2><ul>{side_serv}<li><a href="@/produtos-saneantes.html">Produtos saneantes</a></li></ul></div>
      <div class="card"><h2 style="font-size:1.1rem">Onde atendemos</h2><p>Cajamar (Polvilho, Jordanésia, Centro e Ipês), Santana de Parnaíba, Caieiras, Franco da Rocha, Jundiaí, Barueri, Osasco e noroeste de São Paulo.</p><a class="card__link" href="@/areas-atendidas.html">Ver áreas atendidas</a></div>
    </aside>
  </div>
</div>
<section class="section section--alt">
  <div class="container">
    <h2>Serviços relacionados</h2>
    <div class="grid grid--3">{rel_html}</div>
    <p style="margin-top:20px">Dúvidas sobre prevenção? Leia também nosso <a href="@/blog.html">blog</a> e as <a href="@/faq.html">perguntas frequentes</a>.</p>
  </div>
</section>'''
    return {
        "path": path, "title": s["title"], "desc": s["desc"], "active": "servicos.html",
        "crumbs": crumbs or [("Início", "index.html"), ("Serviços", "servicos.html"), (s["nome"], path)],
        "schemas": [schema_service(s, path), schema_faq(s["faq"])], "body": body,
        "og_img": s["img"].replace(".webp", ".jpg"), "og_alt": s["img_alt"], "priority": "0.9", "_texto": s,
    }

def post_page(p):
    path = f'blog/{p["slug"]}.html'
    others = [x for x in POSTS if x is not p]
    outros = "".join(f'<li><a href="@/blog/{x["slug"]}.html">{x["h1"]}</a></li>' for x in others)
    data_br = datetime.date.fromisoformat(p["data"]).strftime("%d/%m/%Y")
    body = f'''<section class="page-hero"><div class="container"><h1>{p["h1"]}</h1><p>{p["lead"]}</p></div></section>
<div class="section">
  <div class="container content-layout">
    <article class="prose">
      <p class="post-meta">Publicado em <time datetime="{p["data"]}">{data_br}</time> · Elbatec Controle de Pragas</p>
      <figure><img src="@/assets/img/{p["img"]}" alt="{p["img_alt"]}" width="1200" height="675" loading="lazy" decoding="async"></figure>
      {p["corpo"]}
      <div class="cta-box" style="margin-top:32px">
        <h2>Quer uma avaliação profissional?</h2>
        <p>A Elbatec atende Cajamar e região com vistoria e orçamento sem compromisso.</p>
        <div class="btn-row">{btn_whats()}{btn_orc("Pedir orçamento", "btn btn--light")}</div>
      </div>
    </article>
    <aside class="sidebar" aria-label="Leia também">
      <div class="card"><h2 style="font-size:1.1rem">Leia também</h2><ul>{outros}</ul></div>
      <div class="card"><h2 style="font-size:1.1rem">Serviços citados</h2><ul>{"".join(f'<li><a href="@/servicos/{x}.html">{next(s["nome_curto"] for s in SERVICOS if s["slug"]==x)}</a></li>' for x in p["servicos"])}</ul></div>
    </aside>
  </div>
</div>'''
    return {"path": path, "title": p["title"], "desc": p["desc"], "active": "blog.html", "og_type": "article",
            "crumbs": [("Início", "index.html"), ("Blog", "blog.html"), (p["h1"], path)],
            "schemas": [schema_post(p, path)], "body": body, "og_img": p["img"].replace(".webp", ".jpg"),
            "og_alt": p["img_alt"], "priority": "0.6"}

# =====================================================================
# BUILD
# =====================================================================
def sitemap(pages):
    urls = []
    for p in pages:
        if p.get("robots", "").startswith("noindex"):
            continue
        urls.append(f'  <url><loc>{url_abs(p["path"])}</loc><lastmod>{HOJE}</lastmod><changefreq>{p.get("freq","monthly")}</changefreq><priority>{p.get("priority","0.7")}</priority></url>')
    xml = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + "\n".join(urls) + "\n</urlset>\n"
    open(os.path.join(OUT, "sitemap.xml"), "w", encoding="utf-8").write(xml)
    open(os.path.join(OUT, "robots.txt"), "w", encoding="utf-8").write(
        f"User-agent: *\nAllow: /\nDisallow: /_gerador/\n\nSitemap: {CONFIG['site_url']}sitemap.xml\n")

def main():
    ctx = dict(CONFIG=CONFIG, ICONS=ICONS, SERVICOS=SERVICOS, POSTS=POSTS, AREAS=AREAS, btn_whats=btn_whats,
               btn_orc=btn_orc, btn_tel=btn_tel, faq_html=faq_html, schema_localbusiness=schema_localbusiness,
               schema_faq=schema_faq, wa_href=wa_href, MSG_WA=MSG_WA)
    produtos = service_page(PRODUTOS, "produtos-saneantes.html",
                            [("Início", "index.html"), ("Produtos saneantes", "produtos-saneantes.html")])
    produtos["active"] = None
    pages = PAGINAS(ctx) + [service_page(s) for s in SERVICOS] + [produtos] + [post_page(p) for p in POSTS]
    for p in pages:
        render(p)
    sitemap(pages)
    manifest = {"name": CONFIG["nome"], "short_name": "Elbatec", "lang": "pt-BR", "start_url": "./", "scope": "./",
                "display": "standalone", "background_color": "#ffffff", "theme_color": "#0b2540",
                "icons": [{"src": "assets/img/icon-192.png", "sizes": "192x192", "type": "image/png"},
                          {"src": "assets/img/icon-512.png", "sizes": "512x512", "type": "image/png"},
                          {"src": "assets/img/icon-512.png", "sizes": "512x512", "type": "image/png", "purpose": "maskable"}]}
    json.dump(manifest, open(os.path.join(OUT, "manifest.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=2)
    print(f"{len(pages)} páginas geradas em {OUT}")
    return pages

if __name__ == "__main__":
    main()
