# Site Tango Fantasias

Site estático (HTML5 + CSS3 + JavaScript puro), pronto para o **GitHub Pages**. Não precisa de backend, banco de dados nem build.

## Estrutura

```
/
├── index.html                      Home
├── sobre.html                      Sobre a empresa
├── fantasias.html                  Catálogo (visão geral das categorias)
├── fantasias/
│   ├── fantasias-infantis.html
│   ├── fantasias-adultas.html
│   ├── fantasias-de-carnaval.html
│   ├── fantasias-de-halloween.html
│   ├── fantasias-de-festa-junina.html
│   ├── fantasias-para-escolas-e-apresentacoes.html
│   ├── acessorios-para-fantasias.html
│   └── producao-sob-encomenda.html
├── atacado.html                    Página B2B para lojistas
├── como-comprar.html               Varejo, atacado, pagamento, retirada, envio, trocas
├── faq.html
├── blog.html
├── blog/
│   ├── como-escolher-o-tamanho-da-fantasia-infantil.html
│   ├── como-montar-estoque-de-fantasias-para-o-carnaval.html
│   └── como-lavar-e-conservar-fantasias.html
├── contato.html                    Formulário + mapa + dados
├── orcamento.html                  Formulário de orçamento → WhatsApp
├── politica-de-privacidade.html    LGPD
├── termos-de-uso.html
├── 404.html
├── assets/css/style.css · assets/js/main.js · assets/img/
├── favicon.ico · manifest.json · sitemap.xml · robots.txt
├── CNAME.exemplo                   Renomeie para CNAME quando tiver domínio
└── _gerador/                       (opcional) script Python que gera todas as páginas
```

---

## 1. Antes de publicar: troque os dados provisórios

Use "Localizar e substituir em todos os arquivos" (VS Code: `Ctrl+Shift+H`):

| Procure por | Substitua por |
|---|---|
| `https://www.seudominio.com.br/` | Domínio final, com barra no fim (ou `https://SEUUSUARIO.github.io/NOMEDOREPO/`) |
| `contato@seudominio.com.br` | E-mail de contato |
| `Seg. a sex., 8h às 17h · Sáb., 8h às 13h` | Horário real (e ajuste `openingHoursSpecification` no JSON-LD) |

O WhatsApp **(11) 99238-2902** já está configurado em todas as páginas e no `assets/js/main.js`.

Depois, procure por `PREENCHER`, `CONFIRMAR` e `INSERIR DEPOIMENTOS REAIS`: são comentários HTML com o que falta completar.

> **Atalho com o gerador (opcional):** edite o bloco `CONFIG` em `_gerador/build.py` e rode `python3 build.py` dentro de `_gerador` (Python 3.12+). Os textos ficam em `content_categorias.py`, `content_paginas.py` e `content_blog.py`. As imagens provisórias são geradas por `gerar_imagens.py`.
> Se editar os `.html` à mão, **não rode o gerador depois**: ele sobrescreve as páginas.

## 2. Criar o repositório e subir os arquivos

1. Em https://github.com clique em **New repository**, dê um nome (ex.: `tango-fantasias`), deixe **Public** e crie.
2. Clique em **uploading an existing file** e arraste **o conteúdo** desta pasta (o `index.html` precisa ficar na raiz). Clique em **Commit changes**.
   - Pelo terminal: `git init && git add . && git commit -m "Site Tango Fantasias" && git branch -M main && git remote add origin https://github.com/SEUUSUARIO/tango-fantasias.git && git push -u origin main`

## 3. Ativar o GitHub Pages

**Settings → Pages → Build and deployment → Deploy from a branch → main / (root) → Save.**
Em alguns minutos o site fica em `https://SEUUSUARIO.github.io/tango-fantasias/`.
Os caminhos são relativos, com uma exceção: a página **404** usa o endereço absoluto de `site_url`. Ajuste o domínio antes de publicar.

## 4. Domínio próprio (CNAME e DNS)

