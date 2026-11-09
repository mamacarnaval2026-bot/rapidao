# -*- coding: utf-8 -*-
"""Conteúdo das 10 páginas de serviço da Elbatec.
Textos originais. Revise e ajuste à realidade da empresa antes de publicar."""


def passos(vistoria, diagnostico, aplicacao, acompanhamento):
    return [
        ("Vistoria", vistoria),
        ("Diagnóstico", diagnostico),
        ("Aplicação", aplicacao),
        ("Garantia e retorno", acompanhamento),
        ("Certificado", "Ao final, emitimos o comprovante de execução do serviço, com data, área tratada, produtos utilizados e orientações. Ele é aceito como documento de controle por síndicos, gestores e fiscalização."),
    ]


def garantia(nome):
    return (f"<p>Todo serviço de {nome} realizado pela Elbatec tem prazo de garantia informado por escrito no orçamento e no comprovante de execução. "
            "O prazo varia conforme o tipo de imóvel, o nível de infestação e as condições do local, por isso ele é definido depois da vistoria — e não antes. "
            "Durante a garantia, se a praga tratada voltar a aparecer nas áreas atendidas, basta entrar em contato para agendarmos o retorno técnico.</p>"
            "<p>Ao final de cada atendimento, entregamos o <strong>certificado (comprovante) de execução do serviço</strong>, com identificação da empresa, "
            "endereço atendido, data, pragas-alvo, produtos e princípios ativos utilizados, número de registro dos produtos e orientações pós-serviço. "
            "Esse documento é exigido em condomínios, restaurantes, escolas, empresas do setor de alimentos e em auditorias de clientes, e deve ficar arquivado.</p>")


SEG_PADRAO = ("<p>Utilizamos apenas produtos saneantes com registro ou notificação na ANVISA, de uso profissional, aplicados por equipe treinada e com equipamentos de proteção. "
              "Antes do serviço, você recebe por escrito as orientações de preparo do ambiente e o tempo recomendado para retorno de pessoas e animais, que depende do produto e do método escolhido.</p>")

