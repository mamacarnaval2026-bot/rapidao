# Site Elbatec Controle de Pragas

Site estático (HTML5 + CSS3 + JavaScript puro), pronto para o **GitHub Pages**. Não precisa de backend, banco de dados nem build.

## Estrutura

```
/
├── index.html                      Home
├── sobre.html                      Sobre a empresa
├── servicos.html                   Visão geral dos serviços
├── servicos/
│   ├── dedetizacao.html
│   ├── desratizacao.html
│   ├── descupinizacao.html
│   ├── desinsetizacao.html
│   ├── controle-de-escorpioes.html
│   ├── controle-de-pombos.html
│   ├── sanitizacao.html
│   ├── limpeza-caixa-dagua.html
│   └── limpeza-de-fossa-e-desentupimento.html
├── produtos-saneantes.html
├── areas-atendidas.html
├── empresas-e-condominios.html     Página B2B (contratos, MIP, documentação)
├── faq.html
├── blog.html
├── blog/
│   ├── como-identificar-cupins.html
│   ├── escorpioes-como-prevenir-em-casa.html
│   └── de-quanto-em-quanto-tempo-dedetizar.html
├── contato.html                    Formulário + mapa + dados
├── orcamento.html                  Formulário de orçamento → WhatsApp
├── politica-de-privacidade.html    LGPD
├── termos-de-uso.html
├── 404.html
├── assets/
│   ├── css/style.css
│   ├── js/main.js
│   └── img/                        Logo SVG, favicons, imagens WebP + JPG (Open Graph)
├── favicon.ico
├── manifest.json
├── sitemap.xml
├── robots.txt
├── CNAME.exemplo                   Renomeie para CNAME quando tiver domínio
└── _gerador/                       (opcional) script Python que gera todas as páginas
```

---

## 1. Antes de publicar: troque os dados provisórios

Os dados abaixo estão como **placeholders**. Use "Localizar e substituir em todos os arquivos" (VS Code: `Ctrl+Shift+H`):

| Procure por | Substitua por |
|---|---|
| `https://www.seudominio.com.br/` | Seu domínio final, com barra no fim (ou `https://SEUUSUARIO.github.io/NOMEDOREPO/`) |
| `5511000000000` | Número do WhatsApp: 55 + DDD + número, só dígitos |
| `(11) 00000-0000` | WhatsApp como deve aparecer no site |
| `contato@seudominio.com.br` | E-mail de contato |
| `Seg. a sex., 8h às 18h · Sáb., 8h às 12h` | Horário real (e ajuste `openingHoursSpecification` no JSON-LD) |

Depois, procure por `PREENCHER`, `CONFIRMAR` e `INSERIR DEPOIMENTOS REAIS` nos arquivos: são comentários HTML marcando o que você precisa completar.

> **Atalho com o gerador (opcional):** edite o bloco `CONFIG` em `_gerador/build.py` e rode `python3 build.py` dentro da pasta `_gerador` (Python 3.12 ou mais recente). Todas as páginas, o sitemap e o manifest são recriados de uma vez. Os textos ficam em `content_servicos.py`, `content_paginas.py` e `content_blog.py`.
> Se você editar os `.html` à mão, **não rode o gerador depois**, porque ele sobrescreve as páginas.

Em `assets/js/main.js`, ajuste também o bloco `CONFIG` (número do WhatsApp e, se quiser, o Formspree).

## 2. Criar o repositório e subir os arquivos

1. Entre em https://github.com e clique em **New repository**.
2. Dê um nome (ex.: `elbatec-site`), deixe **Public** e clique em **Create repository**.
3. Clique em **uploading an existing file**, arraste **todo o conteúdo** desta pasta (não a pasta em si: o `index.html` precisa ficar na raiz do repositório) e clique em **Commit changes**.
   - Pelo terminal: `git init && git add . && git commit -m "Site Elbatec" && git branch -M main && git remote add origin https://github.com/SEUUSUARIO/elbatec-site.git && git push -u origin main`

## 3. Ativar o GitHub Pages

1. No repositório: **Settings → Pages**.
2. Em **Build and deployment → Source**, escolha **Deploy from a branch**.
3. Branch **main**, pasta **/ (root)** → **Save**.
4. Em 1 a 5 minutos o site fica no ar em `https://SEUUSUARIO.github.io/elbatec-site/`.

Todos os caminhos são relativos, então o site funciona também nessa subpasta. A exceção é a página **404**, que usa o endereço absoluto configurado em `site_url`. Por isso, ajuste o domínio antes de publicar.

## 4. Domínio próprio (CNAME e DNS)

1. Renomeie `CNAME.exemplo` para `CNAME` e deixe nele apenas o domínio, ex.: `www.elbatec.com.br`.
   (Se não tiver domínio, **não** crie o arquivo CNAME.)
