# -*- coding: utf-8 -*-
"""Páginas institucionais, formulários, legais e 404 da Tango Fantasias."""
import datetime


def PAGINAS(ctx):
    C = ctx["CONFIG"]; I = ctx["ICONS"]; S = ctx["CATEGORIAS"]; POSTS = ctx["POSTS"]
    btn_whats = ctx["btn_whats"]; btn_orc = ctx["btn_orc"]; faq_html = ctx["faq_html"]
    LB = ctx["schema_localbusiness"](); schema_faq = ctx["schema_faq"]
    endereco = f'{C["rua"]} – {C["bairro"]}, {C["cidade"]} - {C["uf"]}, CEP {C["cep"]}'
    mapa_q = "Rua+Coronel+Em%C3%ADdio+Piedade,+73,+Br%C3%A1s,+S%C3%A3o+Paulo+-+SP,+03018-010"
    MSG_ATAC = "Olá! Vim pelo site e tenho uma loja. Gostaria de comprar fantasias no atacado."
    pages = []

    def card(s):
        return f'''<article class="card reveal"><div class="icon-circle">{I[s["icone"]]}</div>
<h3><a href="@/fantasias/{s["slug"]}.html">{s["nome"]}</a></h3><p>{s["resumo"]}</p>
<a class="card__link" href="@/fantasias/{s["slug"]}.html" aria-label="Ver {s["nome"].lower()}">Ver categoria</a></article>'''
    cards = "".join(card(s) for s in S)

    def campo(id_, label, tipo="text", req=True, extra="", data_label=None, ac=""):
        r = ' <span class="req" aria-hidden="true">*</span>' if req else ""
        return f'''<div class="field"><label for="{id_}">{label}{r}</label>
<input id="{id_}" name="{id_.split("-")[-1]}" type="{tipo}"{" required" if req else ""}{f' autocomplete="{ac}"' if ac else ""} data-label="{data_label or label}" aria-describedby="{id_}-erro" {extra}>
<span class="error" id="{id_}-erro" aria-live="polite"></span></div>'''

    def select(id_, label, opcoes, req=True):
        r = ' <span class="req" aria-hidden="true">*</span>' if req else ""
        ops = '<option value="">Selecione</option>' + "".join(f"<option>{o}</option>" for o in opcoes)
        return f'''<div class="field"><label for="{id_}">{label}{r}</label>
<select id="{id_}" name="{id_.split("-")[-1]}"{" required" if req else ""} data-label="{label}" aria-describedby="{id_}-erro">{ops}</select>
<span class="error" id="{id_}-erro" aria-live="polite"></span></div>'''

    def textarea(id_, label, req=False, ph=""):
        r = ' <span class="req" aria-hidden="true">*</span>' if req else ""
        return f'''<div class="field"><label for="{id_}">{label}{r}</label>
<textarea id="{id_}" name="mensagem"{" required" if req else ""} data-label="{label}" aria-describedby="{id_}-erro" placeholder="{ph}"></textarea>
<span class="error" id="{id_}-erro" aria-live="polite"></span></div>'''

    def aceite(pfx):
        return f'''<div class="field"><label class="check" for="{pfx}-aceite"><input id="{pfx}-aceite" name="aceite" type="checkbox" required aria-describedby="{pfx}-aceite-erro">
<span>Li e aceito a <a href="@/politica-de-privacidade.html" target="_blank" rel="noopener">Política de Privacidade</a> e autorizo o contato da Tango Fantasias. <span class="req" aria-hidden="true">*</span></span></label>
<span class="error" id="{pfx}-aceite-erro" aria-live="polite"></span></div>
<input type="text" name="_gotcha" tabindex="-1" autocomplete="off" aria-hidden="true" style="position:absolute;left:-9999px" title="Não preencha">'''

    # ================================================================ HOME
    home_faq = [
        ("Vocês vendem no atacado e no varejo?", "Sim. Somos fábrica e atendemos lojistas e revendedores no atacado e também o consumidor final no varejo."),
        ("Onde fica a fábrica?", f"Na {C['rua']}, no Brás, em São Paulo - SP, CEP {C['cep']}."),
        ("Vocês enviam para outras cidades?", "Consulte pelo WhatsApp as opções de envio para a sua cidade e o seu estado."),
        ("Fazem fantasias sob encomenda para grupos?", "Sim. Produzimos lotes padronizados para blocos, escolas, empresas e lojas, conforme quantidade e prazo."),
        ("Como faço um pedido?", "Pelo WhatsApp (11) 99238-2902, pelo formulário de orçamento ou visitando a fábrica no Brás."),
    ]
    home_body = f'''<section class="hero">
  <div class="container">
    <div>
      <h1>Fábrica de fantasias no Brás: atacado e varejo em São Paulo</h1>
      <p class="lead">Fantasias infantis e adultas para Carnaval, Halloween, festa junina, escolas e festas temáticas, com confecção própria no Brás e atendimento para lojistas e consumidor final.</p>
      <div class="btn-row">{btn_whats()}{btn_orc("Pedir orçamento", "btn btn--outline")}</div>
      <ul class="badges">
        <li>{I["factory"]}Direto da fábrica</li>
        <li>{I["store"]}Atacado e varejo</li>
        <li>{I["scissors"]}Produção sob encomenda</li>
        <li>{I["pin"]}No coração do Brás</li>
      </ul>
    </div>
    <img class="hero__img" src="@/assets/img/hero-fabrica-de-fantasias-bras.webp" alt="Fantasias coloridas em cabides na fábrica da Tango Fantasias no Brás, São Paulo" width="1200" height="900" fetchpriority="high" decoding="async">
  </div>
</section>

<section class="section" aria-labelledby="t-cat">
  <div class="container">
    <div class="section__head"><span class="eyebrow">Fantasias</span><h2 id="t-cat">Nossas linhas de fantasias</h2>
    <p>Do bebê ao adulto, para todas as datas do calendário de festas — e produção sob encomenda para quem precisa de algo exclusivo.</p></div>
    <div class="grid grid--4">{cards}</div>
  </div>
</section>

<section class="section section--alt" aria-labelledby="t-como">
  <div class="container">
    <div class="section__head"><span class="eyebrow">Como comprar</span><h2 id="t-como">Comprar fantasias da fábrica em 4 passos</h2></div>
    <ol class="steps steps--4">
      <li class="reveal"><h3>Escolha</h3><p>Veja as categorias no site, peça o catálogo pelo WhatsApp ou visite a fábrica no Brás.</p></li>
      <li class="reveal"><h3>Orçamento</h3><p>Informe modelos, tamanhos e quantidades. Lojistas, informem também o CNPJ.</p></li>
      <li class="reveal"><h3>Confirmação</h3><p>Enviamos valores, prazo e formas de pagamento por escrito.</p></li>
      <li class="reveal"><h3>Retirada ou envio</h3><p>Retire na fábrica ou combine o envio para a sua cidade.</p></li>
    </ol>
    <p style="margin-top:20px"><a href="@/como-comprar.html">Ver todas as informações sobre como comprar</a></p>
  </div>
</section>

<section class="section" aria-labelledby="t-publico">
  <div class="container">
    <div class="section__head"><span class="eyebrow">Para quem</span><h2 id="t-publico">Para lojistas e para quem vai à festa</h2></div>
    <div class="split">
      <div class="panel panel--dark reveal">
        <div class="icon-circle">{I["store"]}</div>
        <h3>Atacado para lojistas</h3>
        <ul class="check-list">
          <li>Preço de fábrica para lojas e revendedores</li>
          <li>Grades de tamanhos e reposição de modelos</li>
          <li>Coleções planejadas para Carnaval, Halloween e festa junina</li>
          <li>Produção de linhas exclusivas sob encomenda</li>
        </ul>
        <a class="btn btn--light" href="@/atacado.html">Comprar no atacado</a>
      </div>
      <div class="panel panel--light reveal">
        <div class="icon-circle" style="background:#fff">{I["star"]}</div>
        <h3>Varejo e grupos</h3>
        <ul class="check-list">
          <li>Compre uma fantasia direto da fábrica</li>
          <li>Fantasias infantis e adultas para todas as festas</li>
          <li>Pedidos para turmas de escola, blocos e empresas</li>
          <li>Atendimento rápido pelo WhatsApp</li>
        </ul>
        <a class="btn btn--primary" href="@/fantasias.html">Ver fantasias</a>
      </div>
    </div>
  </div>
</section>

<section class="section section--alt" aria-labelledby="t-porque">
  <div class="container">
    <div class="section__head"><span class="eyebrow">Diferenciais</span><h2 id="t-porque">Por que comprar da Tango Fantasias</h2></div>
    <!-- CONFIRMAR: revise os diferenciais e mantenha só os que são verdadeiros. -->
    <div class="grid grid--3">
      <div class="card reveal"><div class="icon-circle">{I["factory"]}</div><h3>Somos a fábrica</h3><p>Confecção própria, sem intermediários: mais controle de qualidade, reposição e preço de fábrica.</p></div>
      <div class="card reveal"><div class="icon-circle">{I["pin"]}</div><h3>No Brás, em São Paulo</h3><p>No maior polo atacadista de confecção da cidade, fácil para lojistas que fazem compras na região.</p></div>
      <div class="card reveal"><div class="icon-circle">{I["scissors"]}</div><h3>Produção sob encomenda</h3><p>Lotes padronizados para lojas, blocos, escolas e empresas, com cores e modelos combinados.</p></div>
      <div class="card reveal"><div class="icon-circle">{I["ruler"]}</div><h3>Grade de tamanhos</h3><p>Modelos infantis e adultos em grades pensadas para revenda. <!-- CONFIRMAR --></p></div>
      <div class="card reveal"><div class="icon-circle">{I["tag"]}</div><h3>Atacado e varejo</h3><p>Atendemos da peça única para o consumidor final ao pedido completo do lojista.</p></div>
      <div class="card reveal"><div class="icon-circle">{I["whatsapp"]}</div><h3>Atendimento pelo WhatsApp</h3><p>Orçamentos, catálogo e dúvidas resolvidos de forma rápida pelo {C["whatsapp_exibicao"]}.</p></div>
    </div>
    <!-- INSERIR DEPOIMENTOS REAIS (com autorização dos clientes). Não publique depoimentos ou notas inventados.
    <div class="grid grid--3" style="margin-top:24px">
      <blockquote class="card"><p>"Texto do depoimento real."</p><footer>— Nome do cliente, loja/cidade</footer></blockquote>
    </div>
    -->
  </div>
</section>

<section class="section" aria-labelledby="t-local">
  <div class="container split">
    <div>
      <span class="eyebrow">Onde estamos</span><h2 id="t-local">Visite a fábrica no Brás</h2>
      <p>Estamos na {C["rua"]}, no Brás, região central de São Paulo, a poucos minutos das principais ruas de compras do polo atacadista. Lojistas de São Paulo e de outras cidades podem retirar os pedidos na fábrica ou combinar o envio.</p>
      <ul class="info-list">
        <li>{I["pin"]}<div>{endereco}</div></li>
        <li>{I["clock"]}<div>{C["horario_texto"]}</div></li>
        <li>{I["whatsapp"]}<div><a class="js-wa" href="{ctx["wa_href"]()}" data-msg="{ctx["MSG_WA"]}">{C["whatsapp_exibicao"]}</a></div></li>
      </ul>
      <p><a class="btn btn--outline" href="@/contato.html">Ver mapa e contato</a></p>
    </div>
    <img src="@/assets/img/fabrica-de-fantasias-producao.webp" alt="Confecção da Tango Fantasias no Brás com tecidos coloridos" width="1200" height="675" loading="lazy" decoding="async" style="border-radius:14px">
  </div>
</section>

<section class="section section--alt" aria-labelledby="t-faq">
  <div class="container">
    <div class="section__head"><span class="eyebrow">Dúvidas</span><h2 id="t-faq">Perguntas frequentes</h2></div>
    {faq_html(home_faq)}
    <p style="margin-top:20px"><a href="@/faq.html">Ver todas as perguntas frequentes</a></p>
  </div>
</section>

<section class="cta-final">
  <div class="container">
    <h2>Monte seu pedido direto com a fábrica</h2>
    <p>Atacado para lojistas, varejo para o consumidor final e produção sob encomenda para grupos e eventos.</p>
    <div class="btn-row">{btn_whats()}{btn_orc("Pedir orçamento", "btn btn--light")}</div>
  </div>
</section>'''
    pages.append({"path": "index.html", "title": "Fábrica de Fantasias no Brás SP | Tango Fantasias",
                  "desc": "Fábrica de fantasias no Brás, São Paulo: fantasias infantis e adultas para Carnaval, Halloween e festa junina, no atacado e varejo. Peça orçamento no WhatsApp.",
                  "active": "index.html", "crumbs": [("Início", "index.html")], "schemas": [LB], "body": home_body,
                  "priority": "1.0", "freq": "weekly",
                  "preload": '<link rel="preload" as="image" href="assets/img/hero-fabrica-de-fantasias-bras.webp" type="image/webp" fetchpriority="high">'})

    # ================================================================ SOBRE
    sobre_body = f'''<section class="page-hero"><div class="container"><h1>Sobre a Tango Fantasias</h1>
<p>Indústria e comércio de fantasias no Brás, em São Paulo: confecção própria e venda no atacado e no varejo.</p></div></section>
<div class="section"><div class="container content-layout">
<article class="prose">
  <h2>Quem somos</h2>
  <p>A <strong>{C["razao"]}</strong>, inscrita no CNPJ {C["cnpj"]}, é uma confecção de fantasias instalada no Brás, o maior polo atacadista de moda de São Paulo. Nossa atividade principal é a confecção de peças de vestuário, e também atuamos no comércio atacadista e varejista de artigos do vestuário e acessórios.</p>
  <p>Na prática, isso quer dizer que fabricamos as fantasias que vendemos. Cuidamos da escolha dos tecidos, da modelagem, do corte, da costura e do acabamento, e vendemos tanto para lojistas e revendedores de todo o país quanto para o consumidor que quer comprar direto da fábrica.</p>
  <!-- PREENCHER: história da empresa (ano de início real, fundadores, trajetória). Não publique números que não possam ser comprovados. -->
  <figure><img src="@/assets/img/equipe-tango-fantasias.webp" alt="Equipe da Tango Fantasias na confecção, no Brás" width="1200" height="675" loading="lazy" decoding="async">
  <figcaption>Imagem ilustrativa — substitua por uma foto real da equipe ou da fábrica.</figcaption></figure>
  <h2>O que fazemos</h2>
  <ul class="check-list">
    <li><strong>Confecção de fantasias</strong> infantis e adultas para Carnaval, Halloween, festa junina, escolas e festas temáticas.</li>
    <li><strong>Atacado</strong> para lojas de fantasias, lojas de festas, locadoras e revendedores.</li>
    <li><strong>Varejo</strong> para o consumidor final, direto da fábrica.</li>
    <li><strong>Produção sob encomenda</strong> de lotes para lojas, blocos, escolas e empresas.</li>
    <li><strong>Acessórios</strong> para completar fantasias.</li>
  </ul>
  <h2>Como trabalhamos</h2>
  <p>Acreditamos que uma boa fantasia precisa ser bonita na foto, confortável na festa e durar mais de um uso. Por isso, acompanhamos a produção de perto e mantemos um padrão entre os lotes — o que é essencial para o lojista que precisa repor um modelo que vendeu bem.</p>
  <p>Também respeitamos a propriedade intelectual: trabalhamos com modelos de criação própria e temas genéricos e não produzimos personagens de marcas registradas sem licença.</p>
  <h2>Dados da empresa</h2>
  <ul>
    <li>Razão social: {C["razao"]}</li>
    <li>Nome fantasia: {C["nome"]}</li>
    <li>CNPJ: {C["cnpj"]}</li>
    <li>Inscrição Estadual (SP): {C["ie"]}</li>
    <li>Endereço: {endereco}</li>
    <li>Telefone e WhatsApp: <a href="tel:{C["tel_link"]}">{C["tel_exibicao"]}</a></li>
  </ul>
  <div class="btn-row">{btn_whats()}{btn_orc()}</div>
</article>
<aside class="sidebar" aria-label="Atalhos"><div class="cta-box"><h2>Fale com a gente</h2><p>{C["horario_texto"]}</p>{btn_whats("WhatsApp")}<a class="btn btn--light" href="@/atacado.html">Comprar no atacado</a></div>
<div class="card"><h2 style="font-size:1.1rem">Categorias</h2><ul>{"".join(f'<li><a href="@/fantasias/{s["slug"]}.html">{s["nome_curto"]}</a></li>' for s in S)}</ul></div></aside>
</div></div>'''
    pages.append({"path": "sobre.html", "title": "Sobre a Tango Fantasias | Fábrica no Brás, SP",
                  "desc": "Conheça a Tango Fantasias, indústria e comércio de fantasias no Brás, São Paulo, com confecção própria e venda no atacado e no varejo. Fale com a gente.",
                  "active": "sobre.html", "crumbs": [("Início", "index.html"), ("Sobre", "sobre.html")], "body": sobre_body, "priority": "0.6"})

    # ================================================================ FANTASIAS (catálogo)
    cat_body = f'''<section class="page-hero"><div class="container"><h1>Fantasias no Atacado e Varejo</h1>
<p>Conheça as linhas de fantasias da Tango: infantis, adultas, Carnaval, Halloween, festa junina, escolas, acessórios e produção sob encomenda.</p>
<div class="btn-row">{btn_whats("Pedir catálogo no WhatsApp", "Olá! Vim pelo site e gostaria de receber o catálogo de fantasias.")}{btn_orc("Pedir orçamento", "btn btn--outline")}</div></div></section>
<section class="section"><div class="container">
  <div class="section__head"><h2>Por público</h2></div>
  <div class="grid grid--2">{card(S[0])}{card(S[1])}</div>
</div></section>
<section class="section section--alt"><div class="container">
  <div class="section__head"><h2>Por data e ocasião</h2><p>Coleções planejadas para as temporadas de maior procura.</p></div>
  <div class="grid grid--4">{"".join(card(s) for s in S[2:6])}</div>
</div></section>
<section class="section"><div class="container">
  <div class="section__head"><h2>Acessórios e produção</h2></div>
  <div class="grid grid--2">{card(S[6])}{card(S[7])}</div>
</div></section>
<section class="section section--alt"><div class="container prose">
  <h2>Catálogo atualizado pelo WhatsApp</h2>
  <p>Os modelos disponíveis mudam conforme a temporada. Para ver o catálogo completo, com fotos, tamanhos e disponibilidade, chame a gente no WhatsApp ou visite a fábrica no Brás. Lojistas recebem as condições de <a href="@/atacado.html">atacado</a> e podem programar pedidos antecipados para Carnaval, Halloween e festa junina.</p>
  <!-- PREENCHER (opcional): link para catálogo em PDF ou para o WhatsApp Business (catálogo). Ex.: <a href="assets/catalogo-tango.pdf">Baixar catálogo (PDF)</a> -->
  <p><strong>Sobre personagens:</strong> trabalhamos com criação própria e temas genéricos. Personagens de marcas registradas só podem ser produzidos com licença dos detentores dos direitos.</p>
</div></section>
<section class="cta-final"><div class="container"><h2>Não encontrou o modelo que procura?</h2><p>Envie uma referência: avaliamos a produção sob encomenda para o seu pedido.</p><div class="btn-row">{btn_whats()}{btn_orc("Pedir orçamento", "btn btn--light")}</div></div></section>'''
    pages.append({"path": "fantasias.html", "title": "Fantasias no Atacado e Varejo | Tango Fantasias",
                  "desc": "Veja as fantasias da Tango: infantis, adultas, Carnaval, Halloween, festa junina, escolas e acessórios. Atacado e varejo direto da fábrica no Brás, SP.",
                  "active": "fantasias.html", "crumbs": [("Início", "index.html"), ("Fantasias", "fantasias.html")],
                  "schemas": [{"@context": "https://schema.org", "@type": "ItemList", "name": "Categorias de fantasias",
                               "itemListElement": [{"@type": "ListItem", "position": i + 1, "name": s["nome"], "url": C["site_url"] + "fantasias/" + s["slug"] + ".html"} for i, s in enumerate(S)]}],
                  "body": cat_body, "priority": "0.9"})

    # ================================================================ ATACADO
    atac_faq = [
        ("Preciso ter CNPJ para comprar no atacado?", "Informe seu CNPJ no pedido. As condições de atacado e a necessidade de CNPJ são confirmadas no orçamento. <!-- CONFIRMAR regra -->"),
        ("Qual é o pedido mínimo?", "O pedido mínimo é informado no orçamento e pode variar conforme o modelo e a temporada. <!-- PREENCHER: pedido mínimo real -->"),
        ("Vocês enviam para outros estados?", "Consulte pelo WhatsApp as opções de envio. Também é possível retirar na fábrica, no Brás."),
        ("Posso fazer pedido antecipado de Carnaval?", "Sim, e recomendamos. Pedidos antecipados garantem modelos, cores e grades de tamanho."),
        ("Quais formas de pagamento vocês aceitam?", "As formas de pagamento são informadas no orçamento. <!-- PREENCHER: PIX, cartão, boleto etc. -->"),
        ("Vocês emitem nota fiscal?", "Sim, emitimos nota fiscal nas vendas."),
    ]
    atac_body = f'''<section class="page-hero"><div class="container"><h1>Fantasias no Atacado para Lojistas</h1>
<p>Compre direto da fábrica no Brás: fantasias infantis e adultas, coleções de temporada, acessórios e produção de linhas exclusivas para a sua loja.</p>
<div class="btn-row">{btn_whats("Quero comprar no atacado", MSG_ATAC)}{btn_orc("Enviar pedido de orçamento", "btn btn--outline")}</div></div></section>
<section class="section"><div class="container">
  <div class="section__head"><h2>Vantagens de comprar da fábrica</h2></div>
  <div class="grid grid--3">
    <div class="card reveal"><div class="icon-circle">{I["factory"]}</div><h3>Preço de fábrica</h3><p>Sem intermediários entre a confecção e a sua loja.</p></div>
    <div class="card reveal"><div class="icon-circle">{I["box"]}</div><h3>Reposição de modelos</h3><p>Como produzimos as peças, fica mais fácil repor os modelos que vendem bem.</p></div>
    <div class="card reveal"><div class="icon-circle">{I["scissors"]}</div><h3>Linhas exclusivas</h3><p>Produção sob encomenda de modelos e cores para a sua loja. <!-- CONFIRMAR --></p></div>
  </div>
</div></section>
<section class="section section--alt"><div class="container content-layout">
<article class="prose">
  <h2>Para quem é o atacado da Tango</h2>
  <p>Atendemos lojas de fantasias, lojas de artigos de festa, locadoras de fantasias, armarinhos, lojas de presentes, e-commerces, revendedores e sacoleiros que compram no Brás. Também atendemos compras institucionais de escolas, buffets, produtoras e empresas.</p>
  <h2>Como funciona a compra no atacado</h2>
  <ol>
    <li><strong>Contato:</strong> chame no WhatsApp {C["whatsapp_exibicao"]} e informe o nome da loja, o CNPJ e a cidade.</li>
    <li><strong>Catálogo:</strong> enviamos os modelos disponíveis, com grades de tamanho e condições.</li>
    <li><strong>Pedido:</strong> você monta o pedido por modelo, tamanho e quantidade.</li>
    <li><strong>Confirmação:</strong> enviamos valores, prazo e forma de pagamento por escrito.</li>
    <li><strong>Retirada ou envio:</strong> retire na fábrica, no Brás, ou combine o envio. <!-- CONFIRMAR modalidades --></li>
  </ol>
  <h2>Calendário de vendas para lojistas</h2>
  <p>O mercado de fantasias tem picos bem definidos. Planejar os pedidos com antecedência é a forma mais segura de ter os modelos certos no momento em que o cliente procura:</p>
  <ul class="check-list">
    <li><a href="@/fantasias/fantasias-de-carnaval.html"><strong>Carnaval</strong></a> — a maior temporada do ano; programe o pedido com meses de antecedência.</li>
    <li><a href="@/fantasias/fantasias-de-festa-junina.html"><strong>Festa junina</strong></a> — alta procura por tamanhos infantis entre maio e julho.</li>
    <li><a href="@/fantasias/fantasias-de-halloween.html"><strong>Halloween</strong></a> — estoque pronto no início de outubro.</li>
    <li><strong>Dia das Crianças, festas escolares e fim de ano</strong> — boa saída de <a href="@/fantasias/fantasias-infantis.html">fantasias infantis</a> e <a href="@/fantasias/acessorios-para-fantasias.html">acessórios</a>.</li>
  </ul>
  <p>Veja mais dicas no artigo <a href="@/blog/como-montar-estoque-de-fantasias-para-o-carnaval.html">como montar estoque de fantasias para o Carnaval</a>.</p>
  <h2>Condições comerciais</h2>
  <div class="todo-box">
    <!-- PREENCHER: pedido mínimo (em peças ou valor), formas de pagamento, prazo de separação/produção, política de troca para lojistas e modalidades de envio. -->
    <p>Pedido mínimo, formas de pagamento, prazos e envio são informados no orçamento. Fale com a gente pelo WhatsApp.</p>
  </div>
  <h2>Perguntas frequentes de lojistas</h2>
  {faq_html(atac_faq)}
</article>
<aside class="sidebar" aria-label="Comprar no atacado"><div class="cta-box"><h2>Atendimento ao lojista</h2><p>Informe o nome da loja, o CNPJ e a cidade para receber o catálogo e as condições.</p>{btn_whats("WhatsApp do atacado", MSG_ATAC)}<a class="btn btn--light" href="@/orcamento.html">Formulário de orçamento</a></div>
<div class="card"><h2 style="font-size:1.1rem">Categorias</h2><ul>{"".join(f'<li><a href="@/fantasias/{s["slug"]}.html">{s["nome_curto"]}</a></li>' for s in S)}</ul></div></aside>
</div></section>
<section class="cta-final"><div class="container"><h2>Abasteça sua loja direto da fábrica</h2><p>Fantasias infantis e adultas, coleções de temporada e acessórios no atacado.</p><div class="btn-row">{btn_whats("Quero comprar no atacado", MSG_ATAC)}{btn_orc("Pedir orçamento", "btn btn--light")}</div></div></section>'''
    pages.append({"path": "atacado.html", "title": "Fantasias no Atacado para Lojistas | Brás SP",
                  "desc": "Fantasias no atacado direto da fábrica no Brás, São Paulo: preço de fábrica, reposição e coleções de Carnaval, Halloween e festa junina. Fale com a gente.",
                  "active": "atacado.html", "crumbs": [("Início", "index.html"), ("Atacado", "atacado.html")],
                  "schemas": [schema_faq(atac_faq)], "body": atac_body, "priority": "0.9"})

    # ================================================================ COMO COMPRAR
    como_body = f'''<section class="page-hero"><div class="container"><h1>Como Comprar Fantasias na Tango</h1>
<p>Compre pelo WhatsApp, pelo formulário ou direto na fábrica no Brás. Veja como funcionam pedidos, pagamento, retirada e envio.</p></div></section>
<section class="section"><div class="container content-layout">
<article class="prose">
  <h2>Formas de comprar</h2>
  <div class="grid grid--3" style="margin-bottom:24px">
    <div class="card"><div class="icon-circle">{I["whatsapp"]}</div><h3>WhatsApp</h3><p>Peça o catálogo, tire dúvidas e feche o pedido pelo {C["whatsapp_exibicao"]}.</p></div>
    <div class="card"><div class="icon-circle">{I["store"]}</div><h3>Na fábrica</h3><p>Visite-nos na {C["rua"]}, no Brás. <!-- CONFIRMAR se há atendimento presencial/showroom --></p></div>
    <div class="card"><div class="icon-circle">{I["box"]}</div><h3>Formulário</h3><p>Envie seu pedido pelo <a href="@/orcamento.html">formulário de orçamento</a>.</p></div>
  </div>
  <h2>Atacado ou varejo?</h2>
  <p><strong>Varejo:</strong> para quem vai usar a fantasia. Você pode comprar uma peça ou algumas unidades, direto da fábrica.</p>
  <p><strong>Atacado:</strong> para lojas e revendedores, com condições de fábrica. Veja a página de <a href="@/atacado.html">atacado para lojistas</a>.</p>
  <p><strong>Encomenda:</strong> para grupos, escolas, blocos, empresas e lojas que precisam de modelos específicos. Veja a <a href="@/fantasias/producao-sob-encomenda.html">produção sob encomenda</a>.</p>
  <h2>Tamanhos</h2>
  <p>Cada modelo tem sua própria grade de tamanhos. Antes de fechar o pedido, confirme as medidas com a nossa equipe. Para fantasias infantis, veja o guia <a href="@/blog/como-escolher-o-tamanho-da-fantasia-infantil.html">como escolher o tamanho da fantasia infantil</a>.</p>
  <!-- PREENCHER (opcional): tabela de medidas real por tamanho. -->
  <h2>Pagamento</h2>
  <div class="todo-box"><!-- PREENCHER: formas de pagamento aceitas (PIX, cartão de crédito/débito, boleto, dinheiro) e condições para lojistas. -->
  <p>As formas de pagamento são informadas no orçamento.</p></div>
  <h2>Retirada e envio</h2>
  <p>Os pedidos podem ser retirados na fábrica, no Brás, em horário combinado. Para outras cidades e estados, consulte as opções de envio. <!-- PREENCHER: Correios, transportadora, motoboy, excursões/guias de compras do Brás, prazos e quem paga o frete. --></p>
  <h2>Trocas e devoluções</h2>
  <p>Seguimos o Código de Defesa do Consumidor. Confira as condições no momento da compra e guarde a nota fiscal. Peças com defeito de fabricação são analisadas pela nossa equipe. <!-- PREENCHER: política de trocas (prazo, condições, peças personalizadas sob encomenda) --></p>
  <h2>Nota fiscal</h2>
  <p>Emitimos nota fiscal nas vendas. Para compras de empresas, escolas e lojistas, informe os dados de faturamento no pedido.</p>
</article>
<aside class="sidebar" aria-label="Atendimento"><div class="cta-box"><h2>Pronto para pedir?</h2><p>{C["horario_texto"]}</p>{btn_whats("WhatsApp")}<a class="btn btn--light" href="@/orcamento.html">Formulário de orçamento</a></div></aside>
</div></section>'''
    pages.append({"path": "como-comprar.html", "title": "Como Comprar Fantasias | Tango Fantasias, Brás",
                  "desc": "Saiba como comprar fantasias da Tango: pedido pelo WhatsApp ou na fábrica no Brás, atacado e varejo, tamanhos, pagamento, retirada e envio. Veja aqui.",
                  "active": "como-comprar.html", "crumbs": [("Início", "index.html"), ("Como comprar", "como-comprar.html")],
                  "body": como_body, "priority": "0.8"})

    # ================================================================ FAQ
    faq_geral = home_faq + [
        ("Vocês têm loja física?", f"Atendemos na fábrica, na {C['rua']}, no Brás. Confirme o horário pelo WhatsApp antes de ir. <!-- CONFIRMAR -->"),
        ("Qual é o pedido mínimo no atacado?", "O pedido mínimo é informado no orçamento e pode variar conforme o modelo e a temporada."),
        ("Vocês fazem fantasias de personagens famosos?", "Trabalhamos com criação própria e temas genéricos. Personagens de marcas registradas dependem de licença dos detentores dos direitos."),
        ("Com quanta antecedência devo pedir para o Carnaval?", "Quanto antes, melhor. Para lojistas e blocos, recomendamos programar o pedido com meses de antecedência."),
        ("Como escolho o tamanho certo?", "Confira as medidas com a nossa equipe antes da compra. No blog, há um guia para fantasias infantis."),
        ("Quais formas de pagamento vocês aceitam?", "As condições de pagamento são informadas no orçamento. <!-- PREENCHER -->"),
        ("Vocês emitem nota fiscal?", "Sim, emitimos nota fiscal nas vendas."),
        ("Como lavar e guardar a fantasia?", "Siga a etiqueta. Em geral, lave à mão com água fria, sem torcer, seque à sombra e guarde em local seco. Veja dicas no blog."),
        ("Fazem figurinos para escolas?", "Sim. Produzimos lotes para turmas, apresentações e datas comemorativas."),
        ("Posso trocar uma fantasia?", "As trocas seguem o Código de Defesa do Consumidor e as condições informadas na compra."),
    ]
    faq_body = f'''<section class="page-hero"><div class="container"><h1>Perguntas Frequentes sobre Fantasias</h1>
<p>Atacado, varejo, tamanhos, prazos, envio, encomendas e cuidados com as fantasias da Tango.</p></div></section>
<section class="section"><div class="container content-layout">
<div class="prose">{faq_html(faq_geral)}
<p style="margin-top:24px">Não encontrou sua dúvida? Veja as perguntas de cada <a href="@/fantasias.html">categoria</a> ou fale com a gente.</p></div>
<aside class="sidebar" aria-label="Contato"><div class="cta-box"><h2>Ainda com dúvidas?</h2><p>Nossa equipe responde pelo WhatsApp.</p>{btn_whats("WhatsApp", "Olá! Vim pelo site e tenho uma dúvida.")}</div></aside>
</div></section>'''
    pages.append({"path": "faq.html", "title": "Perguntas Frequentes | Tango Fantasias",
                  "desc": "Tire suas dúvidas sobre compra de fantasias no atacado e varejo, tamanhos, prazos, envio, encomendas e cuidados com as peças da Tango Fantasias, no Brás.",
                  "crumbs": [("Início", "index.html"), ("Perguntas frequentes", "faq.html")],
                  "schemas": [schema_faq(faq_geral)], "body": faq_body, "priority": "0.7"})

    # ================================================================ BLOG
    posts_cards = "".join(f'''<article class="card post-card reveal">
<img src="@/assets/img/{p["img"]}" alt="{p["img_alt"]}" width="1200" height="675" loading="lazy" decoding="async">
<p class="post-meta"><time datetime="{p["data"]}">{datetime.date.fromisoformat(p["data"]).strftime("%d/%m/%Y")}</time></p>
<h2 style="font-size:1.25rem"><a href="@/blog/{p["slug"]}.html">{p["h1"]}</a></h2><p>{p["resumo"]}</p>
<a class="card__link" href="@/blog/{p["slug"]}.html" aria-label="Ler o artigo: {p["h1"]}">Ler artigo</a></article>''' for p in POSTS)
    blog_body = f'''<section class="page-hero"><div class="container"><h1>Blog da Tango Fantasias</h1>
<p>Dicas para escolher, cuidar e vender fantasias: guias de tamanhos, conservação e planejamento de estoque para lojistas.</p></div></section>
<section class="section"><div class="container"><div class="grid grid--3">{posts_cards}</div></div></section>
<!-- Para adicionar artigos: inclua um item em _gerador/content_blog.py e rode python3 build.py (ou copie um arquivo de /blog/ e ajuste). -->'''
    pages.append({"path": "blog.html", "title": "Blog Tango Fantasias | Dicas sobre Fantasias",
                  "desc": "Dicas da Tango Fantasias: como escolher o tamanho da fantasia infantil, como conservar fantasias e como montar o estoque de Carnaval da sua loja. Leia já.",
                  "active": "blog.html", "crumbs": [("Início", "index.html"), ("Blog", "blog.html")],
                  "schemas": [{"@context": "https://schema.org", "@type": "Blog", "name": "Blog Tango Fantasias", "url": C["site_url"] + "blog.html",
                               "blogPost": [{"@type": "BlogPosting", "headline": p["h1"], "url": C["site_url"] + "blog/" + p["slug"] + ".html", "datePublished": p["data"]} for p in POSTS]}],
                  "body": blog_body, "priority": "0.6", "freq": "weekly"})

    # ================================================================ CONTATO
    contato_body = f'''<section class="page-hero"><div class="container"><h1>Contato da Tango Fantasias no Brás</h1>
<p>Fale com a fábrica pelo WhatsApp, telefone, e-mail ou formulário. Estamos no Brás, em São Paulo.</p></div></section>
<section class="section"><div class="container split">
  <div>
    <h2>Fale conosco</h2>
    <ul class="info-list">
      <li>{I["whatsapp"]}<div><strong>WhatsApp</strong><br><a class="js-wa" href="{ctx["wa_href"]()}" data-msg="{ctx["MSG_WA"]}">{C["whatsapp_exibicao"]}</a></div></li>
      <li>{I["phone"]}<div><strong>Telefone</strong><br><a href="tel:{C["tel_link"]}">{C["tel_exibicao"]}</a></div></li>
      <li>{I["mail"]}<div><strong>E-mail</strong><br><a href="mailto:{C["email"]}">{C["email"]}</a></div></li>
      <li>{I["pin"]}<div><strong>Endereço</strong><br>{endereco}</div></li>
      <li>{I["clock"]}<div><strong>Horário de atendimento</strong><br>{C["horario_texto"]}<!-- CONFIRMAR horário --></div></li>
    </ul>
    <div class="map-wrap" style="margin-top:20px">
      <iframe src="https://www.google.com/maps?q={mapa_q}&amp;output=embed" title="Mapa: localização da Tango Fantasias no Brás, São Paulo" loading="lazy" referrerpolicy="no-referrer-when-downgrade" allowfullscreen></iframe>
    </div>
    <p class="form-note" style="margin-top:8px"><a href="https://www.google.com/maps/search/?api=1&amp;query={mapa_q}" target="_blank" rel="noopener">Abrir no Google Maps</a></p>
  </div>
  <div>
    <h2>Envie uma mensagem</h2>
    <form class="form" data-form="contato" novalidate action="https://formspree.io/f/SEU_ID_FORMSPREE" method="POST">
      <!-- Por padrão o envio abre o WhatsApp com os dados (ver assets/js/main.js). Para receber por e-mail, ative o Formspree no main.js. -->
      {campo("c-nome", "Nome", ac="name")}
      <div class="row-2">{campo("c-telefone", "Telefone/WhatsApp", "tel", ac="tel", extra='inputmode="tel" placeholder="(11) 91234-5678"')}{campo("c-email", "E-mail", "email", req=False, ac="email")}</div>
      {textarea("c-mensagem", "Mensagem", True)}
      {aceite("c")}
      <button class="btn btn--whats" type="submit">{I["whatsapp"]}<span>Enviar pelo WhatsApp</span></button>
      <p class="form-status" role="status" aria-live="polite"></p>
      <p class="form-note">Campos com * são obrigatórios. Seus dados são usados apenas para responder ao seu contato.</p>
    </form>
  </div>
</div></section>'''
    pages.append({"path": "contato.html", "title": "Contato | Tango Fantasias no Brás, São Paulo",
                  "desc": "Fale com a Tango Fantasias: WhatsApp (11) 99238-2902, e-mail e endereço da fábrica no Brás, São Paulo. Atendimento para lojistas e consumidor final.",
                  "active": "contato.html", "crumbs": [("Início", "index.html"), ("Contato", "contato.html")],
                  "schemas": [LB], "body": contato_body, "priority": "0.8"})

    # ================================================================ ORÇAMENTO
    orc_body = f'''<section class="page-hero"><div class="container"><h1>Orçamento de Fantasias: Atacado e Varejo</h1>
<p>Preencha e envie direto para o nosso WhatsApp. Quanto mais detalhes, mais rápido e preciso será o orçamento.</p></div></section>
<section class="section"><div class="container content-layout">
  <form class="form" data-form="orcamento" novalidate action="https://formspree.io/f/SEU_ID_FORMSPREE" method="POST">
    <!-- Por padrão o envio abre o WhatsApp com todos os dados formatados (ver assets/js/main.js).
         Alternativa por e-mail: em main.js, defina usarFormspree: true e formspreeId. -->
    <h2 style="font-size:1.3rem;margin:0">Seus dados</h2>
    {campo("o-nome", "Nome completo", ac="name")}
    <div class="row-2">{campo("o-telefone", "Telefone/WhatsApp", "tel", ac="tel", extra='inputmode="tel" placeholder="(11) 91234-5678"')}{campo("o-email", "E-mail", "email", ac="email")}</div>
    <div class="row-2">{campo("o-cidade", "Cidade/UF", extra='placeholder="Ex.: São Paulo - SP"')}{campo("o-cnpj", "CNPJ (lojistas)", req=False, extra='inputmode="numeric" placeholder="Opcional"')}</div>
    <h2 style="font-size:1.3rem;margin:8px 0 0">Sobre o pedido</h2>
    <div class="row-2">
      {select("o-perfil", "Tipo de compra", ["Atacado (loja/revenda)", "Varejo (uso próprio)", "Escola / grupo de dança ou teatro", "Bloco / escola de samba", "Empresa / evento", "Produção sob encomenda / marca própria"])}
      {select("o-categoria", "Categoria", [s["nome"] for s in S] + ["Várias categorias", "Ainda não sei"])}
    </div>
    <div class="row-2">{campo("o-quantidade", "Quantidade aproximada (peças)", "number", req=False, data_label="Quantidade aproximada", extra='min="1" step="1" inputmode="numeric" placeholder="Ex.: 50"')}{campo("o-tamanhos", "Tamanhos / faixa etária", req=False, extra='placeholder="Ex.: 4 a 10 anos; P, M e G"')}</div>
    {campo("o-data", "Data em que precisa das peças", "date", req=False, data_label="Data de que precisa")}
    {textarea("o-mensagem", "Mensagem", False, "Modelos de interesse, cores, referência, forma de entrega...")}
    {aceite("o")}
    <button class="btn btn--whats" type="submit">{I["whatsapp"]}<span>Enviar orçamento pelo WhatsApp</span></button>
    <p class="form-status" role="status" aria-live="polite"></p>
    <p class="form-note">Campos com * são obrigatórios. Ao enviar, o WhatsApp abrirá com a mensagem pronta — basta tocar em "Enviar".</p>
  </form>
  <aside class="sidebar" aria-label="Outras formas de contato">
    <div class="cta-box"><h2>Prefere falar agora?</h2><p>{C["horario_texto"]}</p>{btn_whats("WhatsApp")}<a class="btn btn--light" href="tel:{C["tel_link"]}">{I["phone"]}<span>{C["tel_exibicao"]}</span></a></div>
    <div class="card"><h2 style="font-size:1.1rem">Dica para agilizar</h2><p>Envie fotos de referência pelo WhatsApp e informe a data do evento. Para lojistas, informe o CNPJ.</p></div>
  </aside>
</div></section>'''
    pages.append({"path": "orcamento.html", "title": "Orçamento de Fantasias no Atacado | Tango",
                  "desc": "Peça orçamento de fantasias no atacado, varejo ou sob encomenda direto com a fábrica no Brás, São Paulo. Preencha e envie pelo WhatsApp em poucos minutos.",
                  "crumbs": [("Início", "index.html"), ("Orçamento", "orcamento.html")], "body": orc_body, "priority": "0.8"})

    # ================================================================ POLÍTICA
    hoje_br = datetime.date.today().strftime("%d/%m/%Y")
    pol_body = f'''<section class="page-hero"><div class="container"><h1>Política de Privacidade</h1><p>Como a Tango Fantasias trata os seus dados pessoais, em conformidade com a Lei Geral de Proteção de Dados (Lei nº 13.709/2018).</p></div></section>
<section class="section"><div class="container prose">
<p><em>Última atualização: {hoje_br}</em></p>
<!-- REVISAR com assessoria jurídica antes de publicar. -->
<h2>1. Quem é o controlador dos dados</h2>
<p>{C["razao"]}, CNPJ {C["cnpj"]}, com sede na {endereco} ("Tango Fantasias"), é a controladora dos dados pessoais coletados neste site.</p>
<h2>2. Quais dados coletamos</h2>
<ul><li><strong>Dados que você informa:</strong> nome, telefone/WhatsApp, e-mail, cidade/UF, CNPJ (lojistas), tipo de compra, categoria, quantidades, tamanhos, data e mensagem, quando preenche nossos formulários ou entra em contato.</li>
<li><strong>Dados de navegação:</strong> se você aceitar cookies, ferramentas como Google Analytics e Google Ads podem coletar dados como páginas visitadas, tipo de dispositivo, cidade aproximada e interações (por exemplo, cliques no WhatsApp).</li></ul>
<h2>3. Para que usamos os dados</h2>
<ul><li>Responder contatos e elaborar orçamentos;</li><li>Processar pedidos, emitir nota fiscal e organizar retirada ou envio;</li><li>Cumprir obrigações legais, fiscais e regulatórias;</li><li>Medir o desempenho do site e de campanhas de publicidade, quando houver consentimento.</li></ul>
<h2>4. Bases legais</h2>
<p>Tratamos dados com base na execução de contrato ou de procedimentos preliminares (orçamento), no cumprimento de obrigação legal, no legítimo interesse (para melhorar o atendimento, respeitando seus direitos) e no consentimento (cookies de análise e publicidade).</p>
<h2>5. Envio pelo WhatsApp</h2>
<p>Ao enviar os formulários, seus dados são montados em uma mensagem e abertos no aplicativo WhatsApp, de onde você decide enviá-la. O WhatsApp é um serviço de terceiro (Meta), com política de privacidade própria. Se o envio por e-mail estiver ativo, os dados podem ser processados pelo serviço de formulários Formspree.</p>
<h2>6. Compartilhamento</h2>
<p>Não vendemos dados pessoais. Podemos compartilhá-los apenas com prestadores necessários à operação (por exemplo, transportadoras, meios de pagamento, ferramentas de comunicação, hospedagem e análise), com autoridades quando exigido por lei ou com sua autorização.</p>
<h2>7. Cookies</h2>
<p>Usamos armazenamento local do navegador para lembrar sua escolha sobre cookies. Ferramentas de análise e publicidade só são ativadas se você clicar em "Aceitar" no aviso de cookies. Você pode mudar sua escolha limpando os dados do site no navegador.</p>
<h2>8. Por quanto tempo guardamos</h2>
<p>Mantemos os dados pelo tempo necessário para as finalidades acima e para cumprir prazos legais e fiscais. Depois disso, eles são excluídos ou anonimizados.</p>
<h2>9. Seus direitos</h2>
<p>Você pode solicitar confirmação de tratamento, acesso, correção, anonimização, portabilidade, eliminação, informações sobre compartilhamento e revogação do consentimento, nos termos do art. 18 da LGPD.</p>
<h2>10. Segurança</h2>
<p>Adotamos medidas técnicas e administrativas razoáveis para proteger os dados contra acessos não autorizados e situações acidentais ou ilícitas.</p>
<h2>11. Contato do encarregado (DPO)</h2>
<p>Para exercer seus direitos ou tirar dúvidas, escreva para <a href="mailto:{C["email"]}">{C["email"]}</a> ou chame no WhatsApp {C["whatsapp_exibicao"]}. <!-- PREENCHER: nome do encarregado, se houver. --></p>
<h2>12. Alterações</h2>
<p>Esta política pode ser atualizada. A data da última atualização fica no início da página.</p>
</div></section>'''
    pages.append({"path": "politica-de-privacidade.html", "title": "Política de Privacidade (LGPD) | Tango Fantasias",
                  "desc": "Saiba como a Tango Fantasias coleta, usa e protege seus dados pessoais conforme a LGPD e como exercer seus direitos de titular. Leia a política completa.",
                  "crumbs": [("Início", "index.html"), ("Política de Privacidade", "politica-de-privacidade.html")], "body": pol_body,
                  "priority": "0.3", "freq": "yearly"})

    # ================================================================ TERMOS
    termos_body = f'''<section class="page-hero"><div class="container"><h1>Termos de Uso</h1><p>Condições para utilização do site da Tango Fantasias.</p></div></section>
<section class="section"><div class="container prose">
<p><em>Última atualização: {hoje_br}</em></p>
<!-- REVISAR com assessoria jurídica antes de publicar. -->
<h2>1. Aceitação</h2><p>Ao acessar este site, você concorda com estes Termos de Uso e com a <a href="@/politica-de-privacidade.html">Política de Privacidade</a>. Se não concordar, não utilize o site.</p>
<h2>2. Finalidade do site</h2><p>Este site apresenta os produtos da {C["razao"]} (CNPJ {C["cnpj"]}) e permite solicitar contato e orçamentos. Não há venda on-line com pagamento pelo site.</p>
<h2>3. Produtos, imagens e orçamentos</h2><p>As imagens são ilustrativas e cores podem variar conforme a tela e o lote de tecido. Modelos, tamanhos, preços, prazos e disponibilidade são confirmados no orçamento. O envio de formulário não gera compra automática.</p>
<h2>4. Trocas e devoluções</h2><p>Seguem o Código de Defesa do Consumidor e as condições informadas no momento da compra. Peças produzidas sob encomenda, com especificações do cliente, podem ter condições específicas definidas no orçamento.</p>
<h2>5. Propriedade intelectual</h2><p>Textos, marcas, logotipos, fotos e layout pertencem à Tango Fantasias ou são usados com autorização. É proibida a reprodução sem permissão prévia por escrito. A Tango Fantasias não produz personagens de marcas registradas sem licença dos detentores dos direitos.</p>
<h2>6. Links externos</h2><p>O site pode conter links para serviços de terceiros (como WhatsApp e Google Maps), com termos e políticas próprios.</p>
<h2>7. Responsabilidade</h2><p>Buscamos manter as informações atualizadas, mas podem ocorrer imprecisões, corrigidas assim que identificadas.</p>
<h2>8. Legislação e foro</h2><p>Estes termos são regidos pela legislação brasileira. Fica eleito o foro da comarca de São Paulo - SP, salvo disposição legal em contrário.</p>
<h2>9. Contato</h2><p>WhatsApp {C["whatsapp_exibicao"]} · <a href="mailto:{C["email"]}">{C["email"]}</a> · {endereco}</p>
</div></section>'''
    pages.append({"path": "termos-de-uso.html", "title": "Termos de Uso | Tango Fantasias",
                  "desc": "Leia os Termos de Uso do site da Tango Fantasias, fábrica de fantasias no Brás, São Paulo: orçamentos, imagens, trocas e propriedade intelectual.",
                  "crumbs": [("Início", "index.html"), ("Termos de Uso", "termos-de-uso.html")], "body": termos_body,
                  "priority": "0.3", "freq": "yearly"})

    # ================================================================ 404
    p404 = f'''<section class="error-page"><div class="container">
<p class="code" aria-hidden="true">404</p>
<h1>Página não encontrada</h1>
<p>O endereço pode ter mudado ou não existe mais. Veja alguns links úteis:</p>
<ul class="chips" style="justify-content:center">
<li><a href="@/index.html">Página inicial</a></li><li><a href="@/fantasias.html">Fantasias</a></li>
<li><a href="@/fantasias/fantasias-de-carnaval.html">Carnaval</a></li><li><a href="@/fantasias/fantasias-infantis.html">Infantis</a></li>
<li><a href="@/atacado.html">Atacado</a></li><li><a href="@/orcamento.html">Orçamento</a></li><li><a href="@/contato.html">Contato</a></li></ul>
<div class="btn-row" style="justify-content:center">{btn_whats()}{btn_orc()}</div>
</div></section>'''
    pages.append({"path": "404.html", "title": "Página não encontrada | Tango Fantasias",
                  "desc": "A página que você procura não foi encontrada. Veja as fantasias da Tango no atacado e varejo, direto da fábrica no Brás, ou fale conosco no WhatsApp.",
                  "robots": "noindex,follow", "absolute_root": True, "body": p404})
    return pages