1. Renomeie `CNAME.exemplo` para `CNAME`, contendo só o domínio (ex.: `www.tangofantasias.com.br`). Sem domínio, **não** crie o CNAME.
2. No registrador (Registro.br, Hostinger etc.):
   - **CNAME** `www` → `SEUUSUARIO.github.io`
   - **A** `@` → `185.199.108.153`, `185.199.109.153`, `185.199.110.153`, `185.199.111.153`
   - (opcional) **AAAA** `@` → `2606:50c0:8000::153`, `2606:50c0:8001::153`, `2606:50c0:8002::153`, `2606:50c0:8003::153`
3. **Settings → Pages → Custom domain**: digite o domínio e salve. Depois da propagação, marque **Enforce HTTPS**.

## 5. Google Search Console

1. Em https://search.google.com/search-console, adicione a propriedade e faça a verificação (DNS TXT ou meta tag no `<head>` do `index.html`).
2. Em **Sitemaps**, envie `sitemap.xml`.
3. Em **Inspeção de URL**, peça a indexação da home, do atacado e das categorias principais.

## 6. Perfil da Empresa no Google

1. Em https://business.google.com, crie o perfil **Tango Fantasias**.
2. Categoria principal sugerida: **Loja de fantasias**. Secundárias, se fizerem sentido: *Fabricante de roupas*, *Atacadista de roupas*.
3. Use **exatamente** o mesmo nome, endereço e telefone do site.
4. Informe horário, site e WhatsApp. Publique fotos reais da fábrica, da arara de produtos e da fachada, e peça avaliações a clientes reais.
5. Coloque o link do perfil em `google_perfil` (build.py) ou no rodapé.

## 7. Analytics, Google Ads e formulários

- Cada página tem no `<head>` um bloco comentado com **GTM** (opção A) ou **GA4 + Ads** (opção B). Descomente um deles e troque os IDs.
- O `main.js` dispara os eventos `clique_whatsapp`, `clique_telefone`, `envio_orcamento` e `envio_contato`. Use-os como conversões no GTM ou no Google Ads (linha `send_to` comentada no `main.js`).
- O banner LGPD chama `gtag('consent','update', ...)` (Consent Mode v2).
- Os formulários abrem o WhatsApp com a mensagem pronta. Para receber por e-mail: crie um formulário em https://formspree.io e, em `main.js`, use `usarFormspree: true` e `formspreeId`.

## 8. Fotos

As imagens em `assets/img/` são **ilustrações provisórias**. Troque-as por fotos reais mantendo o **mesmo nome de arquivo**: 1200×675 (16:9) nas categorias e no blog, 1200×900 (4:3) no hero. Use WebP com qualidade 75–80 (https://squoosh.app) e atualize também o `.jpg` de mesmo nome (1200×630, para redes sociais). Remova o texto "Imagem ilustrativa" das legendas.
**Não use fotos de personagens licenciados** (Disney, Marvel etc.) sem licença: isso traz risco jurídico e pode reprovar anúncios no Google Ads.

---

## Checklist do que falta preencher

- [ ] **Domínio** final (`site_url`, sitemap, robots, canonical) e arquivo **CNAME**
- [ ] **E-mail** de contato
- [ ] **Horário** de atendimento e se há atendimento presencial ou showroom na fábrica
- [ ] **Fotos reais** dos produtos, da fábrica e da equipe
- [ ] Lista real de **modelos** de cada categoria (comentários `CONFIRMAR`)
- [ ] **Grade de tamanhos** (e, se quiser, uma tabela de medidas)
- [ ] **Pedido mínimo** de atacado e regra de CNPJ
- [ ] **Formas de pagamento**
- [ ] **Envio**: Correios, transportadora, excursões, prazos e frete
- [ ] **Política de trocas**, incluindo peças sob encomenda
- [ ] Produção sob encomenda: quantidade mínima, peça-piloto, etiqueta própria (private label)
- [ ] **Diferenciais** da home: confirmar ou remover
- [ ] **História da empresa** (sobre.html)
- [ ] **Depoimentos reais**, com autorização
- [ ] **Redes sociais** (Instagram, Facebook, TikTok, Perfil da Empresa no Google)
- [ ] Catálogo em PDF ou link do catálogo do WhatsApp Business (opcional)
- [ ] Coordenadas **geo** exatas (JSON-LD)
- [ ] Revisão jurídica da Política de Privacidade e dos Termos
- [ ] IDs de **GA4 / GTM / Google Ads** e do **Formspree** (opcional)