2. No painel do seu registrador (Registro.br, GoDaddy, Hostinger etc.), crie os registros DNS:
   - **CNAME** `www` → `SEUUSUARIO.github.io`
   - **A** `@` (domínio sem www) → `185.199.108.153`, `185.199.109.153`, `185.199.110.153`, `185.199.111.153`
   - (opcional) **AAAA** `@` → `2606:50c0:8000::153`, `2606:50c0:8001::153`, `2606:50c0:8002::153`, `2606:50c0:8003::153`
3. Em **Settings → Pages → Custom domain**, digite `www.seudominio.com.br` e salve.
4. Quando o DNS propagar (de minutos a 48 h), marque **Enforce HTTPS**.
5. Confirme que `site_url`, `sitemap.xml`, `robots.txt` e as tags `canonical` usam esse domínio.

## 5. Google Search Console (sitemap)

1. Acesse https://search.google.com/search-console e adicione a propriedade (**Domínio** via DNS TXT, ou **Prefixo de URL**).
2. Verifique a propriedade. No método "Tag HTML", cole a meta tag no `<head>` do `index.html`.
3. Em **Sitemaps**, envie `sitemap.xml`.
4. Em **Inspeção de URL**, peça a indexação da home e das principais páginas de serviço.

## 6. Perfil da Empresa no Google (Google Meu Negócio)

1. Acesse https://business.google.com e crie o perfil **Elbatec Controle de Pragas**.
2. Categoria principal: **Serviço de controle de pragas**. Secundárias possíveis: *Serviço de limpeza de fossas*, *Serviço de desentupimento*, *Serviço de limpeza de caixa d'água* (use apenas as que você realmente oferece).
3. Use **exatamente** o mesmo nome, endereço e telefone do site (consistência NAP).
4. Informe a área de atendimento (Cajamar, Santana de Parnaíba, Caieiras etc.), o horário, o site e os serviços.
5. Conclua a verificação, publique fotos reais da equipe e dos veículos e peça avaliações a clientes reais.
6. Depois, coloque o link do perfil em `google_perfil` (build.py) ou no rodapé.

## 7. Analytics, Google Ads e formulários

- **GA4 / GTM / Google Ads:** cada página tem no `<head>` um bloco comentado com as opções A (GTM) e B (gtag). Descomente uma delas e troque os IDs.
- **Conversões:** o `main.js` já dispara `clique_whatsapp`, `clique_telefone`, `envio_orcamento` e `envio_contato` (no `dataLayer` e no `gtag`). No GTM, crie acionadores de "Evento personalizado" com esses nomes. Para Ads direto, descomente a linha `send_to: 'AW-.../...'` em `main.js`.
- **Consentimento (LGPD):** o banner salva a escolha do usuário e chama `gtag('consent','update', ...)` (Consent Mode v2).
- **Formulários:** por padrão abrem o WhatsApp com a mensagem formatada. Para receber por e-mail, crie um formulário em https://formspree.io e, em `main.js`, use `usarFormspree: true` e `formspreeId: 'seuid'`.

## 8. Trocar as imagens

As imagens em `assets/img/` são **ilustrações provisórias**. Para trocar por fotos reais:
- Mantenha o **mesmo nome de arquivo**. Use 1200×675 px (16:9) nos serviços e no blog e 1200×900 px (4:3) no hero.
- Converta para WebP (ex.: https://squoosh.app, qualidade 75–80, até ~150 KB).
- Atualize também o `.jpg` de mesmo nome (1200×630), usado no compartilhamento em redes sociais.
- Remova das legendas o texto "Imagem ilustrativa".

---

## Checklist do que falta preencher

- [ ] Número do **WhatsApp** (HTML + `main.js`)
- [ ] **E-mail** de contato
- [ ] **Domínio** final (`site_url`, sitemap, robots, canonical) e arquivo **CNAME**
- [ ] **Horário** de atendimento real e se há plantão para emergências
- [ ] **Licença sanitária / CVS** e **responsável técnico** (sobre.html e rodapé, blocos comentados)
- [ ] **Prazo de garantia** de cada serviço (comentários `PREENCHER` nas páginas de serviço)
- [ ] **Fotos reais** (equipe, veículos, serviços) no lugar das ilustrações
- [ ] **Depoimentos reais**, com autorização dos clientes (bloco comentado na home)
- [ ] **Diferenciais** da home: confirmar ou remover cada um
- [ ] **História da empresa** em sobre.html (sem números que não possam ser comprovados)
- [ ] **Redes sociais** (Instagram, Facebook, Perfil da Empresa no Google)
- [ ] Coordenadas **geo** exatas (JSON-LD) a partir do Google Maps
- [ ] **Formas de pagamento** (faq.html)
- [ ] Equipamentos de **limpa-fossa/desentupimento** e licenças ambientais ou transportador de resíduos
- [ ] Produtos saneantes: retirada, entrega, pedido mínimo e política de troca
- [ ] Revisão de **Política de Privacidade** e **Termos** por assessoria jurídica
- [ ] IDs do **GA4 / GTM / Google Ads** e do **Formspree** (opcional)
- [ ] Revisar a lista de **áreas atendidas**
