# -*- coding: utf-8 -*-
"""Páginas institucionais, formulários, legais e 404 da Elbatec."""
import datetime


def PAGINAS(ctx):
    C = ctx["CONFIG"]; I = ctx["ICONS"]; S = ctx["SERVICOS"]; POSTS = ctx["POSTS"]; AREAS = ctx["AREAS"]
    btn_whats = ctx["btn_whats"]; btn_orc = ctx["btn_orc"]; btn_tel = ctx["btn_tel"]; faq_html = ctx["faq_html"]
    LB = ctx["schema_localbusiness"](); schema_faq = ctx["schema_faq"]
    endereco = f'{C["rua"]} – {C["bairro"]}, {C["cidade"]} - {C["uf"]}, CEP {C["cep"]}'
    mapa_q = "Rua+das+Palmas,+235,+Polvilho,+Cajamar+-+SP,+07791-655"
    pages = []

    def card_servico(s):
        return f'''<article class="card reveal"><div class="icon-circle">{I[s["icone"]]}</div>
<h3><a href="@/servicos/{s["slug"]}.html">{s["nome"]}</a></h3><p>{s["resumo"]}</p>
<a class="card__link" href="@/servicos/{s["slug"]}.html" aria-label="Saiba mais sobre {s["nome_curto"].lower()}">Saiba mais</a></article>'''

    card_produtos = f'''<article class="card reveal"><div class="icon-circle">{I["flask"]}</div>
<h3><a href="@/produtos-saneantes.html">Venda de produtos saneantes</a></h3><p>Saneantes domissanitários regularizados na ANVISA, com orientação de uso seguro.</p>
<a class="card__link" href="@/produtos-saneantes.html" aria-label="Saiba mais sobre produtos saneantes">Saiba mais</a></article>'''

    cards = "".join(card_servico(s) for s in S) + card_produtos

    areas_chips = "".join(f'<li>{c}{" (" + ", ".join(b) + ")" if b else ""}</li>' for c, b in AREAS)

    def opcoes_servico():
        o = ['<option value="">Selecione</option>'] + [f'<option>{s["nome"]}</option>' for s in S]
        o += ['<option>Venda de produtos saneantes</option>', '<option>Contrato de manutenção (empresa/condomínio)</option>', '<option>Outro / não sei</option>']
        return "".join(o)

    def campo(id_, label, tipo="text", req=True, extra="", data_label=None, ac=""):
        r = ' <span class="req" aria-hidden="true">*</span>' if req else ""
        req_attr = " required" if req else ""
        acs = f' autocomplete="{ac}"' if ac else ""
        return f'''<div class="field"><label for="{id_}">{label}{r}</label>
<input id="{id_}" name="{id_.split("-")[-1]}" type="{tipo}"{req_attr}{acs} data-label="{data_label or label}" aria-describedby="{id_}-erro" {extra}>
<span class="error" id="{id_}-erro" aria-live="polite"></span></div>'''

    def aceite(pfx):
        return f'''<div class="field"><label class="check" for="{pfx}-aceite"><input id="{pfx}-aceite" name="aceite" type="checkbox" required aria-describedby="{pfx}-aceite-erro">
<span>Li e aceito a <a href="@/politica-de-privacidade.html" target="_blank" rel="noopener">Política de Privacidade</a> e autorizo o contato da Elbatec. <span class="req" aria-hidden="true">*</span></span></label>
<span class="error" id="{pfx}-aceite-erro" aria-live="polite"></span></div>
<input type="text" name="_gotcha" tabindex="-1" autocomplete="off" aria-hidden="true" style="position:absolute;left:-9999px" title="Não preencha">'''

    # ==================================================================== HOME
    home_faq = [
        ("Os produtos são seguros para crianças e animais?", "Usamos produtos registrados na ANVISA e escolhemos métodos de menor exposição quando há crianças, gestantes e pets. Você recebe por escrito as orientações e o tempo para retornar ao ambiente."),
        ("Quanto custa uma dedetização?", "O valor depende do tipo de imóvel, da metragem, da praga e do método. Envie os dados pelo formulário ou pelo WhatsApp e retornamos com o orçamento."),
        ("Vocês emitem certificado?", "Sim. Todo serviço gera comprovante de execução com data, área tratada e produtos utilizados, aceito por condomínios, empresas e fiscalização."),
        ("Atendem empresas e condomínios com contrato?", "Sim. Oferecemos programas de manejo integrado de pragas com visitas programadas, relatórios e documentação para auditorias."),
        ("Quais cidades vocês atendem?", "Cajamar (Polvilho, Jordanésia, Centro e Ipês), Santana de Parnaíba, Pirapora do Bom Jesus, Caieiras, Franco da Rocha, Cabreúva, Jundiaí, Barueri, Osasco e a região noroeste de São Paulo."),
    ]
    home_body = f'''<section class="hero">
  <div class="container">
    <div>
      <h1>Dedetizadora em Cajamar: controle de pragas para casas e empresas</h1>
      <p class="lead">Dedetização, desratização, descupinização, controle de escorpiões e pombos, limpeza de caixa d'água e de fossa em Cajamar, Polvilho, Jordanésia e região — com produtos registrados na ANVISA e certificado de execução.</p>
      <div class="btn-row">{btn_whats()}{btn_orc("Pedir orçamento", "btn btn--outline")}</div>
      <ul class="badges">
        <li>{I["bolt"]}Atendimento rápido</li>
        <li>{I["shield"]}Produtos registrados na ANVISA</li>
        <li>{I["doc"]}Certificado de execução</li>
        <li>{I["building"]}Atendimento para empresas</li>
      </ul>
    </div>
    <img class="hero__img" src="@/assets/img/hero-controle-de-pragas-cajamar.webp" alt="Técnico da Elbatec com equipamento de proteção atendendo uma residência em Cajamar" width="1200" height="900" fetchpriority="high" decoding="async">
  </div>
</section>

<section class="section" aria-labelledby="t-servicos">
  <div class="container">
    <div class="section__head"><span class="eyebrow">Serviços</span><h2 id="t-servicos">Controle de pragas e saneamento ambiental</h2>
    <p>Soluções completas para manter seu imóvel livre de pragas e com água e esgoto em ordem — do diagnóstico ao certificado.</p></div>
    <div class="grid grid--3">{cards}</div>
  </div>
</section>

<section class="section section--alt" aria-labelledby="t-como">
  <div class="container">
    <div class="section__head"><span class="eyebrow">Como funciona</span><h2 id="t-como">Do primeiro contato ao certificado em 4 passos</h2></div>
    <ol class="steps steps--4">
      <li class="reveal"><h3>Contato e orçamento</h3><p>Fale pelo WhatsApp, telefone ou formulário. Se puder, envie fotos e a metragem aproximada.</p></li>
      <li class="reveal"><h3>Vistoria e diagnóstico</h3><p>Identificamos a praga, os abrigos e as entradas para escolher o método mais adequado.</p></li>
      <li class="reveal"><h3>Aplicação segura</h3><p>Equipe com EPIs, produtos registrados na ANVISA e orientações claras de preparo e retorno.</p></li>
      <li class="reveal"><h3>Garantia e certificado</h3><p>Você recebe o comprovante de execução e as condições de garantia por escrito.</p></li>
    </ol>
  </div>
</section>

<section class="section" aria-labelledby="t-publico">
  <div class="container">
    <div class="section__head"><span class="eyebrow">Para quem</span><h2 id="t-publico">Soluções para residências, empresas e condomínios</h2></div>
    <div class="split">
      <div class="panel panel--light reveal">
        <div class="icon-circle" style="background:#fff">{I["home"]}</div>
        <h3>Para residências</h3>
        <ul class="check-list">
          <li>Casas, sobrados, apartamentos e chácaras</li>
          <li>Métodos de baixa exposição para crianças e pets</li>
          <li>Horários combinados com você</li>
          <li>Orientações de prevenção após o serviço</li>
        </ul>
        <a class="btn btn--primary" href="@/orcamento.html">Orçamento para minha casa</a>
      </div>
      <div class="panel panel--dark reveal">
        <div class="icon-circle">{I["building"]}</div>
        <h3>Para empresas e condomínios</h3>
        <ul class="check-list">
          <li>Contratos de manejo integrado de pragas (MIP)</li>
          <li>Galpões logísticos, indústrias, restaurantes e escolas</li>
          <li>Relatórios, mapas de iscas e comprovantes para auditorias</li>
          <li>Visitas programadas fora do horário de operação</li>
        </ul>
        <a class="btn btn--light" href="@/empresas-e-condominios.html">Conhecer soluções B2B</a>
      </div>
    </div>
  </div>
</section>

<section class="section section--alt" aria-labelledby="t-porque">
  <div class="container">
    <div class="section__head"><span class="eyebrow">Diferenciais</span><h2 id="t-porque">Por que escolher a Elbatec</h2></div>
    <!-- CONFIRMAR: revise os diferenciais abaixo e mantenha somente os que são verdadeiros para a empresa. -->
    <div class="grid grid--3">
      <div class="card reveal"><div class="icon-circle">{I["pin"]}</div><h3>Empresa de Cajamar</h3><p>Sede no Polvilho, perto de quem atendemos — o que facilita vistorias e retornos em Cajamar e cidades vizinhas.</p></div>
      <div class="card reveal"><div class="icon-circle">{I["shield"]}</div><h3>Produtos regularizados</h3><p>Apenas saneantes com registro ou notificação na ANVISA, aplicados conforme o rótulo e as boas práticas.</p></div>
      <div class="card reveal"><div class="icon-circle">{I["doc"]}</div><h3>Documentação completa</h3><p>Comprovante de execução em todo serviço e relatórios para empresas e condomínios.</p></div>
      <div class="card reveal"><div class="icon-circle">{I["check"]}</div><h3>Serviços integrados</h3><p>Controle de pragas, limpeza de caixa d'água, fossa e caixa de gordura com um único fornecedor.</p></div>
      <div class="card reveal"><div class="icon-circle">{I["building"]}</div><h3>Experiência com empresas</h3><p>Atendimento a galpões, indústrias e comércios com planejamento de horários. <!-- CONFIRMAR --></p></div>
      <div class="card reveal"><div class="icon-circle">{I["clock"]}</div><h3>Atendimento ágil</h3><p>Resposta rápida pelo WhatsApp e agendamento conforme a sua necessidade. <!-- CONFIRMAR prazo médio de atendimento --></p></div>
    </div>
    <!-- INSERIR DEPOIMENTOS REAIS (com autorização dos clientes). Não publique depoimentos ou notas inventados.
    <div class="grid grid--3" style="margin-top:24px">
      <blockquote class="card"><p>"Texto do depoimento real."</p><footer>— Nome do cliente, bairro/cidade</footer></blockquote>
    </div>
    -->
  </div>
</section>

<section class="section" aria-labelledby="t-areas">
  <div class="container">
    <div class="section__head"><span class="eyebrow">Áreas atendidas</span><h2 id="t-areas">Dedetizadora em Cajamar, Polvilho, Jordanésia e região</h2>
    <p>Atendemos toda Cajamar e cidades da região noroeste da Grande São Paulo e de Jundiaí.</p></div>
    <ul class="chips">{areas_chips}</ul>
    <p><a class="btn btn--outline" href="@/areas-atendidas.html">Ver todas as áreas atendidas</a></p>
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
    <h2>Problema com pragas? Fale com a Elbatec agora</h2>
    <p>Orçamento sem compromisso para residências, condomínios e empresas de Cajamar e região.</p>
    <div class="btn-row">{btn_whats()}{btn_orc("Pedir orçamento", "btn btn--light")}</div>
  </div>
</section>'''
    pages.append({"path": "index.html", "title": "Dedetizadora em Cajamar | Elbatec Controle de Pragas",
                  "desc": "Dedetizadora em Cajamar e região: dedetização, desratização, cupins, escorpiões e limpeza de caixa d'água. Produtos ANVISA e certificado. Peça orçamento!",
                  "active": "index.html", "crumbs": [("Início", "index.html")], "schemas": [LB], "body": home_body,
                  "priority": "1.0", "freq": "weekly",
                  "preload": '<link rel="preload" as="image" href="assets/img/hero-controle-de-pragas-cajamar.webp" type="image/webp" fetchpriority="high">'})

    # ==================================================================== SOBRE
    sobre_body = f'''<section class="page-hero"><div class="container"><h1>Sobre a Elbatec Controle de Pragas</h1>
<p>Empresa de Cajamar especializada em controle de pragas urbanas, limpeza e saneamento ambiental para residências, condomínios e empresas.</p></div></section>
<div class="section"><div class="container content-layout">
<article class="prose">
  <h2>Quem somos</h2>
  <p>A <strong>{C["razao"]}</strong>, inscrita no CNPJ {C["cnpj"]}, atua com imunização e controle de pragas urbanas, atividades de limpeza, comércio de produtos saneantes domissanitários e serviços relacionados a esgoto. Nossa sede fica na {C["rua"]}, no bairro {C["bairro"]}, em Cajamar - SP.</p>
  <p>Trabalhamos para que casas, condomínios, comércios e empresas da região tenham ambientes mais seguros e saudáveis, combinando técnica, produtos regularizados e uma comunicação clara com o cliente: você sabe o que será feito, quais produtos serão usados, como se preparar e quais cuidados tomar depois.</p>
  <!-- PREENCHER: história da empresa (ano de fundação real, fundadores, trajetória). Não publique números que não possam ser comprovados. -->
  <figure><img src="@/assets/img/equipe-elbatec.webp" alt="Equipe da Elbatec Controle de Pragas com uniformes e equipamentos de proteção" width="1200" height="675" loading="lazy" decoding="async">
  <figcaption>Imagem ilustrativa — substitua por uma foto real da equipe.</figcaption></figure>
  <h2>Nossas atividades</h2>
  <ul class="check-list">
    <li><strong>Imunização e controle de pragas urbanas</strong> — dedetização, desratização, descupinização, desinsetização, controle de escorpiões e manejo de pombos.</li>
    <li><strong>Atividades de limpeza</strong> — sanitização de ambientes e limpeza e higienização de caixas d'água.</li>
    <li><strong>Serviços relacionados a esgoto</strong> — limpeza de fossa, caixa de gordura e desentupimento.</li>
    <li><strong>Comércio de saneantes domissanitários</strong> — venda de produtos regularizados com orientação de uso.</li>
  </ul>
  <h2>Como trabalhamos</h2>
  <p>Seguimos os princípios do <strong>manejo integrado de pragas</strong>: antes de aplicar qualquer produto, entendemos por que a praga está ali. Muitas vezes, vedar uma fresta, ajustar o armazenamento ou corrigir uma caixa de gordura faz tanta diferença quanto o produto. O resultado é um controle mais duradouro e com menor uso de químicos.</p>
  <p>As empresas especializadas em controle de pragas seguem as normas da ANVISA (RDC nº 622/2022) e da vigilância sanitária estadual e municipal. Por isso, todo serviço é registrado em comprovante de execução, com produtos, princípios ativos e orientações.</p>
  <h2>Licenças e responsável técnico</h2>
  <div class="todo-box">
  <!-- PREENCHER: Licença de funcionamento / CVS (número e órgão emissor) e responsável técnico (nome, formação e registro no conselho).
  Exemplo:
  <p>Licença de Funcionamento da Vigilância Sanitária nº XXXXXXX — válida até XX/XX/XXXX.<br>
  Responsável técnico: Nome Sobrenome — Químico(a), CRQ IV Região nº XXXXXXXX.</p>
  -->
  <p>Documentação sanitária e responsável técnico disponíveis mediante solicitação.</p>
  </div>
  <h2>Dados da empresa</h2>
  <ul>
    <li>Razão social: {C["razao"]}</li>
    <li>Nome fantasia: {C["nome"]}</li>
    <li>CNPJ: {C["cnpj"]}</li>
    <li>Inscrição Estadual (SP): {C["ie"]}</li>
    <li>Endereço: {endereco}</li>
    <li>Telefone: <a href="tel:{C["tel_link"]}">{C["tel_exibicao"]}</a></li>
  </ul>
  <div class="btn-row">{btn_whats()}{btn_orc()}</div>
</article>
<aside class="sidebar" aria-label="Atalhos"><div class="cta-box"><h2>Fale com a gente</h2><p>{C["horario_texto"]}</p>{btn_whats("WhatsApp")}<a class="btn btn--light" href="tel:{C["tel_link"]}">{I["phone"]}<span>{C["tel_exibicao"]}</span></a></div>
<div class="card"><h2 style="font-size:1.1rem">Serviços</h2><ul>{"".join(f'<li><a href="@/servicos/{s["slug"]}.html">{s["nome_curto"]}</a></li>' for s in S)}</ul></div></aside>
</div></div>'''
    pages.append({"path": "sobre.html", "title": "Sobre a Elbatec | Controle de Pragas em Cajamar",
                  "desc": "Conheça a Elbatec Controle de Pragas, empresa de Cajamar - SP com dedetização, limpeza e saneamento ambiental para casas e empresas. Fale com a gente.",
                  "active": "sobre.html", "crumbs": [("Início", "index.html"), ("Sobre", "sobre.html")], "body": sobre_body, "priority": "0.6"})

    # ==================================================================== SERVIÇOS
    serv_body = f'''<section class="page-hero"><div class="container"><h1>Serviços de Controle de Pragas em Cajamar</h1>
<p>Do controle de insetos e roedores à limpeza de caixa d'água e fossa: conheça todas as soluções da Elbatec para residências, condomínios e empresas.</p>
<div class="btn-row">{btn_whats()}{btn_orc("Pedir orçamento", "btn btn--outline")}</div></div></section>
<section class="section"><div class="container">
  <div class="section__head"><h2>Controle de pragas urbanas</h2><p>Métodos definidos após vistoria, com produtos registrados na ANVISA e comprovante de execução.</p></div>
  <div class="grid grid--3">{"".join(card_servico(s) for s in S[:6])}</div>
</div></section>
<section class="section section--alt"><div class="container">
  <div class="section__head"><h2>Limpeza, saneamento e produtos</h2><p>Serviços que completam a prevenção: água limpa, esgoto funcionando e ambientes desinfetados.</p></div>
  <div class="grid grid--3">{"".join(card_servico(s) for s in S[6:])}{card_produtos}</div>
</div></section>
<section class="section"><div class="container prose">
  <h2>Como escolher o serviço certo</h2>
  <p>Nem sempre é fácil saber qual serviço contratar. Baratas, formigas e aranhas pedem <a href="@/servicos/dedetizacao.html">dedetização</a>; ratos e camundongos, <a href="@/servicos/desratizacao.html">desratização</a>; madeira com furinhos e pó, <a href="@/servicos/descupinizacao.html">descupinização</a>; pulgas, carrapatos e mosquitos, <a href="@/servicos/desinsetizacao.html">desinsetização</a>. Escorpiões exigem um <a href="@/servicos/controle-de-escorpioes.html">manejo específico</a>, e pombos são controlados com <a href="@/servicos/controle-de-pombos.html">barreiras físicas</a>.</p>
  <p>Se estiver em dúvida, mande uma foto pelo WhatsApp: nossa equipe ajuda a identificar o problema e indica o melhor caminho. Para empresas e condomínios que precisam de controle contínuo, veja os <a href="@/empresas-e-condominios.html">contratos de manejo integrado de pragas</a>.</p>
</div></section>
<section class="cta-final"><div class="container"><h2>Não sabe qual serviço contratar?</h2><p>Descreva o problema e indicamos a solução mais adequada para o seu imóvel.</p><div class="btn-row">{btn_whats()}{btn_orc("Pedir orçamento", "btn btn--light")}</div></div></section>'''
    pages.append({"path": "servicos.html", "title": "Serviços de Controle de Pragas em Cajamar | Elbatec",
                  "desc": "Veja os serviços da Elbatec em Cajamar: dedetização, desratização, cupins, escorpiões, pombos, sanitização, caixa d'água e fossa. Solicite seu orçamento.",
                  "active": "servicos.html", "crumbs": [("Início", "index.html"), ("Serviços", "servicos.html")],
                  "schemas": [{"@context": "https://schema.org", "@type": "ItemList", "name": "Serviços da Elbatec",
                               "itemListElement": [{"@type": "ListItem", "position": i + 1, "name": s["nome"],
                                                    "url": C["site_url"] + "servicos/" + s["slug"] + ".html"} for i, s in enumerate(S)]}],
                  "body": serv_body, "priority": "0.9"})

    # ==================================================================== ÁREAS ATENDIDAS
    areas_txt = {
        "Cajamar": "Nossa sede fica no Polvilho, e atendemos todos os bairros de Cajamar — Polvilho, Jordanésia, Centro, Ipês e demais regiões —, incluindo condomínios residenciais, comércios e os centros de distribuição às margens da Anhanguera.",
        "Santana de Parnaíba": "Residências, condomínios fechados e empresas, com atenção especial ao controle de escorpiões e de cupins em áreas com muita vegetação.",
        "Pirapora do Bom Jesus": "Casas, chácaras e comércios, com serviços de desinsetização, controle de escorpiões e limpeza de fossa.",
        "Caieiras": "Residências, indústrias e condomínios, com dedetização, desratização e limpeza de caixa d'água.",
        "Franco da Rocha": "Casas, comércios e empresas, com controle de pragas e serviços de saneamento.",
        "Cabreúva": "Chácaras, condomínios e galpões, com controle de roedores, escorpiões e cupins.",
        "Jundiaí": "Empresas, condomínios e residências, sob consulta de agenda para a região.",
        "Barueri": "Empresas, condomínios e residências, com contratos de manejo integrado de pragas.",
        "Osasco": "Comércios, empresas e residências, com dedetização e sanitização.",
        "Perus (São Paulo)": "Residências e comércios da zona noroeste da capital.",
        "Pirituba (São Paulo)": "Residências, condomínios e empresas da zona noroeste da capital.",
        "Região noroeste de São Paulo": "Outros bairros da região noroeste da capital, sob consulta.",
    }
    areas_cards = "".join(f'''<article class="card reveal"><div class="icon-circle">{I["pin"]}</div><h3>{c}</h3>
{"<p><strong>Bairros:</strong> " + ", ".join(b) + "</p>" if b else ""}<p>{areas_txt.get(c, "")}</p></article>''' for c, b in AREAS)
    areas_body = f'''<section class="page-hero"><div class="container"><h1>Áreas Atendidas: Cajamar e Região</h1>
<p>A Elbatec atende Cajamar e cidades vizinhas da Grande São Paulo e região de Jundiaí. Confira as localidades e fale com a gente para confirmar a disponibilidade no seu endereço.</p></div></section>
<!-- AJUSTE A LISTA CONFORME SUA ÁREA REAL (edite AREAS no build.py ou diretamente aqui) -->
<section class="section"><div class="container"><div class="grid grid--3">{areas_cards}</div></div></section>
<section class="section section--alt"><div class="container prose">
  <h2>Controle de pragas perto de você</h2>
  <p>Estar sediada no Polvilho, em Cajamar, permite que a Elbatec faça vistorias e retornos com agilidade em toda a cidade e nos municípios vizinhos. A região tem características que influenciam o tipo de praga mais comum: áreas verdes e terrenos favorecem <a href="@/servicos/controle-de-escorpioes.html">escorpiões</a> e <a href="@/servicos/descupinizacao.html">cupins</a>; córregos e galerias aumentam a pressão de <a href="@/servicos/desratizacao.html">roedores</a>; e a grande quantidade de galpões e centros logísticos exige <a href="@/empresas-e-condominios.html">programas contínuos de controle</a>.</p>
  <p>Seu bairro não está na lista? Entre em contato — avaliamos o atendimento caso a caso.</p>
  <div class="btn-row">{btn_whats("Consultar meu endereço", "Olá! Vim pelo site e gostaria de saber se vocês atendem meu endereço.")}{btn_orc()}</div>
</div></section>'''
    pages.append({"path": "areas-atendidas.html", "title": "Áreas Atendidas | Dedetizadora em Cajamar e Região",
                  "desc": "Dedetizadora em Cajamar, Polvilho, Jordanésia, Santana de Parnaíba, Caieiras, Franco da Rocha, Jundiaí, Barueri e Osasco. Consulte seu endereço agora.",
                  "active": "areas-atendidas.html", "crumbs": [("Início", "index.html"), ("Áreas atendidas", "areas-atendidas.html")],
                  "body": areas_body, "priority": "0.8"})

    # ==================================================================== EMPRESAS E CONDOMÍNIOS
    b2b_faq = [
        ("O que é manejo integrado de pragas (MIP)?", "É um programa contínuo que combina inspeção, monitoramento, medidas preventivas e controle químico apenas quando necessário, com registros de cada etapa."),
        ("Vocês atendem fora do horário comercial?", "Sim, mediante agendamento, para não interferir na operação de empresas, restaurantes e escolas. Condições definidas em contrato."),
        ("Que documentos a empresa recebe?", "Comprovante de execução a cada visita e, nos contratos, relatórios, mapas de porta-iscas e fichas dos produtos utilizados, conforme o escopo contratado."),
        ("O contrato tem fidelidade?", "As condições de prazo, frequência e rescisão são definidas na proposta comercial, conforme a necessidade de cada cliente."),
        ("Atendem centros de distribuição grandes?", "Sim. O escopo é definido após vistoria técnica, considerando área, docas, áreas externas e exigências de auditoria dos clientes."),
    ]
    b2b_body = f'''<section class="page-hero"><div class="container"><h1>Controle de Pragas para Empresas e Condomínios</h1>
<p>Contratos de manejo integrado de pragas para condomínios, indústrias, galpões logísticos, restaurantes, escolas e comércios de Cajamar e região, com documentação para auditorias.</p>
<div class="btn-row">{btn_whats("Falar com um consultor", "Olá! Vim pelo site e gostaria de uma proposta de contrato para minha empresa/condomínio.")}{btn_orc("Solicitar proposta", "btn btn--outline")}</div></div></section>
<section class="section"><div class="container">
  <div class="section__head"><h2>Por que ter um contrato de controle de pragas</h2>
  <p>Em empresas e condomínios, uma infestação gera prejuízo, reclamações, risco à saúde e problemas em auditorias. O controle contínuo é mais eficiente e previsível do que chamar uma dedetizadora só quando o problema aparece.</p></div>
  <div class="grid grid--3">
    <div class="card reveal"><div class="icon-circle">{I["doc"]}</div><h3>Documentação para auditorias</h3><p>Comprovantes de execução, relatórios de visita, mapas de porta-iscas e fichas dos produtos utilizados.</p></div>
    <div class="card reveal"><div class="icon-circle">{I["clock"]}</div><h3>Visitas programadas</h3><p>Cronograma definido em contrato, com horários que respeitam a operação de cada cliente.</p></div>
    <div class="card reveal"><div class="icon-circle">{I["shield"]}</div><h3>Manejo integrado (MIP)</h3><p>Prevenção, monitoramento e controle com menor uso de químicos e foco nas causas.</p></div>
  </div>
</div></section>
<section class="section section--alt"><div class="container content-layout">
<article class="prose">
  <h2>Segmentos atendidos</h2>
  <h3>Galpões logísticos e centros de distribuição</h3>
  <p>A região de Cajamar concentra muitos centros de distribuição ao longo da Rodovia Anhanguera. Docas, áreas externas, paletes e grandes coberturas exigem controle de roedores com porta-iscas numerados, monitoramento de insetos rasteiros e <a href="@/servicos/controle-de-pombos.html">proteção contra pombos</a>. Montamos o plano conforme as exigências de auditoria dos seus clientes.</p>
  <h3>Indústrias</h3>
  <p>Programas sob medida para áreas produtivas, refeitórios, vestiários e almoxarifados, com registros que apoiam sistemas de qualidade e boas práticas de fabricação.</p>
  <h3>Condomínios residenciais e comerciais</h3>
  <p>Dedetização de áreas comuns, casas de lixo, garagens, poços de elevador e caixas de gordura; desratização de áreas externas; <a href="@/servicos/limpeza-caixa-dagua.html">limpeza de caixas d'água e cisternas</a>; e comprovantes para apresentar em assembleia e aos moradores.</p>
  <h3>Restaurantes, padarias e cozinhas industriais</h3>
  <p>Controle de baratas, moscas e roedores com métodos compatíveis com a manipulação de alimentos, mais <a href="@/servicos/limpeza-de-fossa-e-desentupimento.html">limpeza periódica de caixa de gordura</a>.</p>
  <h3>Escolas, creches e clínicas</h3>
  <p>Aplicações planejadas fora do horário de aulas ou de atendimento, com métodos de baixa exposição e orientação de reentrada.</p>
  <h2>O que pode estar incluído no contrato</h2>
  <ul class="check-list">
    <li>Vistoria inicial e diagnóstico das áreas de risco</li>
    <li>Plano de manejo integrado de pragas com cronograma de visitas</li>
    <li>Instalação e monitoramento de porta-iscas com mapa de localização</li>
    <li>Dedetização e desinsetização periódicas</li>
    <li>Atendimentos extras em caso de ocorrência (conforme contrato)</li>
    <li>Limpeza de caixas d'água e de gordura em calendário programado</li>
    <li>Comprovantes de execução e relatórios de cada visita</li>
  </ul>
  <!-- PREENCHER: se a empresa tiver modelo de relatório, sistema online ou atendimento emergencial, descreva aqui. -->
  <h2>Perguntas frequentes de empresas</h2>
  {faq_html(b2b_faq)}
</article>
<aside class="sidebar" aria-label="Solicitar proposta"><div class="cta-box"><h2>Solicite uma proposta</h2><p>Conte o segmento, a área aproximada e a cidade. Agendamos a vistoria técnica.</p>{btn_whats("WhatsApp", "Olá! Vim pelo site e gostaria de uma proposta de contrato para minha empresa/condomínio.")}<a class="btn btn--light" href="@/orcamento.html">Formulário de orçamento</a></div></aside>
</div></section>
<section class="cta-final"><div class="container"><h2>Sua empresa precisa de controle de pragas contínuo?</h2><p>Proposta personalizada após vistoria técnica, sem compromisso.</p><div class="btn-row">{btn_whats("Falar com um consultor", "Olá! Vim pelo site e gostaria de uma proposta de contrato para minha empresa/condomínio.")}{btn_orc("Solicitar proposta", "btn btn--light")}</div></div></section>'''
    pages.append({"path": "empresas-e-condominios.html", "title": "Dedetização para Empresas e Condomínios | Elbatec",
                  "desc": "Dedetização para empresas e condomínios em Cajamar: contratos de manejo integrado de pragas, relatórios e certificados para auditoria. Solicite proposta.",
                  "active": "empresas-e-condominios.html", "crumbs": [("Início", "index.html"), ("Empresas e condomínios", "empresas-e-condominios.html")],
                  "schemas": [schema_faq(b2b_faq)], "body": b2b_body, "priority": "0.9"})

    # ==================================================================== FAQ
    faq_geral = home_faq + [
        ("Qual a diferença entre dedetização, desinsetização e desratização?", "Dedetização é usada principalmente para baratas, formigas e aranhas; desinsetização para insetos como mosquitos, pulgas, carrapatos e traças; desratização para ratos e camundongos."),
        ("Preciso preparar o imóvel antes do serviço?", "Sim. Antes do atendimento enviamos as orientações: guardar alimentos e utensílios, recolher objetos dos pets, liberar acesso a rodapés e armários, entre outras, conforme o serviço."),
        ("O resultado é imediato?", "Depende da praga e do método. Algumas pragas reduzem em poucos dias; outras, como baratas em gel e roedores com iscas, levam algumas semanas. Explicamos o que esperar em cada caso."),
        ("A dedetização elimina 100% das pragas?", "Nenhuma empresa séria pode prometer isso. O controle reduz a infestação a níveis aceitáveis, e a manutenção depende também de vedação, limpeza e prevenção."),
        ("De quanto em quanto tempo devo dedetizar?", "Depende do imóvel, do histórico e do entorno. Empresas de alimentação e condomínios costumam ter programas contínuos; residências, com menor frequência. Veja nosso artigo sobre o tema no blog."),
        ("Como funciona a garantia?", "O prazo é informado por escrito no orçamento e no comprovante, de acordo com o serviço e as condições do local. Se a praga voltar à área tratada dentro do prazo, agendamos o retorno."),
        ("Quais formas de pagamento vocês aceitam?", "As condições de pagamento são informadas no orçamento. <!-- PREENCHER: formas de pagamento aceitas (PIX, cartão, boleto, faturamento para empresas). -->"),
        ("Posso mandar foto da praga para identificação?", "Sim, e ajuda muito. Envie pelo WhatsApp a foto do inseto, das fezes ou dos danos, junto com o endereço."),
        ("Vocês vendem produtos para eu mesmo aplicar?", "Vendemos saneantes de venda livre com orientação. Produtos de uso profissional não são vendidos ao consumidor final; nesses casos, o serviço é feito pela nossa equipe."),
        ("Com que frequência limpar caixa d'água e fossa?", "A caixa d'água costuma ser limpa a cada seis meses. A fossa depende do volume e do número de moradores; a caixa de gordura precisa de limpeza mais frequente."),
    ]
    faq_body = f'''<section class="page-hero"><div class="container"><h1>Perguntas Frequentes sobre Controle de Pragas</h1>
<p>Respostas para as dúvidas mais comuns sobre dedetização, segurança, preparo do imóvel, garantia e atendimento da Elbatec em Cajamar e região.</p></div></section>
<section class="section"><div class="container content-layout">
<div class="prose">{faq_html(faq_geral)}
<p style="margin-top:24px">Não encontrou sua dúvida? Veja as perguntas específicas em cada página de <a href="@/servicos.html">serviço</a> ou fale com a gente.</p></div>
<aside class="sidebar" aria-label="Contato"><div class="cta-box"><h2>Ainda com dúvidas?</h2><p>Nossa equipe responde pelo WhatsApp.</p>{btn_whats("WhatsApp", "Olá! Vim pelo site e tenho uma dúvida.")}<a class="btn btn--light" href="tel:{C["tel_link"]}">{I["phone"]}<span>{C["tel_exibicao"]}</span></a></div></aside>
</div></section>'''
    pages.append({"path": "faq.html", "title": "Perguntas Frequentes sobre Dedetização | Elbatec",
                  "desc": "Tire dúvidas sobre dedetização, segurança para crianças e pets, garantia, certificado e preparo do imóvel com a Elbatec, de Cajamar. Fale com a gente.",
                  "crumbs": [("Início", "index.html"), ("Perguntas frequentes", "faq.html")],
                  "schemas": [schema_faq(faq_geral)], "body": faq_body, "priority": "0.7"})

    # ==================================================================== BLOG
    posts_cards = "".join(f'''<article class="card post-card reveal">
<img src="@/assets/img/{p["img"]}" alt="{p["img_alt"]}" width="1200" height="675" loading="lazy" decoding="async">
<p class="post-meta"><time datetime="{p["data"]}">{datetime.date.fromisoformat(p["data"]).strftime("%d/%m/%Y")}</time></p>
<h2 style="font-size:1.25rem"><a href="@/blog/{p["slug"]}.html">{p["h1"]}</a></h2><p>{p["resumo"]}</p>
<a class="card__link" href="@/blog/{p["slug"]}.html" aria-label="Ler o artigo: {p["h1"]}">Ler artigo</a></article>''' for p in POSTS)
    blog_body = f'''<section class="page-hero"><div class="container"><h1>Blog: Dicas de Controle de Pragas</h1>
<p>Orientações práticas para identificar, prevenir e controlar pragas em casas, condomínios e empresas de Cajamar e região.</p></div></section>
<section class="section"><div class="container"><div class="grid grid--3">{posts_cards}</div></div></section>
<!-- Para adicionar novos artigos: inclua um item em content_blog.py e rode python3 build.py (ou copie um arquivo de /blog/ e ajuste). -->'''
    pages.append({"path": "blog.html", "title": "Blog Elbatec | Dicas de Controle de Pragas",
                  "desc": "Dicas da Elbatec para identificar cupins, prevenir escorpiões e saber quando dedetizar. Conteúdo prático para casas e empresas de Cajamar. Leia agora.",
                  "active": "blog.html", "crumbs": [("Início", "index.html"), ("Blog", "blog.html")],
                  "schemas": [{"@context": "https://schema.org", "@type": "Blog", "name": "Blog Elbatec", "url": C["site_url"] + "blog.html",
                               "blogPost": [{"@type": "BlogPosting", "headline": p["h1"], "url": C["site_url"] + "blog/" + p["slug"] + ".html", "datePublished": p["data"]} for p in POSTS]}],
                  "body": blog_body, "priority": "0.6", "freq": "weekly"})

    # ==================================================================== CONTATO
    contato_body = f'''<section class="page-hero"><div class="container"><h1>Contato da Elbatec em Cajamar</h1>
<p>Fale com a Elbatec pelo WhatsApp, telefone, e-mail ou formulário. Atendemos Cajamar, Polvilho, Jordanésia e região.</p></div></section>
<section class="section"><div class="container split">
  <div>
    <h2>Fale conosco</h2>
    <ul class="info-list">
      <li>{I["phone"]}<div><strong>Telefone</strong><br><a href="tel:{C["tel_link"]}">{C["tel_exibicao"]}</a></div></li>
      <li>{I["whatsapp"]}<div><strong>WhatsApp</strong><br><a class="js-wa" href="{ctx["wa_href"]()}" data-msg="{ctx["MSG_WA"]}">{C["whatsapp_exibicao"]}</a></div></li>
      <li>{I["mail"]}<div><strong>E-mail</strong><br><a href="mailto:{C["email"]}">{C["email"]}</a></div></li>
      <li>{I["pin"]}<div><strong>Endereço</strong><br>{endereco}</div></li>
      <li>{I["clock"]}<div><strong>Horário de atendimento</strong><br>{C["horario_texto"]}<!-- CONFIRMAR horário e informar se há plantão para emergências --></div></li>
    </ul>
    <div class="map-wrap" style="margin-top:20px">
      <iframe src="https://www.google.com/maps?q={mapa_q}&amp;output=embed" title="Mapa: localização da Elbatec em Cajamar - SP" loading="lazy" referrerpolicy="no-referrer-when-downgrade" allowfullscreen></iframe>
    </div>
    <p class="form-note" style="margin-top:8px"><a href="https://www.google.com/maps/search/?api=1&amp;query={mapa_q}" target="_blank" rel="noopener">Abrir no Google Maps</a></p>
  </div>
  <div>
    <h2>Envie uma mensagem</h2>
    <form class="form" data-form="contato" novalidate action="https://formspree.io/f/SEU_ID_FORMSPREE" method="POST">
      <!-- Por padrão o envio abre o WhatsApp com os dados (ver assets/js/main.js). Para receber por e-mail, ative o Formspree em CONFIG no main.js. -->
      {campo("c-nome", "Nome", ac="name")}
      <div class="row-2">{campo("c-telefone", "Telefone/WhatsApp", "tel", ac="tel", extra='inputmode="tel" placeholder="(11) 91234-5678"')}{campo("c-email", "E-mail", "email", req=False, ac="email")}</div>
      <div class="field"><label for="c-mensagem">Mensagem <span class="req" aria-hidden="true">*</span></label>
      <textarea id="c-mensagem" name="mensagem" required data-label="Mensagem" aria-describedby="c-mensagem-erro"></textarea>
      <span class="error" id="c-mensagem-erro" aria-live="polite"></span></div>
      {aceite("c")}
      <button class="btn btn--whats" type="submit">{I["whatsapp"]}<span>Enviar pelo WhatsApp</span></button>
      <p class="form-status" role="status" aria-live="polite"></p>
      <p class="form-note">Campos com * são obrigatórios. Seus dados são usados apenas para responder ao seu contato.</p>
    </form>
  </div>
</div></section>'''
    pages.append({"path": "contato.html", "title": "Contato | Elbatec Controle de Pragas em Cajamar",
                  "desc": "Fale com a Elbatec Controle de Pragas em Cajamar - SP: WhatsApp, telefone (11) 3232-2206, e-mail e endereço no Polvilho. Atendimento para toda a região.",
                  "active": "contato.html", "crumbs": [("Início", "index.html"), ("Contato", "contato.html")],
                  "schemas": [LB], "body": contato_body, "priority": "0.8"})

    # ==================================================================== ORÇAMENTO
    orc_body = f'''<section class="page-hero"><div class="container"><h1>Orçamento de Dedetização e Controle de Pragas</h1>
<p>Preencha o formulário e envie direto para o nosso WhatsApp. Quanto mais detalhes, mais rápido e preciso será o orçamento.</p></div></section>
<section class="section"><div class="container content-layout">
  <form class="form" data-form="orcamento" novalidate action="https://formspree.io/f/SEU_ID_FORMSPREE" method="POST">
    <!-- Por padrão o envio abre o WhatsApp com todos os dados formatados (ver assets/js/main.js).
         Alternativa por e-mail: em main.js, defina usarFormspree: true e formspreeId. -->
    <h2 style="font-size:1.3rem;margin:0">Seus dados</h2>
    {campo("o-nome", "Nome completo", ac="name")}
    <div class="row-2">{campo("o-telefone", "Telefone/WhatsApp", "tel", ac="tel", extra='inputmode="tel" placeholder="(11) 91234-5678"')}{campo("o-email", "E-mail", "email", ac="email")}</div>
    {campo("o-cidade", "Cidade/Bairro", data_label="Cidade/Bairro", extra='placeholder="Ex.: Cajamar - Polvilho"')}
    <h2 style="font-size:1.3rem;margin:8px 0 0">Sobre o serviço</h2>
    <div class="row-2">
      <div class="field"><label for="o-imovel">Tipo de imóvel <span class="req" aria-hidden="true">*</span></label>
      <select id="o-imovel" name="imovel" required data-label="Tipo de imóvel" aria-describedby="o-imovel-erro">
        <option value="">Selecione</option><option>Casa</option><option>Apartamento</option><option>Condomínio</option><option>Empresa / comércio</option><option>Indústria</option><option>Galpão / centro de distribuição</option><option>Restaurante / cozinha</option><option>Escola / creche</option><option>Outro</option>
      </select><span class="error" id="o-imovel-erro" aria-live="polite"></span></div>
      <div class="field"><label for="o-servico">Serviço desejado <span class="req" aria-hidden="true">*</span></label>
      <select id="o-servico" name="servico" required data-label="Serviço desejado" aria-describedby="o-servico-erro">{opcoes_servico()}</select>
      <span class="error" id="o-servico-erro" aria-live="polite"></span></div>
    </div>
    {campo("o-area", "Tamanho aproximado (m²)", "number", req=False, data_label="Tamanho aproximado", extra='min="0" step="1" inputmode="numeric" placeholder="Ex.: 120"')}
    <div class="field"><label for="o-mensagem">Mensagem</label>
    <textarea id="o-mensagem" name="mensagem" data-label="Mensagem" aria-describedby="o-mensagem-erro" placeholder="Qual praga você viu, onde e há quanto tempo? Há crianças ou animais no local?"></textarea>
    <span class="error" id="o-mensagem-erro" aria-live="polite"></span></div>
    {aceite("o")}
    <button class="btn btn--whats" type="submit">{I["whatsapp"]}<span>Enviar orçamento pelo WhatsApp</span></button>
    <p class="form-status" role="status" aria-live="polite"></p>
    <p class="form-note">Campos com * são obrigatórios. Ao enviar, o WhatsApp abrirá com a mensagem pronta — basta tocar em "Enviar".</p>
  </form>
  <aside class="sidebar" aria-label="Outras formas de contato">
    <div class="cta-box"><h2>Prefere falar agora?</h2><p>{C["horario_texto"]}</p>{btn_whats("WhatsApp")}<a class="btn btn--light" href="tel:{C["tel_link"]}">{I["phone"]}<span>{C["tel_exibicao"]}</span></a></div>
    <div class="card"><h2 style="font-size:1.1rem">Dica para agilizar</h2><p>Envie fotos da praga, das fezes ou dos danos pelo WhatsApp. Isso ajuda a identificar o problema antes da vistoria.</p></div>
  </aside>
</div></section>'''
    pages.append({"path": "orcamento.html", "title": "Orçamento de Dedetização em Cajamar | Elbatec",
                  "desc": "Peça orçamento de dedetização, desratização, descupinização, caixa d'água ou fossa em Cajamar e região. Preencha e envie direto pelo WhatsApp. É rápido!",
                  "crumbs": [("Início", "index.html"), ("Orçamento", "orcamento.html")], "body": orc_body, "priority": "0.8"})

    # ==================================================================== POLÍTICA DE PRIVACIDADE
    hoje_br = datetime.date.today().strftime("%d/%m/%Y")
    pol_body = f'''<section class="page-hero"><div class="container"><h1>Política de Privacidade</h1><p>Como a Elbatec trata os seus dados pessoais, em conformidade com a Lei Geral de Proteção de Dados (Lei nº 13.709/2018).</p></div></section>
<section class="section"><div class="container prose">
<p><em>Última atualização: {hoje_br}</em></p>
<!-- REVISAR com assessoria jurídica antes de publicar. -->
<h2>1. Quem é o controlador dos dados</h2>
<p>{C["razao"]}, CNPJ {C["cnpj"]}, com sede na {endereco} ("Elbatec"), é a controladora dos dados pessoais coletados neste site.</p>
<h2>2. Quais dados coletamos</h2>
<ul><li><strong>Dados que você informa:</strong> nome, telefone/WhatsApp, e-mail, cidade/bairro, tipo de imóvel, serviço desejado, metragem e mensagem, quando preenche nossos formulários ou entra em contato.</li>
<li><strong>Dados de navegação:</strong> se você aceitar cookies, ferramentas como Google Analytics e Google Ads podem coletar dados como páginas visitadas, tipo de dispositivo, cidade aproximada e interações (por exemplo, cliques no WhatsApp).</li></ul>
<h2>3. Para que usamos os dados</h2>
<ul><li>Responder contatos e elaborar orçamentos;</li><li>Agendar e executar serviços e emitir comprovantes;</li><li>Cumprir obrigações legais e regulatórias (inclusive sanitárias e fiscais);</li><li>Medir o desempenho do site e de campanhas de publicidade, quando houver consentimento.</li></ul>
<h2>4. Bases legais</h2>
<p>Tratamos dados com base na execução de contrato ou de procedimentos preliminares (orçamento), no cumprimento de obrigação legal, no legítimo interesse (para melhorar o atendimento, respeitando seus direitos) e no consentimento (cookies de análise e publicidade).</p>
<h2>5. Envio pelo WhatsApp</h2>
<p>Ao enviar os formulários, seus dados são montados em uma mensagem e abertos no aplicativo WhatsApp, de onde você decide enviá-la. O WhatsApp é um serviço de terceiro (Meta), com política de privacidade própria. Se o envio por e-mail estiver ativo, os dados podem ser processados pelo serviço de formulários Formspree.</p>
<h2>6. Compartilhamento</h2>
<p>Não vendemos dados pessoais. Podemos compartilhá-los apenas com prestadores necessários à operação (por exemplo, ferramentas de comunicação, hospedagem e análise), com autoridades quando exigido por lei, ou com sua autorização.</p>
<h2>7. Cookies</h2>
<p>Usamos armazenamento local do navegador para lembrar sua escolha sobre cookies. Ferramentas de análise e publicidade só são ativadas se você clicar em "Aceitar" no aviso de cookies. Você pode mudar sua escolha limpando os dados do site no seu navegador.</p>
<h2>8. Por quanto tempo guardamos</h2>
<p>Mantemos os dados pelo tempo necessário para as finalidades acima e para cumprir prazos legais. Depois disso, eles são excluídos ou anonimizados.</p>
<h2>9. Seus direitos</h2>
<p>Você pode solicitar confirmação de tratamento, acesso, correção, anonimização, portabilidade, eliminação, informações sobre compartilhamento e revogação do consentimento, nos termos do art. 18 da LGPD.</p>
<h2>10. Segurança</h2>
<p>Adotamos medidas técnicas e administrativas razoáveis para proteger os dados contra acessos não autorizados e situações acidentais ou ilícitas.</p>
<h2>11. Contato do encarregado (DPO)</h2>
<p>Para exercer seus direitos ou tirar dúvidas, escreva para <a href="mailto:{C["email"]}">{C["email"]}</a> ou ligue para {C["tel_exibicao"]}. <!-- PREENCHER: nome do encarregado pelo tratamento de dados, se houver. --></p>
<h2>12. Alterações</h2>
<p>Esta política pode ser atualizada. A data da última atualização fica no início da página.</p>
</div></section>'''
    pages.append({"path": "politica-de-privacidade.html", "title": "Política de Privacidade (LGPD) | Elbatec",
                  "desc": "Saiba como a Elbatec Controle de Pragas coleta, usa e protege seus dados pessoais conforme a LGPD, e como exercer seus direitos de titular. Leia a política.",
                  "crumbs": [("Início", "index.html"), ("Política de Privacidade", "politica-de-privacidade.html")], "body": pol_body,
                  "priority": "0.3", "freq": "yearly"})

    # ==================================================================== TERMOS
    termos_body = f'''<section class="page-hero"><div class="container"><h1>Termos de Uso</h1><p>Condições para utilização do site da Elbatec Controle de Pragas.</p></div></section>
<section class="section"><div class="container prose">
<p><em>Última atualização: {hoje_br}</em></p>
<!-- REVISAR com assessoria jurídica antes de publicar. -->
<h2>1. Aceitação</h2><p>Ao acessar este site, você concorda com estes Termos de Uso e com a <a href="@/politica-de-privacidade.html">Política de Privacidade</a>. Se não concordar, não utilize o site.</p>
<h2>2. Finalidade do site</h2><p>Este site apresenta os serviços e produtos da {C["razao"]} (CNPJ {C["cnpj"]}) e permite solicitar contato e orçamentos. As informações têm caráter informativo e não substituem a vistoria técnica no local.</p>
<h2>3. Orçamentos e serviços</h2><p>Valores, prazos, garantias e condições de cada serviço são definidos no orçamento formal, após avaliação. O envio de formulário não gera contratação automática.</p>
<h2>4. Conteúdo informativo</h2><p>Dicas e artigos do blog são orientações gerais. Em caso de acidentes com animais peçonhentos ou intoxicações, procure imediatamente atendimento médico.</p>
<h2>5. Propriedade intelectual</h2><p>Textos, marcas, logotipos e layout pertencem à Elbatec ou são usados com autorização. É proibida a reprodução sem permissão prévia por escrito.</p>
<h2>6. Links externos</h2><p>O site pode conter links para serviços de terceiros (como WhatsApp e Google Maps), que têm termos e políticas próprios.</p>
<h2>7. Responsabilidade</h2><p>Buscamos manter as informações atualizadas, mas podem ocorrer imprecisões. A Elbatec não se responsabiliza por decisões tomadas exclusivamente com base no conteúdo do site, sem orientação técnica.</p>
<h2>8. Legislação e foro</h2><p>Estes termos são regidos pela legislação brasileira. Fica eleito o foro da comarca de Cajamar - SP, salvo disposição legal em contrário.</p>
<h2>9. Contato</h2><p>{C["tel_exibicao"]} · <a href="mailto:{C["email"]}">{C["email"]}</a> · {endereco}</p>
</div></section>'''
    pages.append({"path": "termos-de-uso.html", "title": "Termos de Uso | Elbatec Controle de Pragas",
                  "desc": "Leia os Termos de Uso do site da Elbatec Controle de Pragas, de Cajamar - SP: condições de uso, orçamentos, conteúdo informativo e propriedade intelectual.",
                  "crumbs": [("Início", "index.html"), ("Termos de Uso", "termos-de-uso.html")], "body": termos_body,
                  "priority": "0.3", "freq": "yearly"})

    # ==================================================================== 404
    p404 = f'''<section class="error-page"><div class="container">
<p class="code" aria-hidden="true">404</p>
<h1>Página não encontrada</h1>
<p>O endereço pode ter mudado ou não existe mais. Veja alguns links úteis:</p>
<ul class="chips" style="justify-content:center">
<li><a href="@/index.html">Página inicial</a></li><li><a href="@/servicos.html">Serviços</a></li>
<li><a href="@/servicos/dedetizacao.html">Dedetização</a></li><li><a href="@/servicos/desratizacao.html">Desratização</a></li>
<li><a href="@/areas-atendidas.html">Áreas atendidas</a></li><li><a href="@/orcamento.html">Orçamento</a></li><li><a href="@/contato.html">Contato</a></li></ul>
<div class="btn-row" style="justify-content:center">{btn_whats()}{btn_orc()}</div>
</div></section>'''
    pages.append({"path": "404.html", "title": "Página não encontrada | Elbatec Controle de Pragas",
                  "desc": "A página que você procura não foi encontrada. Acesse os serviços de dedetização e controle de pragas da Elbatec em Cajamar ou fale conosco pelo WhatsApp.",
                  "robots": "noindex,follow", "absolute_root": True, "body": p404})
    return pages