SERVICOS = [
# ---------------------------------------------------------------- 1
{
"slug": "dedetizacao", "nome": "Dedetização", "nome_curto": "Dedetização", "icone": "bug",
"resumo": "Controle de baratas, formigas, aranhas e outros insetos rasteiros em casas, condomínios e empresas.",
"title": "Dedetização em Cajamar e Região | Elbatec",
"desc": "Dedetização em Cajamar, Polvilho e Jordanésia contra baratas, formigas e aranhas. Produtos registrados na ANVISA e certificado. Peça seu orçamento!",
"h1": "Dedetização em Cajamar e Região",
"lead": "Controle profissional de baratas, formigas, aranhas e outros insetos em residências, condomínios, comércios e empresas de Cajamar, Polvilho, Jordanésia e cidades vizinhas.",
"img": "dedetizacao-cajamar.webp", "img_alt": "Técnico da Elbatec realizando dedetização com equipamento de proteção em área interna",
"img_cap": "Aplicação profissional com equipamento de proteção individual. (Imagem ilustrativa — substitua por foto real da equipe.)",
"oque": """<p>Dedetização é o conjunto de técnicas usadas para controlar insetos que vivem e se reproduzem dentro e ao redor das edificações — principalmente baratas, formigas, aranhas, escorpiões, traças e cupins-de-solo em fase inicial. Mais do que "passar veneno", uma dedetização bem-feita começa por entender por onde a praga entra, onde ela se abriga e do que se alimenta. Só depois disso escolhemos o produto, a formulação (gel, pó, líquido, isca granulada) e a forma de aplicação.</p>
<p>Em Cajamar, o crescimento de condomínios e de centros de distribuição ao longo da Rodovia Anhanguera aumentou a circulação de mercadorias, caixas e paletes — um caminho comum para baratas e formigas chegarem a novos imóveis. Por isso, o ideal é não esperar a infestação ficar visível: contrate a dedetização quando notar os primeiros sinais, ao se mudar para um imóvel novo, antes de reformas e de forma periódica em locais que manipulam alimentos.</p>
<p>Empresas de alimentação, cozinhas industriais, escolas e condomínios normalmente precisam manter um programa contínuo de controle, com visitas programadas e registros. Para residências, a frequência depende do histórico do imóvel e do entorno; explicamos isso em detalhes no artigo <a href="@/blog/de-quanto-em-quanto-tempo-dedetizar.html">de quanto em quanto tempo dedetizar</a>.</p>""",
"sinais_titulo": "Sinais de que é hora de dedetizar",
"sinais": [
 "Baratas vistas à noite na cozinha, banheiros, ralos ou caixas de gordura — para cada uma visível, costuma haver muitas escondidas.",
 "Pequenas fezes escuras (parecidas com borra de café) em gavetas, atrás da geladeira e dentro de armários.",
 "Ootecas (cápsulas de ovos de barata) em frestas, rodapés e motores de eletrodomésticos.",
 "Trilhas de formigas em bancadas, potes de açúcar, tomadas e batentes de portas.",
 "Teias e aranhas frequentes em cantos, garagens, depósitos e jardins.",
 "Cheiro adocicado e desagradável em armários fechados, típico de infestações maiores de baratas.",
],
"passos": passos(
 "Um técnico avalia o imóvel, identifica as espécies presentes, os pontos de abrigo e as rotas de entrada (ralos, frestas, tubulações).",
 "Definimos o método mais adequado: gel em pontos estratégicos, pulverização, polvilhamento em frestas ou iscas, considerando a presença de crianças e animais.",
 "A aplicação é feita com equipamentos calibrados e EPIs, priorizando locais de abrigo e reduzindo exposição desnecessária em áreas de convivência.",
 "Orientamos sobre limpeza, vedação e armazenamento. Se a praga voltar dentro do prazo de garantia, agendamos o retorno."),
"seguranca": SEG_PADRAO + """<p>Em residências com bebês, crianças pequenas, gestantes, idosos ou animais de estimação, priorizamos formulações de baixa exposição, como iscas em gel aplicadas em frestas e pontos fora do alcance. Em geral, pedimos que comedouros, bebedouros, brinquedos e alimentos sejam guardados, que aquários sejam cobertos (com a bomba de ar desligada durante a aplicação) e que pessoas e pets aguardem o período indicado no laudo antes de voltar ao ambiente tratado. Pássaros e peixes são mais sensíveis e merecem atenção especial — avise-nos com antecedência.</p>""",
"publico": """<p>Fazemos dedetização em casas e apartamentos, áreas comuns de condomínios (casas de lixo, garagens, poços de elevador, caixas de gordura), restaurantes, padarias, mercados, escolas, escritórios, indústrias e galpões logísticos. Para empresas, oferecemos contratos com visitas periódicas e documentação para auditorias — veja a página <a href="@/empresas-e-condominios.html">empresas e condomínios</a>.</p>""",
"garantia": garantia("dedetização"),
"faq_titulo": "dedetização",
"faq": [
 ("Preciso sair de casa durante a dedetização?", "Depende do método. Com gel e iscas, muitas vezes não é necessário sair; com pulverização, recomendamos que pessoas e animais fiquem fora do ambiente pelo tempo indicado no orçamento, que varia conforme o produto."),
 ("A dedetização tem cheiro forte?", "Os produtos profissionais atuais costumam ter odor leve ou nenhum odor. Em pulverizações, pode haver um cheiro discreto que desaparece após a ventilação do ambiente."),
 ("Em quanto tempo as baratas desaparecem?", "É normal ver mais insetos nos primeiros dias, porque eles saem dos esconderijos afetados pelo produto. A redução costuma ser perceptível nas semanas seguintes, conforme o ciclo da praga e o método aplicado."),
 ("Posso limpar a casa depois do serviço?", "Pode limpar normalmente as áreas de convivência, mas evite lavar rodapés, frestas e os pontos onde o gel foi aplicado durante o período orientado pelo técnico."),
 ("Vocês emitem certificado para condomínio e empresa?", "Sim. Todo serviço gera comprovante de execução com produtos utilizados, área tratada e data, documento usado por síndicos, gestores e em fiscalizações."),
],
"relacionados": ["desinsetizacao", "controle-de-escorpioes", "sanitizacao"],
},
# ---------------------------------------------------------------- 2
{
"slug": "desratizacao", "nome": "Desratização", "nome_curto": "Desratização", "icone": "rat",
"resumo": "Controle de ratos e camundongos com iscas protegidas, monitoramento e vedação de acessos.",
"title": "Desratização em Cajamar | Controle de Ratos | Elbatec",
"desc": "Desratização em Cajamar e região com porta-iscas lacrados, monitoramento e orientação de vedação. Para casas, condomínios e galpões. Solicite orçamento.",
"h1": "Desratização em Cajamar e Região",
"lead": "Controle de ratos e camundongos em residências, condomínios, comércios, indústrias e centros de distribuição, com iscas protegidas, monitoramento e orientação de vedação.",
"img": "desratizacao-cajamar.webp", "img_alt": "Porta-isca lacrado instalado junto à parede externa de um galpão",
"img_cap": "Porta-iscas lacrados e numerados permitem monitorar a atividade de roedores. (Imagem ilustrativa.)",
"oque": """<p>Desratização é o controle de roedores sinantrópicos — ratazana (<em>Rattus norvegicus</em>), rato-de-telhado (<em>Rattus rattus</em>) e camundongo (<em>Mus musculus</em>). Cada espécie tem hábitos diferentes: a ratazana costuma viver em tocas no solo, galerias de esgoto e margens de córregos; o rato-de-telhado prefere forros, sótãos e árvores; o camundongo se instala dentro de móveis, depósitos e paredes. Identificar a espécie muda completamente a estratégia.</p>
<p>Ratos transmitem doenças como leptospirose e hantavirose, contaminam alimentos e estoques e roem fios elétricos — o que pode causar curtos-circuitos e incêndios. Em uma região com tantos galpões, áreas verdes e córregos como Cajamar e o entorno da Anhanguera, a pressão de roedores costuma ser alta, principalmente em épocas de chuva e de obras.</p>
<p>Contrate a desratização ao primeiro sinal de presença, antes de armazenar mercadorias em um galpão novo, após enchentes e em qualquer estabelecimento que manipule ou estoque alimentos. Em empresas, o controle de roedores é contínuo: os porta-iscas são inspecionados periodicamente e os resultados ficam registrados em mapa e relatório.</p>""",
"sinais_titulo": "Sinais da presença de ratos",
"sinais": [
 "Fezes escuras em formato de grão de arroz (camundongo) ou de azeitona (ratazana) perto de alimentos, rodapés e depósitos.",
 "Embalagens, sacarias, fios, mangueiras ou portas roídas.",
 "Barulhos de arranhar ou correr no forro e nas paredes, principalmente à noite.",
 "Manchas de gordura escura nas paredes ao longo das rotas que os ratos usam.",
 "Tocas e buracos no solo, junto a muros, canteiros e calçadas.",
 "Cheiro forte de urina em ambientes fechados e reações agitadas de cães e gatos.",
],
"passos": passos(
 "Mapeamos sinais de atividade, tocas, rotas e pontos de entrada, dentro e fora do imóvel, incluindo telhado, ralos e áreas externas.",
 "Identificamos a espécie e definimos o tipo de isca (bloco, pellet ou pasta), a quantidade e a posição dos porta-iscas.",
 "Instalamos porta-iscas com trava, fixados e identificados, fora do alcance de crianças e animais domésticos. Em áreas internas sensíveis, usamos armadilhas mecânicas ou adesivas.",
 "Fazemos inspeções de reposição e orientamos sobre vedações, poda, lixo e armazenamento para que os roedores não voltem."),
"seguranca": SEG_PADRAO + """<p>Os raticidas usados profissionalmente ficam dentro de porta-iscas com trava, presos ao piso ou à parede, o que impede o acesso de crianças e de cães e gatos. Nunca deixamos iscas soltas em áreas de convivência. Em locais com animais de estimação, combinamos a posição de cada ponto e, quando necessário, usamos métodos mecânicos. Após o serviço, recolhemos as iscas não consumidas e orientamos o descarte seguro de roedores mortos, usando luvas.</p>""",
"publico": """<p>Atendemos casas com quintal, condomínios horizontais e verticais, restaurantes, supermercados, indústrias, transportadoras e centros de distribuição. Para galpões e indústrias, montamos um mapa de porta-iscas com numeração e relatório de consumo em cada visita, documentação frequentemente exigida em auditorias de clientes. Veja também o serviço de <a href="@/servicos/limpeza-de-fossa-e-desentupimento.html">limpeza de caixa de gordura</a>, que reduz a atração de roedores.</p>""",
"garantia": garantia("desratização"),
"faq_titulo": "desratização",
"faq": [
 ("Os ratos vão morrer dentro das paredes e causar mau cheiro?", "Pode acontecer, mas é minimizado com a escolha da isca, a posição dos porta-iscas e a vedação de acessos. Orientamos o que fazer caso haja odor."),
 ("A isca é perigosa para meu cachorro ou gato?", "Os raticidas são tóxicos para mamíferos, por isso usamos porta-iscas com trava fixados no local. Em casas com pets, combinamos posições seguras e alternativas mecânicas quando necessário."),
 ("Quanto tempo leva para controlar os ratos?", "Depende do nível de infestação e das condições do local. Em geral, a redução da atividade é percebida nas primeiras semanas, e o resultado se mantém quando as falhas estruturais são corrigidas."),
 ("Por que os ratos voltam?", "Os principais motivos são acessos abertos, lixo exposto, alimento disponível e vizinhança infestada. Por isso, a vedação e a organização são parte essencial do serviço."),
 ("Vocês fazem contrato de desratização para empresas?", "Sim, com visitas programadas, mapa de porta-iscas, relatórios e comprovantes de execução para auditorias."),
],
"relacionados": ["dedetizacao", "limpeza-de-fossa-e-desentupimento", "sanitizacao"],
},
# ---------------------------------------------------------------- 3
{
"slug": "descupinizacao", "nome": "Descupinização", "nome_curto": "Descupinização", "icone": "wood",
"resumo": "Tratamento de cupins de madeira seca e de solo em móveis, telhados, batentes e estruturas.",
"title": "Descupinização em Cajamar | Cupim de Madeira e Solo",
"desc": "Descupinização em Cajamar e região contra cupim de madeira seca e de solo, em móveis, telhados e batentes. Vistoria técnica e certificado. Fale conosco.",
"h1": "Descupinização em Cajamar e Região",
"lead": "Tratamento de cupins de madeira seca e de cupins subterrâneos (de solo) em móveis, portas, forros, telhados, pisos e estruturas de imóveis residenciais e comerciais.",
"img": "descupinizacao-cajamar.webp", "img_alt": "Viga de madeira de telhado sendo inspecionada para identificar cupins",
"img_cap": "A inspeção das madeiras define o tipo de cupim e o método de tratamento. (Imagem ilustrativa.)",
"oque": """<p>Descupinização é o tratamento para controlar cupins, insetos sociais que se alimentam de celulose e podem comprometer móveis, batentes, rodapés, forros, telhados, livros e até estruturas. Existem dois grupos principais, que exigem técnicas diferentes. O <strong>cupim de madeira seca</strong> vive dentro da própria peça de madeira, em colônias pequenas, e denuncia sua presença pelos resíduos em forma de grãos. O <strong>cupim subterrâneo (de solo)</strong> forma colônias enormes no solo e chega à madeira por túneis de terra, podendo atravessar paredes, conduítes e pequenas fissuras no concreto.</p>
<p>Como os cupins trabalham escondidos, quando o dano aparece a infestação normalmente já tem meses ou anos. Por isso vale contratar uma vistoria ao comprar ou alugar um imóvel, antes de reformas e de instalar móveis planejados, ao notar revoadas de "aleluias" e sempre que encontrar resíduos ou madeira oca. Para aprender a reconhecer os sinais, leia nosso guia <a href="@/blog/como-identificar-cupins.html">como identificar cupins</a>.</p>""",
"sinais_titulo": "Sinais de cupins no imóvel",
"sinais": [
 "Montinhos de grãos parecidos com areia ou pó de café perto de móveis, portas e rodapés (cupim de madeira seca).",
 "Pequenos furos na superfície da madeira, por onde os resíduos são expelidos.",
 "Madeira que soa oca ou cede quando pressionada.",
 "Túneis de terra (galerias) em paredes, rodapés, conduítes e pilares (cupim de solo).",
 "Revoadas de insetos alados (aleluias) e asas soltas perto de janelas e lâmpadas, normalmente em dias quentes e úmidos.",
 "Portas e janelas emperrando, pisos de madeira estufados ou forros cedendo.",
],
"passos": passos(
 "Inspecionamos madeiras, forros, telhado, rodapés e áreas externas para encontrar focos, galerias e a extensão da infestação.",
 "Identificamos se é cupim de madeira seca ou de solo e propomos o tratamento: injeção, pincelamento, pulverização ou barreira química no solo.",
 "Aplicamos o produto diretamente nas galerias e nas peças afetadas. Para cupim de solo, criamos barreiras em pontos críticos da edificação, com perfurações quando necessário.",
 "Orientamos sobre umidade, troca de peças comprometidas e retorno técnico. Caso surjam novos sinais na área tratada dentro da garantia, voltamos para avaliar."),
"seguranca": SEG_PADRAO + """<p>Na descupinização de móveis, o tratamento é localizado e o produto vai para dentro da madeira, o que reduz a exposição no ambiente. Para barreiras de solo, as perfurações são feitas em pontos definidos e vedadas após a aplicação. Pedimos que alimentos, utensílios e roupas sejam retirados dos armários tratados e que crianças e animais não tenham contato com as superfícies até a secagem, conforme o tempo indicado na orientação escrita.</p>""",
"publico": """<p>Atendemos casas e sobrados com telhado de madeira, apartamentos com móveis planejados e pisos de madeira, condomínios, igrejas, escolas, bibliotecas, depósitos de paletes e empresas. Em galpões logísticos, paletes e embalagens de madeira podem trazer cupins de outras regiões; a inspeção periódica evita que o problema chegue à estrutura.</p>""",
"garantia": garantia("descupinização"),
"faq_titulo": "descupinização",
"faq": [
 ("Como sei se é cupim de madeira seca ou de solo?", "O cupim de madeira seca deixa resíduos em grãos e furinhos na madeira. O de solo forma túneis de terra nas paredes e estruturas. Na vistoria, o técnico confirma a espécie."),
 ("Preciso trocar o móvel atacado por cupim?", "Nem sempre. Se a estrutura da peça ainda estiver firme, o tratamento costuma resolver. Peças muito comprometidas podem precisar de substituição, e indicamos isso na vistoria."),
 ("O tratamento de cupim de solo exige quebrar o piso?", "Em alguns casos, são feitas pequenas perfurações para levar o produto até o solo, depois vedadas. A necessidade é avaliada caso a caso."),
 ("As aleluias significam que tenho cupim em casa?", "São um sinal de alerta: indicam colônias maduras por perto. Se encontrar asas soltas dentro do imóvel, vale agendar uma inspeção."),
 ("Dedetização comum mata cupim?", "Não necessariamente. O cupim exige aplicação direcionada nas galerias ou no solo, com técnica e produto específicos."),
],
"relacionados": ["dedetizacao", "desinsetizacao", "sanitizacao"],
},
# ---------------------------------------------------------------- 4
{
"slug": "desinsetizacao", "nome": "Desinsetização", "nome_curto": "Desinsetização", "icone": "mosquito",
"resumo": "Controle de mosquitos, pulgas, carrapatos, traças e insetos voadores ou rasteiros.",
"title": "Desinsetização em Cajamar | Pulgas, Mosquitos e Traças",
"desc": "Desinsetização em Cajamar e região contra mosquitos, pulgas, carrapatos e traças. Atendemos casas, condomínios e empresas com certificado. Peça orçamento.",
"h1": "Desinsetização em Cajamar e Região",
"lead": "Controle de mosquitos, pulgas, carrapatos, traças, moscas e outros insetos em residências, quintais, condomínios, empresas e áreas externas.",
"img": "desinsetizacao-cajamar.webp", "img_alt": "Quintal gramado com área externa sendo tratada contra pulgas e carrapatos",
"img_cap": "Áreas externas, gramados e canis são pontos críticos para pulgas e carrapatos. (Imagem ilustrativa.)",
"oque": """<p>Desinsetização é o controle de insetos e artrópodes que incomodam, picam ou transmitem doenças. Enquanto a dedetização costuma focar em baratas e formigas, a desinsetização abrange um grupo mais amplo: mosquitos (incluindo o <em>Aedes aegypti</em>, transmissor de dengue, zika e chikungunya), pernilongos, pulgas, carrapatos, moscas, traças de livros e de roupas, percevejos e mosquitinhos de ralo.</p>
<p>Cada praga pede uma abordagem diferente. Pulgas e carrapatos, por exemplo, passam boa parte do ciclo de vida fora do animal — no gramado, em frestas do piso, no canil e em tapetes —, por isso não basta tratar o pet. Mosquitos se reproduzem em água parada, e o trabalho inclui eliminar criadouros. Traças vivem em locais escuros, úmidos e com papel ou tecido.</p>
<p>Em Cajamar e região, com muitas áreas verdes, chácaras e córregos, a pressão de mosquitos e carrapatos aumenta nos meses quentes e chuvosos. Contrate a desinsetização quando houver picadas frequentes, infestação de pulgas após a chegada de um animal, carrapatos no quintal ou traças danificando roupas e documentos.</p>""",
"sinais_titulo": "Sinais de infestação de insetos",
"sinais": [
 "Picadas frequentes nas pernas e tornozelos, principalmente após contato com tapetes, sofás ou gramado (pulgas).",
 "Carrapatos nos cães, em muros, frestas e na casinha do animal.",
 "Muitos pernilongos dentro de casa, mesmo com telas, e larvas em recipientes com água.",
 "Mosquitinhos saindo dos ralos do banheiro e da cozinha.",
 "Roupas, livros, papéis e caixas com furos ou manchas, e pequenos insetos prateados (traças).",
 "Moscas em excesso em áreas de lixo, cozinhas e áreas de animais.",
],
"passos": passos(
 "Avaliamos o imóvel, áreas externas, criadouros e abrigos, e verificamos se há animais de estimação ou de criação no local.",
 "Identificamos o inseto e combinamos o método: pulverização residual, nebulização, tratamento de ralos, gramados e frestas, ou ações físicas como eliminação de criadouros.",
 "Aplicamos o produto nas áreas de abrigo e reprodução. Em casos de pulgas e carrapatos, tratamos ambiente interno e externo de forma integrada.",
 "Orientamos sobre o tratamento veterinário dos pets, limpeza, aspiração e manutenção, e acompanhamos o resultado dentro da garantia."),
"seguranca": SEG_PADRAO + """<p>Em casos de pulgas e carrapatos, o tratamento do ambiente precisa ser combinado com o tratamento dos animais, indicado pelo médico-veterinário — nós cuidamos do ambiente. Durante a aplicação, os pets devem ficar em outro local e só retornar após a secagem e a ventilação. Comedouros, bebedouros, caminhas e brinquedos devem ser recolhidos. Em nebulizações, informamos o tempo de reentrada, que costuma ser maior do que em aplicações localizadas.</p>""",
"publico": """<p>Atendemos casas com quintal e jardim, chácaras, canis e hotéis para pets, condomínios (áreas verdes, playgrounds, casas de máquinas), escolas, hotéis, hospitais, empresas e áreas externas de galpões. Para controle de mosquitos em condomínios e empresas, combinamos a desinsetização com a eliminação de criadouros e com a <a href="@/servicos/limpeza-caixa-dagua.html">limpeza de caixa d'água</a>.</p>""",
"garantia": garantia("desinsetização"),
"faq_titulo": "desinsetização",
"faq": [
 ("Qual a diferença entre dedetização e desinsetização?", "Na prática, os termos se sobrepõem. Usamos desinsetização para o controle de insetos como mosquitos, pulgas, carrapatos e traças, e dedetização para baratas, formigas e aranhas."),
 ("Tratar só o cachorro resolve as pulgas?", "Normalmente não. A maior parte das pulgas, ovos e larvas fica no ambiente. É preciso tratar o animal (com orientação veterinária) e o ambiente ao mesmo tempo."),
 ("A nebulização acaba com os pernilongos de vez?", "A nebulização reduz os insetos adultos, mas o resultado duradouro depende de eliminar criadouros de água parada no imóvel e no entorno."),
 ("Como acabar com os mosquitinhos do ralo?", "Eles se criam na matéria orgânica acumulada no sifão. O tratamento combina limpeza do ralo com aplicação de produto específico."),
 ("Em quanto tempo posso voltar com meu pet para casa?", "O tempo depende do produto e do método. Informamos o período exato por escrito antes do serviço."),
],
"relacionados": ["dedetizacao", "controle-de-escorpioes", "sanitizacao"],
},
# ---------------------------------------------------------------- 5
{
"slug": "controle-de-escorpioes", "nome": "Controle de escorpiões", "nome_curto": "Controle de escorpiões", "icone": "scorpion",
"resumo": "Manejo integrado para reduzir escorpiões, com vistoria, eliminação de abrigos e controle de baratas.",
"title": "Controle de Escorpiões em Cajamar e Região | Elbatec",
"desc": "Controle de escorpiões em Cajamar, Polvilho e Jordanésia com vistoria, vedação de acessos e controle de baratas. Proteja sua família. Peça um orçamento.",
"h1": "Controle de Escorpiões em Cajamar e Região",
"lead": "Manejo integrado para reduzir a presença de escorpiões em casas, condomínios, escolas e empresas: vistoria, eliminação de abrigos, controle de baratas e orientação de vedação.",
"img": "controle-de-escorpioes-cajamar.webp", "img_alt": "Ralo com tela de proteção e soleira vedada para impedir entrada de escorpiões",
"img_cap": "Telas em ralos e vedação de soleiras são medidas centrais contra escorpiões. (Imagem ilustrativa.)",
"artigo_lower": True,
"oque": """<p>O controle de escorpiões é diferente do controle de outros insetos. O escorpião-amarelo (<em>Tityus serrulatus</em>), espécie mais comum em áreas urbanas do Sudeste, se reproduz sem precisar de macho, vive escondido em frestas, entulho, caixas de inspeção e redes de esgoto, e consegue ficar meses sem se alimentar. Além disso, ele não é tão sensível aos inseticidas convencionais como as baratas. Por isso, aplicar produto sozinho raramente resolve.</p>
<p>O trabalho eficiente é o <strong>manejo integrado</strong>: localizar abrigos, retirar entulhos e materiais acumulados, vedar acessos, telar ralos, controlar as baratas (o principal alimento dos escorpiões) e, quando indicado, aplicar produtos em pontos estratégicos. Cajamar e cidades vizinhas têm muitas áreas em obra, terrenos com vegetação e galerias pluviais — ambientes que favorecem escorpiões, principalmente nos meses quentes.</p>
<p>Contrate o serviço ao encontrar o primeiro escorpião, sobretudo em imóveis com crianças, idosos e animais. Em escolas, creches e condomínios, a prevenção deve ser contínua. Veja dicas práticas no artigo <a href="@/blog/escorpioes-como-prevenir-em-casa.html">escorpiões: como prevenir em casa</a>.</p>""",
"sinais_titulo": "Sinais de risco de escorpiões",
"sinais": [
 "Escorpiões vistos em ralos, banheiros, áreas de serviço, garagens ou quintal — mesmo que apenas um.",
 "Presença frequente de baratas, que servem de alimento para os escorpiões.",
 "Entulho, telhas, tijolos, lenha ou materiais de construção acumulados no terreno.",
 "Caixas de inspeção, de gordura e de esgoto com tampas mal vedadas.",
 "Vizinhança com terrenos baldios, obras ou córregos.",
 "Frestas em rodapés, soleiras de portas e ralos sem tela ou sem sistema abre-fecha.",
],
"passos": passos(
 "Percorremos o imóvel e o entorno buscando abrigos, acessos e condições que favorecem escorpiões, inclusive à noite quando necessário.",
 "Elaboramos um plano com ações físicas (vedação, telas, limpeza de abrigos) e químicas (controle de baratas e aplicação em pontos estratégicos).",
 "Executamos o controle de baratas em ralos, caixas e galerias e aplicamos o produto nos pontos de abrigo, sempre seguindo as orientações técnicas.",
 "Entregamos uma lista de melhorias estruturais e fazemos visitas de acompanhamento conforme o plano contratado."),
"seguranca": SEG_PADRAO + """<p>O maior risco dos escorpiões é para crianças, idosos e animais de pequeno porte. Por isso, além do controle, orientamos medidas de proteção: sacudir roupas, calçados e toalhas antes de usar, afastar camas e berços das paredes, não colocar a mão em buracos e frestas e manter o quintal limpo. <strong>Em caso de picada, procure imediatamente o pronto-socorro mais próximo</strong> — e, se possível, leve o escorpião para identificação. O serviço de controle não substitui o atendimento médico.</p>""",
"publico": """<p>Atendemos casas, sobrados e chácaras, condomínios (casas de lixo, caixas de passagem, jardins e playgrounds), escolas e creches, empresas, indústrias e galpões. Em condomínios, recomendamos um plano contínuo com inspeção das caixas e controle de baratas — veja <a href="@/empresas-e-condominios.html">soluções para condomínios</a>.</p>""",
"garantia": garantia("controle de escorpiões"),
"faq_titulo": "controle de escorpiões",
"faq": [
 ("Dedetização comum mata escorpião?", "Não é suficiente sozinha. O escorpião é menos sensível aos inseticidas e fica abrigado. O controle exige manejo integrado: vedação, limpeza de abrigos e controle de baratas."),
 ("Encontrei um escorpião em casa. Tem mais?", "É possível. O escorpião-amarelo se reproduz sem macho e pode haver outros abrigados no imóvel ou no entorno. Uma vistoria ajuda a identificar a origem."),
 ("O que fazer em caso de picada?", "Lave o local com água e sabão e procure imediatamente atendimento médico, principalmente em crianças e idosos. Não faça torniquete, não corte nem sugue o local."),
 ("Telas de ralo realmente ajudam?", "Sim. Ralos são uma das principais vias de entrada. Ralos com tela ou sistema abre-fecha, somados à vedação de soleiras e rodapés, reduzem muito o risco."),
 ("Vocês atendem escolas e creches?", "Sim, com planejamento de horários, produtos e métodos adequados ao ambiente e comprovante de execução."),
],
"relacionados": ["dedetizacao", "limpeza-de-fossa-e-desentupimento", "desinsetizacao"],
},
# ---------------------------------------------------------------- 6
{
"slug": "controle-de-pombos", "nome": "Controle e manejo de pombos", "nome_curto": "Controle de pombos", "icone": "bird",
"resumo": "Telas, espículas e limpeza técnica para impedir que pombos se instalem em telhados e fachadas.",
"title": "Controle de Pombos em Cajamar | Telas e Espículas",
"desc": "Controle e manejo de pombos em Cajamar e região com telas, espículas e limpeza de fezes. Soluções físicas e humanitárias para casas e galpões. Peça orçamento.",
"h1": "Controle de Pombos em Cajamar e Região",
"lead": "Manejo de pombos com métodos físicos e humanitários — telas, espículas e fios tensionados — e limpeza técnica de fezes e ninhos em telhados, fachadas, galpões e condomínios.",
"img": "controle-de-pombos-cajamar.webp", "img_alt": "Espículas instaladas em beiral de prédio para impedir pouso de pombos",
"img_cap": "Espículas e telas impedem pouso e nidificação sem ferir as aves. (Imagem ilustrativa.)",
"oque": """<p>O pombo-doméstico se adaptou muito bem às cidades: encontra alimento fácil, abrigo em telhados, forros, beirais, marquises, aparelhos de ar-condicionado e estruturas metálicas de galpões. O problema é que as fezes acumuladas são corrosivas, sujam fachadas, entopem calhas e podem abrigar fungos e bactérias associados a doenças respiratórias, além de piolhos e ácaros das aves.</p>
<p>O manejo de pombos não envolve venenos. O trabalho é feito com <strong>barreiras físicas</strong> que impedem o pouso e a construção de ninhos — telas de proteção, espículas de policarbonato ou aço inox, fios tensionados — e com a retirada dos atrativos (alimento e água). Antes da instalação, fazemos a limpeza e a desinfecção das áreas contaminadas, com equipamentos de proteção respiratória.</p>
<p>Contrate o serviço quando os pombos começarem a frequentar um beiral, forro ou telhado, antes que formem ninhos — quanto mais tempo eles permanecem, mais fiéis ao local ficam. Em galpões logísticos de Cajamar, pombos nas estruturas de cobertura podem contaminar mercadorias e docas, e a proteção é parte das boas práticas exigidas por muitos clientes.</p>""",
"sinais_titulo": "Sinais de que os pombos estão se instalando",
"sinais": [
 "Acúmulo de fezes em parapeitos, beirais, calhas, aparelhos de ar-condicionado e docas.",
 "Ninhos, penas e gravetos em forros, vãos de telhado e estruturas metálicas.",
 "Barulho de aves no forro, principalmente ao amanhecer.",
 "Calhas entupidas e manchas em fachadas e telhas.",
 "Grupos de pombos pousando sempre nos mesmos pontos.",
 "Pessoas alimentando aves no entorno do imóvel ou do condomínio.",
],
"passos": passos(
 "Identificamos os pontos de pouso, abrigo e nidificação e avaliamos acessos, altura e necessidade de equipamentos de trabalho em altura.",
 "Escolhemos a solução para cada ponto: tela, espícula, fio tensionado ou fechamento de vãos, com orçamento detalhado por metro ou por área.",
 "Fazemos a limpeza e a desinfecção das fezes e ninhos, e instalamos as barreiras físicas com fixação adequada a cada superfície.",
 "Revisamos a instalação e orientamos sobre manutenção, alimentação de aves e pontos que possam surgir no futuro."),
"seguranca_titulo": "Métodos humanitários e segurança na limpeza",
"seguranca": """<p>O controle de pombos é feito sem venenos e sem ferir as aves: as barreiras apenas impedem o pouso e a entrada. Quando há ninhos com ovos ou filhotes, avaliamos a melhor forma de conduzir a situação antes de fechar o acesso. Na limpeza de fezes, a equipe usa proteção respiratória, umedece o material para evitar poeira e aplica desinfetante saneante com registro ou notificação na ANVISA. Moradores, crianças e animais devem se manter afastados da área durante a limpeza.</p>
<p>Serviços em altura são realizados com equipamentos de segurança adequados. Informe no orçamento a altura aproximada e o tipo de acesso (escada, plataforma, telhado) para planejarmos o atendimento.</p>""",
"publico": """<p>Atendemos casas e sobrados, prédios residenciais e comerciais, condomínios, igrejas, escolas, indústrias, supermercados e galpões logísticos. Para grandes coberturas, o orçamento é feito após vistoria técnica no local.</p>""",
"garantia": garantia("controle de pombos").replace("se a praga tratada voltar a aparecer nas áreas atendidas", "se houver falha na instalação das barreiras"),
"faq_titulo": "controle de pombos",
"faq": [
 ("Vocês matam os pombos?", "Não. Usamos apenas métodos físicos (telas, espículas e fios) que impedem o pouso e a entrada, sem ferir as aves."),
 ("Espícula machuca o pombo?", "Não. As espículas têm pontas rombudas; elas apenas impedem que a ave consiga pousar."),
 ("Tela ou espícula: qual é melhor?", "Depende do local. Telas fecham vãos e áreas onde os pombos entram; espículas e fios protegem beirais, parapeitos e superfícies de pouso. Indicamos a solução após a vistoria."),
 ("As fezes de pombo fazem mal à saúde?", "As fezes acumuladas podem abrigar fungos e bactérias. A limpeza deve ser feita com proteção respiratória e desinfetante adequado."),
 ("Vocês atendem galpões altos?", "Sim, com planejamento de acesso e equipamentos de segurança para trabalho em altura."),
],
"relacionados": ["sanitizacao", "desratizacao", "limpeza-caixa-dagua"],
},
# ---------------------------------------------------------------- 7
{
"slug": "sanitizacao", "nome": "Sanitização e desinfecção de ambientes", "nome_curto": "Sanitização", "icone": "spray",
"resumo": "Desinfecção de ambientes e superfícies com saneantes regularizados, para casas e empresas.",
"title": "Sanitização de Ambientes em Cajamar | Elbatec",
"desc": "Sanitização e desinfecção de ambientes em Cajamar e região para empresas, escolas, condomínios e residências. Saneantes regularizados e certificado. Saiba mais.",
"h1": "Sanitização de Ambientes em Cajamar e Região",
"lead": "Desinfecção de ambientes e superfícies em empresas, escolas, academias, veículos, condomínios e residências, com saneantes regularizados e comprovante de execução.",
"img": "sanitizacao-de-ambientes-cajamar.webp", "img_alt": "Profissional fazendo sanitização de escritório com pulverizador e equipamento de proteção",
"img_cap": "Sanitização de superfícies de alto contato em ambiente corporativo. (Imagem ilustrativa.)",
"oque": """<p>Sanitização é a aplicação de produtos desinfetantes para reduzir microrganismos — bactérias, vírus e fungos — em superfícies e ambientes. Ela é complementar à limpeza: primeiro se remove a sujeira visível, depois se aplica o desinfetante adequado, respeitando o tempo de contato indicado pelo fabricante. Sem a limpeza prévia, a matéria orgânica reduz a eficácia de qualquer produto.</p>
<p>O serviço é indicado após casos de doenças contagiosas entre ocupantes, depois de enchentes e infiltrações, na reabertura de imóveis fechados por muito tempo, após a retirada de fezes de pombos ou roedores, e de forma periódica em locais de grande circulação: escolas, academias, consultórios, escritórios, refeitórios, vestiários e frotas de veículos.</p>
<p>Usamos técnicas como pulverização, nebulização e aplicação manual em superfícies de alto contato (maçanetas, corrimãos, botoeiras de elevador, bancadas, teclados, catracas), escolhendo o produto conforme o tipo de ambiente e de material.</p>""",
"sinais_titulo": "Quando a sanitização é recomendada",
"sinais": [
 "Casos de doenças contagiosas entre moradores, alunos ou colaboradores.",
 "Imóveis que passaram por enchente, vazamento ou infiltração.",
 "Ambientes com mofo, odores persistentes ou fechados por longo período.",
 "Áreas onde houve infestação de roedores ou acúmulo de fezes de pombos.",
 "Locais de grande circulação: escolas, academias, clínicas, refeitórios e vestiários.",
 "Entrega ou recebimento de imóvel, mudança e reabertura de estabelecimentos.",
],
"passos": passos(
 "Avaliamos o tipo de ambiente, os materiais das superfícies, a circulação de pessoas e o objetivo da desinfecção.",
 "Escolhemos o desinfetante e o método (pulverização, nebulização ou aplicação manual), considerando compatibilidade com os materiais e tempo de reocupação.",
 "Aplicamos o produto após a limpeza prévia, com atenção às superfícies de alto contato e respeitando o tempo de ação.",
 "Orientamos sobre ventilação, reocupação e rotina de limpeza para manter o ambiente adequado entre as aplicações."),
"seguranca_titulo": "Produtos regularizados na ANVISA e segurança",
"seguranca": """<p>Usamos desinfetantes saneantes com registro ou notificação na ANVISA, dentro da finalidade indicada no rótulo e nas diluições recomendadas. Equipamentos eletrônicos são protegidos ou tratados com produtos compatíveis. Durante a aplicação por nebulização, o ambiente deve estar desocupado; a reocupação acontece após o tempo de ação e a ventilação indicados por escrito.</p>
<p>Pessoas com alergias, asma ou sensibilidade química e animais de estimação devem ficar fora do local durante o serviço. Alimentos, utensílios de cozinha, brinquedos e objetos pessoais devem ser guardados antes da aplicação.</p>""",
"publico": """<p>Atendemos empresas, escritórios, indústrias, centros de distribuição, escolas e creches, academias, clínicas, igrejas, condomínios, residências e frotas de veículos (vans, ônibus e caminhões). Para empresas, oferecemos aplicações programadas com comprovante para cada visita.</p>""",
"garantia": """<p>A sanitização tem efeito imediato sobre os microrganismos presentes nas superfícies tratadas no momento da aplicação, mas não cria uma "proteção permanente": o ambiente volta a ser contaminado com o uso. Por isso, não trabalhamos com promessa de prazo de proteção — indicamos a frequência adequada para cada tipo de local e mantemos a rotina de limpeza como parte do plano.</p>
<p>Ao final, entregamos o <strong>comprovante de execução do serviço</strong>, com data, áreas tratadas, produto utilizado e seu número de registro ou notificação, documento útil para empresas, escolas e condomínios apresentarem a clientes, pais, moradores e órgãos de fiscalização.</p>""",
"faq_titulo": "sanitização",
"faq": [
 ("Qual a diferença entre limpeza, sanitização e desinfecção?", "Limpeza remove a sujeira visível. Desinfecção e sanitização usam produtos para reduzir microrganismos nas superfícies. O ideal é sempre limpar antes de desinfetar."),
 ("Quanto tempo dura o efeito da sanitização?", "O produto age sobre os microrganismos presentes no momento da aplicação. Com o uso do ambiente, ocorre nova contaminação, por isso a frequência deve ser planejada."),
 ("A sanitização danifica eletrônicos e móveis?", "Escolhemos produtos e métodos compatíveis com os materiais e protegemos equipamentos sensíveis."),
 ("Preciso desocupar o ambiente?", "Sim, durante a aplicação e pelo tempo de ação e ventilação indicados. Informamos o prazo por escrito."),
 ("Vocês fazem sanitização em veículos?", "Sim, em carros, vans, ônibus e caminhões, com produtos adequados a estofados e painéis."),
],
"relacionados": ["limpeza-caixa-dagua", "controle-de-pombos", "dedetizacao"],
},
# ---------------------------------------------------------------- 8
{
"slug": "limpeza-caixa-dagua", "garantia_titulo": "Certificado de limpeza e garantia", "nome": "Limpeza e higienização de caixa d'água", "nome_curto": "Limpeza de caixa d'água", "icone": "water",
"resumo": "Esvaziamento, limpeza, desinfecção e vedação de caixas e reservatórios de água.",
"title": "Limpeza de Caixa d'Água em Cajamar | Elbatec",
"desc": "Limpeza e higienização de caixa d'água em Cajamar e região para casas, condomínios e empresas, com desinfecção e comprovante. Agende pelo WhatsApp agora.",
"h1": "Limpeza de Caixa d'Água em Cajamar e Região",
"lead": "Limpeza, desinfecção e inspeção de caixas d'água e reservatórios em residências, condomínios, escolas, restaurantes e empresas, com comprovante de execução.",
"img": "limpeza-caixa-dagua-cajamar.webp", "img_alt": "Caixa d'água aberta e limpa após higienização, com tampa ao lado",
"img_cap": "Reservatório limpo, desinfetado e pronto para ser tampado. (Imagem ilustrativa.)",
"oque": """<p>A caixa d'água acumula, com o tempo, sedimentos, lodo, ferrugem e biofilme no fundo e nas paredes. Se a tampa estiver mal encaixada ou danificada, podem entrar folhas, insetos, pequenos animais e até larvas de mosquito. A água que sai das torneiras passa por esse reservatório, por isso mantê-lo limpo é uma medida simples e importante de saúde.</p>
<p>A recomendação usual é fazer a limpeza da caixa d'água a cada seis meses, ou antes disso se houver obra, falta de água prolongada, água turva, cheiro diferente ou suspeita de contaminação. Em condomínios, escolas, restaurantes e empresas, a limpeza periódica dos reservatórios faz parte das obrigações de manutenção e costuma ser verificada em fiscalizações e auditorias.</p>
<p>O serviço da Elbatec inclui o esvaziamento controlado, a limpeza mecânica das paredes e do fundo, a remoção dos resíduos, a desinfecção com produto adequado para água de consumo, o enxágue e a verificação de tampa, boia e extravasor.</p>""",
"sinais_titulo": "Sinais de que a caixa d'água precisa de limpeza",
"sinais": [
 "Já se passaram mais de seis meses desde a última limpeza (ou você não sabe quando foi feita).",
 "Água com cor amarelada ou turva, gosto ou cheiro diferente.",
 "Partículas, areia ou resíduos saindo das torneiras e entupindo arejadores.",
 "Tampa quebrada, mal encaixada ou ausente.",
 "Obra recente na casa, no prédio ou na rede de abastecimento.",
 "Presença de insetos, larvas ou animais no reservatório.",
],
"passos": passos(
 "Verificamos o tipo, o volume e o acesso ao reservatório, as condições da tampa e da estrutura e a necessidade de interromper o abastecimento.",
 "Combinamos o melhor horário para esvaziar a caixa, orientando para reservar água para uso essencial durante o serviço.",
 "Esvaziamos, limpamos paredes e fundo sem produtos abrasivos que danifiquem o revestimento, removemos resíduos, desinfetamos e enxaguamos antes de reabastecer.",
 "Indicamos eventuais reparos (tampa, boia, trincas) e a data recomendada para a próxima limpeza."),
"seguranca_titulo": "Produtos adequados e segurança da água",
"seguranca": """<p>Na desinfecção usamos produto à base de cloro indicado para tratamento de água de consumo, em concentração e tempo de contato corretos, seguidos de descarte e enxágue antes do reabastecimento. Não usamos sabão, detergente ou produtos que deixem resíduos na água. Todos os produtos têm registro ou notificação na ANVISA.</p>
<p>Durante o serviço, a água da rede interna não deve ser usada para beber ou cozinhar. Após a liberação, orientamos abrir as torneiras para renovar a água das tubulações. Crianças e animais devem ficar longe da área de trabalho, especialmente em lajes e telhados.</p>""",
"publico": """<p>Atendemos casas, sobrados, prédios e condomínios (caixas superiores e cisternas), escolas, creches, restaurantes, hotéis, clínicas, academias, empresas e indústrias. Para reservatórios grandes ou com acesso restrito, o orçamento é feito após vistoria.</p>""",
"garantia": """<p>Após a limpeza, entregamos o <strong>certificado (comprovante) de limpeza e desinfecção do reservatório</strong>, com data, volume aproximado, produto utilizado e data recomendada para a próxima higienização — documento que síndicos, gestores e responsáveis por estabelecimentos usam em fiscalizações e auditorias.</p>
<p>Como a qualidade da água também depende da rede de abastecimento e das condições do reservatório, não prometemos "água garantida" por um período fixo. Se você precisar de análise laboratorial da potabilidade, podemos orientar como contratar um laboratório credenciado. Eventuais garantias específicas são informadas no orçamento.</p>""",
"faq_titulo": "limpeza de caixa d'água",
"faq": [
 ("De quanto em quanto tempo devo limpar a caixa d'água?", "A recomendação mais comum é a cada seis meses, ou antes disso em caso de obra, água turva ou suspeita de contaminação."),
 ("Quanto tempo fico sem água?", "Depende do tamanho do reservatório. Em residências, o serviço costuma levar algumas horas. Informamos a estimativa no orçamento."),
 ("Vocês usam sabão para limpar a caixa?", "Não. Sabão e detergente deixam resíduos. A limpeza é mecânica e a desinfecção é feita com produto adequado para água de consumo."),
 ("Vocês limpam cisternas de condomínio?", "Sim, caixas superiores e cisternas, com planejamento para reduzir o tempo sem abastecimento dos moradores."),
 ("O certificado serve para a vigilância sanitária?", "O comprovante registra a data, o produto utilizado e o responsável pela execução, e costuma ser solicitado em fiscalizações de estabelecimentos."),
],
"relacionados": ["limpeza-de-fossa-e-desentupimento", "sanitizacao", "desinsetizacao"],
},
# ---------------------------------------------------------------- 9
{
"slug": "limpeza-de-fossa-e-desentupimento", "oque_titulo": "O que inclui a limpeza de fossa, caixa de gordura e o desentupimento", "nome": "Limpeza de fossa, caixa de gordura e desentupimento", "nome_curto": "Limpa fossa e desentupimento", "icone": "pipe",
"resumo": "Limpeza de fossa e caixa de gordura e desentupimento de pias, ralos, vasos e redes de esgoto.",
"title": "Limpa Fossa e Desentupidora em Cajamar | Elbatec",
"desc": "Limpeza de fossa, caixa de gordura e desentupimento em Cajamar e região para casas, condomínios, restaurantes e empresas. Chame a Elbatec no WhatsApp.",
"h1": "Limpa Fossa e Desentupidora em Cajamar e Região",
"lead": "Limpeza de fossa séptica, caixa de gordura e caixas de passagem, e desentupimento de pias, ralos, vasos sanitários e redes de esgoto em residências, condomínios e empresas.",
"img": "limpeza-de-fossa-desentupimento-cajamar.webp", "img_alt": "Equipamento de desentupimento em caixa de inspeção de esgoto",
"img_cap": "Desentupimento e limpeza de caixas de inspeção e de gordura. (Imagem ilustrativa.)",
"artigo_lower": True,
"oque": """<p>Fossas sépticas, caixas de gordura e redes de esgoto precisam de manutenção periódica. Com o uso, a fossa acumula lodo, e a caixa de gordura retém óleos e restos de alimentos que endurecem e formam crostas. Quando a limpeza atrasa, surgem mau cheiro, retorno de esgoto, entupimentos e atração de baratas, ratos e moscas — o que conecta diretamente este serviço ao controle de pragas.</p>
<p>Em Cajamar e em bairros de cidades vizinhas onde parte dos imóveis ainda usa fossa séptica, a limpeza deve seguir uma rotina definida pelo tamanho da fossa e pelo número de moradores. Já a caixa de gordura precisa de limpeza mais frequente, sobretudo em restaurantes, padarias, cozinhas industriais e refeitórios de empresas.</p>
<p>Também realizamos o <strong>desentupimento</strong> de pias, ralos, tanques, vasos sanitários, colunas e ramais de esgoto, usando equipamentos adequados a cada situação, sem quebrar pisos sempre que possível. <!-- CONFIRMAR: tipos de equipamento disponíveis (caminhão limpa-fossa próprio ou parceiro, hidrojateamento, máquina de cabo rotativo). --></p>""",
"sinais_titulo": "Sinais de fossa cheia, caixa de gordura saturada ou entupimento",
"sinais": [
 "Mau cheiro de esgoto em ralos, quintal ou perto da fossa.",
 "Água descendo devagar em pias, ralos e vasos.",
 "Retorno de esgoto ou gordura pelos ralos e pela caixa de inspeção.",
 "Barulho de borbulhamento nos ralos ao dar descarga.",
 "Gramado excessivamente úmido ou afundado perto da fossa.",
 "Presença de baratas, moscas e ratos próximos às caixas de esgoto e gordura.",
],
"passos": passos(
 "Localizamos fossa, caixas e pontos de entupimento e avaliamos o acesso para equipamentos e veículo.",
 "Identificamos a causa (gordura, objetos, raízes, lodo) e definimos o método de limpeza ou desentupimento.",
 "Executamos a sucção, a limpeza ou o desentupimento, com cuidado para não danificar a tubulação, e destinamos os resíduos a locais licenciados.",
 "Orientamos sobre uso correto das pias e vasos e indicamos a periodicidade ideal de limpeza para o seu imóvel."),
"seguranca_titulo": "Segurança, higiene e destinação correta",
"seguranca": """<p>Fossas e redes de esgoto podem acumular gases tóxicos e contaminação biológica. Nossa equipe trabalha com equipamentos de proteção e não entra em espaços confinados sem os procedimentos de segurança necessários. Moradores, crianças e animais devem ficar afastados das caixas abertas durante o serviço.</p>
<p>Os resíduos retirados de fossas e caixas de gordura devem ser transportados e destinados a locais licenciados para recebê-los. Após o serviço, se necessário, aplicamos desinfetante saneante regularizado na ANVISA nas áreas externas afetadas e podemos complementar com dedetização de caixas para controle de baratas. <!-- PREENCHER: licenças ambientais / transportador de resíduos, se houver. --></p>""",
"publico": """<p>Atendemos casas, chácaras, condomínios, restaurantes, padarias, lanchonetes, cozinhas industriais, escolas, refeitórios de empresas, indústrias e galpões. Para estabelecimentos de alimentação, recomendamos combinar a limpeza periódica da caixa de gordura com o programa de <a href="@/servicos/dedetizacao.html">dedetização</a> e <a href="@/servicos/desratizacao.html">desratização</a>.</p>""",
"garantia": garantia("limpeza de fossa, caixa de gordura ou desentupimento").replace("se a praga tratada voltar a aparecer nas áreas atendidas", "se o mesmo ponto voltar a apresentar problema em condições normais de uso"),
"faq_titulo": "limpa fossa e desentupimento",
"faq": [
 ("De quanto em quanto tempo limpar a fossa?", "Depende do volume da fossa e do número de usuários. Em residências, é comum entre um e dois anos; na vistoria indicamos a frequência adequada."),
 ("E a caixa de gordura?", "Em residências, costuma ser limpa a cada poucos meses. Em restaurantes e cozinhas industriais, a frequência é bem maior, às vezes mensal ou quinzenal."),
 ("Vocês quebram o piso para desentupir?", "Sempre tentamos resolver sem quebra, usando equipamentos próprios para cada caso. A quebra só é indicada quando não há outra alternativa e com sua autorização."),
 ("Posso jogar óleo de cozinha na pia?", "Não. O óleo solidifica na tubulação e na caixa de gordura. Guarde-o em garrafa e leve a um ponto de coleta."),
 ("Para onde vai o resíduo da fossa?", "Os resíduos devem ser destinados a locais licenciados para recebimento e tratamento."),
],
"relacionados": ["limpeza-caixa-dagua", "desratizacao", "dedetizacao"],
},
# ---------------------------------------------------------------- 10
{
"slug": "venda-de-produtos-saneantes", "oque_titulo": "O que são produtos saneantes e quando comprar", "garantia_titulo": "Garantia, nota fiscal e documentação", "nome": "Venda de produtos saneantes", "nome_curto": "Produtos saneantes", "icone": "flask",
"resumo": "Venda de saneantes domissanitários regularizados, com orientação de uso seguro.",
"title": "Produtos Saneantes em Cajamar | Venda e Orientação",
"desc": "Venda de produtos saneantes domissanitários em Cajamar: desinfetantes, inseticidas e itens de limpeza regularizados na ANVISA, com orientação. Consulte.",
"h1": "Venda de Produtos Saneantes em Cajamar",
"lead": "Saneantes domissanitários regularizados na ANVISA — desinfetantes, produtos de limpeza e inseticidas de venda livre — com orientação técnica para uso correto e seguro.",
"img": "produtos-saneantes-cajamar.webp", "img_alt": "Embalagens de produtos de limpeza e desinfetantes organizadas em prateleira",
"img_cap": "Produtos saneantes regularizados para uso doméstico e institucional. (Imagem ilustrativa.)",
"oque": """<p>Saneantes domissanitários são produtos destinados à higienização, desinfecção e desinfestação de ambientes: desinfetantes, detergentes, alvejantes, limpadores, inseticidas e raticidas de venda livre, entre outros. No Brasil, eles são regulados pela ANVISA e só podem ser comercializados com registro ou notificação, rótulo em português e informações de uso e segurança.</p>
<p>Além de prestar serviços, a Elbatec comercializa saneantes para quem precisa manter a rotina de limpeza e prevenção entre uma visita técnica e outra: condomínios, empresas, escolas, restaurantes e residências. Nosso diferencial é a <strong>orientação</strong>: indicamos o produto certo para cada superfície e finalidade, a diluição correta e os cuidados de armazenamento.</p>
<p>Importante: produtos de uso exclusivamente profissional (como muitos inseticidas e raticidas usados nos nossos serviços) têm venda restrita a empresas especializadas e não são vendidos ao consumidor final. Para esses casos, oferecemos o serviço aplicado por nossa equipe. Veja a <a href="@/produtos-saneantes.html">página de produtos saneantes</a> para conhecer as categorias disponíveis.</p>""",
"sinais_titulo": "Quando comprar saneantes com orientação técnica",
"sinais": [
 "Condomínios e empresas que precisam padronizar produtos de limpeza e desinfecção.",
 "Restaurantes e cozinhas que precisam de desinfetantes adequados para superfícies que entram em contato com alimentos.",
 "Quem quer manter a prevenção entre os serviços de dedetização.",
 "Dúvidas sobre diluição, mistura de produtos ou compatibilidade com superfícies.",
 "Necessidade de fichas técnicas e de segurança dos produtos para documentação interna.",
 "Compras recorrentes com entrega programada (consulte disponibilidade).",
],
"passos": [
 ("Contato", "Você nos conta o tipo de ambiente, a finalidade e o volume necessário, pelo WhatsApp, telefone ou formulário."),
 ("Indicação", "Indicamos os produtos adequados, apresentando as opções disponíveis e as informações de rótulo."),
 ("Orçamento", "Enviamos o orçamento com valores, quantidades, forma de pagamento e prazo de retirada ou entrega."),
 ("Orientação de uso", "Explicamos diluição, aplicação, tempo de ação, armazenamento e descarte de embalagens."),
 ("Documentação", "Quando necessário, fornecemos ficha técnica e ficha de informações de segurança dos produtos."),
],
"seguranca_titulo": "Produtos regularizados na ANVISA e cuidados com crianças e pets",
"seguranca": """<p>Comercializamos apenas saneantes com registro ou notificação na ANVISA, em embalagens originais e com rótulo completo. Recomendamos sempre: ler o rótulo antes de usar, nunca misturar produtos (por exemplo, cloro com amoníaco ou com ácidos, que liberam gases tóxicos), não reaproveitar embalagens para outros fins e guardar tudo em local alto, ventilado e trancado, longe de crianças e de animais.</p>
<p>Em caso de ingestão ou contato acidental, siga as instruções do rótulo e procure atendimento médico levando a embalagem do produto. Para dúvidas sobre intoxicação, o Disque-Intoxicação da ANVISA atende pelo 0800 722 6001.</p>""",
"publico": """<p>Atendemos residências, condomínios, empresas, escolas, igrejas, academias, restaurantes, comércios e indústrias de Cajamar e região. <!-- PREENCHER: informar se há loja/retirada no endereço, entrega e pedido mínimo. --></p>""",
"garantia": """<p>Os produtos são vendidos lacrados, dentro do prazo de validade e com nota fiscal. Trocas e devoluções seguem o Código de Defesa do Consumidor e as condições informadas no orçamento. <!-- PREENCHER: política de troca/devolução. --></p>
<p>Clientes de serviços da Elbatec recebem, junto com o <strong>comprovante de execução</strong>, a indicação dos produtos de uso doméstico que podem ajudar na manutenção do ambiente tratado, sem interferir no resultado do serviço.</p>""",
"faq_titulo": "produtos saneantes",
"faq": [
 ("Vocês vendem o mesmo veneno usado na dedetização?", "Produtos de uso profissional têm venda restrita a empresas especializadas. Para esses casos, oferecemos o serviço aplicado por nossa equipe."),
 ("Os produtos são registrados na ANVISA?", "Sim. Comercializamos apenas saneantes com registro ou notificação na ANVISA."),
 ("Posso misturar desinfetante com água sanitária?", "Não é recomendado misturar produtos. Algumas combinações liberam gases tóxicos. Use cada produto separadamente, conforme o rótulo."),
 ("Vocês fornecem ficha técnica dos produtos?", "Sim, quando disponível do fabricante, fornecemos ficha técnica e ficha de informações de segurança."),
 ("Fazem entrega?", "Consulte pelo WhatsApp as condições de retirada e entrega para sua região."),
],
"relacionados": ["sanitizacao", "dedetizacao", "limpeza-caixa-dagua"],
"cta_local": "Cajamar",
},
]

# A página de "Venda de produtos saneantes" é publicada como /produtos-saneantes.html
# (ver content_paginas.py). As 9 páginas de serviço ficam em /servicos/.
PRODUTOS = SERVICOS.pop()  # remove da lista de /servicos/ e guarda para a página própria
