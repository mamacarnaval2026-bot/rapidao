# -*- coding: utf-8 -*-
"""Conteúdo das páginas de categoria da Tango Fantasias.
Textos originais. CONFIRME modelos, tamanhos, pedido mínimo e prazos antes de publicar.
Não cite nem use imagens de personagens licenciados (Disney, Marvel etc.) sem autorização dos detentores."""


def passos(escolha, producao):
    return [
        ("Escolha", escolha),
        ("Orçamento", "Envie pelo WhatsApp ou pelo formulário os modelos, tamanhos e quantidades. Para lojistas, informe CNPJ e cidade de entrega."),
        ("Confirmação", "Enviamos valores, disponibilidade, prazo e formas de pagamento. O pedido é confirmado por escrito."),
        ("Separação ou produção", producao),
        ("Retirada ou envio", "Retire na fábrica, no Brás, ou combine o envio para sua cidade. <!-- CONFIRMAR: modalidades de envio (Correios, transportadora, excursões) -->"),
    ]


CONDICOES = ("<p>Trabalhamos com venda no <strong>atacado</strong> (para lojistas e revendedores) e no <strong>varejo</strong> (consumidor final). "
             "Grade de tamanhos, pedido mínimo, preços e prazos variam conforme o modelo e a época do ano e são informados no orçamento. "
             "Em datas de alta procura, como Carnaval, Halloween e festas juninas, a produção é planejada com antecedência: quanto antes o pedido, maior a disponibilidade.</p>")

QUALIDADE_PADRAO = ("<p>Como somos a própria confecção, acompanhamos cada etapa: escolha de tecidos, modelagem, corte, costura e acabamento. "
                    "Isso permite manter o padrão entre lotes, repor modelos com mais facilidade e ajustar cores e detalhes em pedidos maiores. "
                    "As peças levam etiqueta com composição do tecido e instruções de conservação. <!-- CONFIRMAR: etiquetagem e tecidos utilizados --></p>")

CATEGORIAS = [
# -------------------------------------------------------------- 1
{
"slug": "fantasias-infantis", "nome": "Fantasias infantis", "nome_curto": "Fantasias infantis", "icone": "child",
"resumo": "Fantasias para meninas e meninos, do bebê à pré-adolescência, para festas, escola e Carnaval.",
"title": "Fantasias Infantis no Atacado | Brás SP | Tango",
"desc": "Fantasias infantis no atacado e varejo, direto da fábrica no Brás, SP. Modelos para festas, escola e Carnaval, em vários tamanhos. Peça orçamento no WhatsApp.",
"h1": "Fantasias Infantis no Atacado e Varejo",
"lead": "Fantasias para meninas e meninos, fabricadas no Brás, em São Paulo, para lojas, revendedores, escolas e famílias que querem uma festa caprichada.",
"img": "fantasias-infantis-atacado.webp", "img_alt": "Fantasias infantis coloridas penduradas em cabides na fábrica da Tango Fantasias no Brás",
"img_cap": "Imagem ilustrativa — substitua por fotos reais das fantasias infantis.",
"oque_titulo": "Fantasias infantis direto da fábrica",
"oque": """<p>A fantasia infantil é a categoria que mais gira durante o ano: aniversários, festas temáticas, dias de fantasia na escola, Carnaval, Halloween e festa junina. Para quem revende, ter uma boa variedade de modelos e tamanhos é o que faz o cliente voltar. Para as famílias, o que importa é conforto, durabilidade e aquele acabamento que aparece bem nas fotos.</p>
<p>Na Tango Fantasias, as peças infantis são produzidas na nossa própria confecção, no Brás. Trabalhamos temas clássicos e atemporais — princesas e reis, bailarinas, fadas, super-heróis com visual próprio, animais, profissões, piratas, palhaços, personagens de contos e figuras históricas — além de lançamentos sazonais. <!-- CONFIRMAR: lista real de modelos e linhas infantis --></p>
<p>Por ser fábrica, conseguimos atender desde a compra de uma única peça no varejo até grades completas para lojas, com reposição de modelos e opção de produção para grupos, como turmas de escola e apresentações de dança.</p>""",
"destaques_titulo": "Destaques da linha infantil",
"destaques": [
 "Modelos de temas clássicos e sazonais, com cores vivas e acabamento caprichado.",
 "Tamanhos do infantil ao juvenil, em grade para revenda. <!-- CONFIRMAR grade -->",
 "Tecidos escolhidos para conforto da criança durante festas e apresentações.",
 "Fechamentos práticos para vestir e tirar com facilidade.",
 "Opção de kits com acessórios (tiaras, capas, saias, chapéus).",
 "Reposição de modelos de linha para lojistas.",
],
"passos": passos("Escolha os modelos pelo catálogo, pelo WhatsApp ou visitando a fábrica no Brás.",
                 "Separamos as peças do estoque ou programamos a produção, conforme a quantidade e o modelo."),
"qualidade_titulo": "Conforto, acabamento e segurança para as crianças",
"qualidade": QUALIDADE_PADRAO + """<p>Nas peças infantis, damos atenção especial a costuras internas sem rebarbas, elásticos confortáveis e aviamentos bem fixados. Recomendamos sempre que crianças pequenas usem fantasias com a supervisão de um adulto, que peças com pequenos enfeites não sejam usadas por bebês e que a fantasia seja mantida longe de velas e fontes de calor. <!-- CONFIRMAR: certificações/ensaios aplicáveis, se houver --></p>""",
"publico": """<p>Vendemos para lojas de fantasias, lojas de festas e de presentes, revendedores e sacoleiros, buffets infantis, escolas, grupos de dança e para famílias que compram direto da fábrica. Lojistas têm condições especiais na página de <a href="@/atacado.html">atacado</a>.</p>""",
"condicoes": CONDICOES + """<p>Na dúvida sobre o tamanho, veja o nosso guia <a href="@/blog/como-escolher-o-tamanho-da-fantasia-infantil.html">como escolher o tamanho da fantasia infantil</a>.</p>""",
"faq_titulo": "fantasias infantis",
"faq": [
 ("Vocês vendem fantasia infantil no varejo ou só no atacado?", "Atendemos os dois. Você pode comprar uma peça no varejo ou grades completas para revenda no atacado."),
 ("Quais tamanhos vocês trabalham?", "Trabalhamos tamanhos do infantil ao juvenil. A grade exata de cada modelo é informada no orçamento."),
 ("Vocês fazem fantasias iguais para uma turma da escola?", "Sim. Fazemos pedidos para turmas e grupos, com prazo combinado conforme a quantidade e a data do evento."),
 ("As fantasias vêm com acessórios?", "Alguns modelos acompanham acessórios e outros podem ser montados em kit. Consulte as opções de cada modelo."),
 ("Vocês têm fantasias de personagens de desenho?", "Trabalhamos modelos com criação própria e temas clássicos. Personagens de marcas registradas dependem de licença dos detentores dos direitos."),
],
"relacionados": ["fantasias-de-carnaval", "fantasias-para-escolas-e-apresentacoes", "acessorios-para-fantasias"],
},
# -------------------------------------------------------------- 2
{
"slug": "fantasias-adultas", "nome": "Fantasias adultas", "nome_curto": "Fantasias adultas", "icone": "mask",
"resumo": "Fantasias femininas e masculinas para festas, Carnaval, Halloween e eventos temáticos.",
"title": "Fantasias Adultas no Atacado | Brás SP | Tango",
"desc": "Fantasias adultas femininas e masculinas no atacado e varejo, fabricadas no Brás, São Paulo. Para Carnaval, Halloween e festas temáticas. Peça seu orçamento.",
"h1": "Fantasias Adultas no Atacado e Varejo",
"lead": "Fantasias femininas, masculinas e unissex para Carnaval, Halloween, festas temáticas, eventos corporativos e ensaios fotográficos, direto da fábrica no Brás.",
"img": "fantasias-adultas-atacado.webp", "img_alt": "Arara com fantasias adultas femininas e masculinas em tons vibrantes",
"img_cap": "Imagem ilustrativa — substitua por fotos reais das fantasias adultas.",
"oque_titulo": "Fantasias adultas para todas as festas",
"oque": """<p>O público adulto busca fantasias que vistam bem, sejam confortáveis para passar horas na festa e tenham personalidade. Por isso, a linha adulta da Tango Fantasias combina modelagem pensada para diferentes corpos, tecidos com bom caimento e detalhes que fazem diferença nas fotos: brilho na medida, cores intensas e acabamento cuidadoso.</p>
<p>Produzimos temas clássicos e muito procurados — anos 60, 70 e 80, piratas, marinheiros, cowboys, ciganas, havaianas, melindrosas, gangsters, personagens históricos, profissões, animais e figuras de contos — além de modelos para Halloween e Carnaval. <!-- CONFIRMAR: lista real de modelos adultos --></p>
<p>As fantasias adultas também são muito usadas em festas de empresa, confraternizações, despedidas de solteiro, eventos promocionais e produções de fotos e vídeos. Para esses casos, atendemos pedidos em quantidade com modelos padronizados.</p>""",
"destaques_titulo": "Destaques da linha adulta",
"destaques": [
 "Modelos femininos, masculinos e unissex.",
 "Tamanhos variados, com opções plus size. <!-- CONFIRMAR -->",
 "Temas clássicos, retrô, históricos, profissões e sazonais.",
 "Tecidos com bom caimento e conforto para uso prolongado.",
 "Combinações com acessórios para completar o visual.",
 "Pedidos padronizados para grupos, eventos e empresas.",
],
"passos": passos("Escolha os modelos e tamanhos pelo WhatsApp ou venha conhecer a fábrica no Brás.",
                 "Separamos do estoque ou produzimos o lote, conforme o modelo e a quantidade."),
"qualidade_titulo": "Modelagem, tecidos e acabamento",
"qualidade": QUALIDADE_PADRAO + """<p>Na linha adulta, a modelagem é o ponto principal: ajustes com elástico e amarrações ajudam a fantasia a vestir bem em mais tipos de corpo, e as costuras reforçadas aguentam dança e movimento. Recomendamos conferir as medidas antes da compra e seguir as instruções de lavagem da etiqueta para conservar cores e brilhos.</p>""",
"publico": """<p>Atendemos lojas de fantasias e de festas, locadoras de fantasias, revendedores, produtoras de eventos, agências de promoção, grupos e o consumidor final. Para revenda, veja as condições de <a href="@/atacado.html">atacado para lojistas</a>.</p>""",
"condicoes": CONDICOES,
"faq_titulo": "fantasias adultas",
"faq": [
 ("Vocês têm fantasias plus size?", "Trabalhamos modelos em diferentes tamanhos. Consulte pelo WhatsApp a grade disponível para o modelo que você procura."),
 ("Posso comprar só uma fantasia?", "Sim, vendemos no varejo. Para quantidades maiores, há condições de atacado."),
 ("Fazem fantasias iguais para um grupo?", "Sim, produzimos lotes padronizados para grupos, festas de empresa e eventos, com prazo combinado."),
 ("Locadoras podem comprar no atacado?", "Sim. Atendemos locadoras e lojas com CNPJ nas condições de atacado."),
 ("Como lavar a fantasia?", "Siga a etiqueta. Em geral, lavagem à mão, com água fria e secagem à sombra conservam melhor tecidos com brilho e aplicações."),
],
"relacionados": ["fantasias-de-carnaval", "fantasias-de-halloween", "acessorios-para-fantasias"],
},
# -------------------------------------------------------------- 3
{
"slug": "fantasias-de-carnaval", "nome": "Fantasias de Carnaval", "nome_curto": "Fantasias de Carnaval", "icone": "confetti",
"resumo": "Fantasias para foliões, blocos de rua, bailes e escolas de samba, no atacado e no varejo.",
"title": "Fantasias de Carnaval no Atacado | Brás SP | Tango",
"desc": "Fantasias de Carnaval no atacado e varejo, direto da fábrica no Brás, São Paulo. Para lojas, blocos, bailes e foliões. Garanta seu estoque: peça orçamento.",
"h1": "Fantasias de Carnaval no Atacado e Varejo",
"lead": "Fantasias para blocos de rua, bailes, matinês e foliões de todas as idades — com produção própria no Brás para lojistas abastecerem o estoque da temporada.",
"img": "fantasias-de-carnaval-atacado.webp", "img_alt": "Fantasias de Carnaval com cores vibrantes, brilhos e confetes",
"img_cap": "Imagem ilustrativa — substitua por fotos reais da coleção de Carnaval.",
"oque_titulo": "Carnaval é a nossa alta temporada",
"oque": """<p>O Carnaval é o período de maior procura por fantasias no Brasil, e quem revende sabe: o estoque precisa estar pronto antes da corrida às lojas. Na Tango Fantasias, a coleção de Carnaval é planejada com antecedência para que lojistas, revendedores e blocos consigam fazer seus pedidos com tranquilidade.</p>
<p>A linha inclui fantasias completas e peças para montar o visual — saias, bodies, coletes, capas, macacões e acessórios —, em temas que sempre fazem sucesso nos blocos: marinheiros, havaianas, ciganas, sereias, piratas, animais, frutas, profissões, anos 80 e muito brilho. <!-- CONFIRMAR: modelos da coleção atual --></p>
<p>Também atendemos <strong>blocos de rua, cordões e grupos</strong> que querem sair com fantasias iguais ou em cores combinadas. Nesses casos, o ideal é falar com a gente com bastante antecedência para garantir tecido, cores e prazo de produção. Lojistas podem conferir dicas no artigo <a href="@/blog/como-montar-estoque-de-fantasias-para-o-carnaval.html">como montar estoque de fantasias para o Carnaval</a>.</p>""",
"destaques_titulo": "Destaques da coleção de Carnaval",
"destaques": [
 "Fantasias infantis e adultas para blocos, bailes e matinês.",
 "Peças avulsas para montar o visual: saias, capas, coletes e bodies.",
 "Cores vibrantes, brilhos e acabamentos que aparecem nas fotos.",
 "Produção de lotes padronizados para blocos e grupos.",
 "Planejamento de pedidos antecipados para lojistas.",
 "Acessórios para completar: tiaras, chapéus, leques e asas.",
],
"passos": passos("Escolha os modelos da coleção ou envie a referência do seu bloco ou grupo.",
                 "Separamos do estoque ou produzimos o lote. Para blocos, confirmamos cores e amostra antes da produção. <!-- CONFIRMAR se há amostra -->"),
"qualidade_titulo": "Feitas para aguentar a folia",
"qualidade": QUALIDADE_PADRAO + """<p>Fantasias de Carnaval enfrentam calor, sol, chuva e muitas horas de dança. Por isso, priorizamos costuras firmes, tecidos leves e modelos que permitem movimento. Para conservar brilhos e aplicações, recomendamos lavar à mão, sem torcer, e secar à sombra.</p>""",
"publico": """<p>Lojas de fantasias e de artigos de festa, revendedores e sacoleiros, blocos de rua, cordões, escolas de samba (alas e comunidade), clubes e organizadores de bailes, buffets e o folião que quer comprar direto da fábrica. Veja também as <a href="@/atacado.html">condições de atacado</a>.</p>""",
"condicoes": CONDICOES + "<p><strong>Dica para lojistas:</strong> antecipe o pedido da coleção de Carnaval para garantir os modelos mais procurados e a grade completa de tamanhos.</p>",
"faq_titulo": "fantasias de Carnaval",
"faq": [
 ("Com quanta antecedência devo fazer o pedido de Carnaval?", "Quanto antes, melhor. Para lojistas e blocos, recomendamos fazer o pedido com meses de antecedência para garantir modelos, cores e prazo."),
 ("Vocês fazem fantasias para blocos de rua?", "Sim. Produzimos lotes padronizados ou em cores combinadas para blocos, cordões e grupos."),
 ("Fazem fantasias para escolas de samba?", "Atendemos pedidos de alas e grupos, conforme o modelo e a quantidade. Envie a referência para avaliarmos."),
 ("Posso comprar fantasia de Carnaval no varejo?", "Sim. Vendemos para o consumidor final, diretamente na fábrica ou com envio combinado."),
 ("Vocês enviam para outros estados?", "Consulte pelo WhatsApp as opções de envio para a sua cidade."),
],
"relacionados": ["fantasias-adultas", "fantasias-infantis", "acessorios-para-fantasias"],
},
# -------------------------------------------------------------- 4
{
"slug": "fantasias-de-halloween", "nome": "Fantasias de Halloween", "nome_curto": "Fantasias de Halloween", "icone": "pumpkin",
"resumo": "Bruxas, vampiros, caveiras e outros temas para festas de Halloween, escolas e eventos.",
"title": "Fantasias de Halloween no Atacado | Brás SP | Tango",
"desc": "Fantasias de Halloween infantis e adultas no atacado e varejo: bruxas, vampiros, caveiras e mais. Direto da fábrica no Brás, São Paulo. Peça orçamento.",
"h1": "Fantasias de Halloween no Atacado e Varejo",
"lead": "Fantasias infantis e adultas para o Dia das Bruxas: festas, escolas de idiomas, eventos, baladas e lojas que querem aproveitar a temporada de outubro.",
"img": "fantasias-de-halloween-atacado.webp", "img_alt": "Fantasias de Halloween em tons de preto, roxo e laranja com chapéu de bruxa",
"img_cap": "Imagem ilustrativa — substitua por fotos reais da linha de Halloween.",
"oque_titulo": "Halloween: uma temporada que cresce a cada ano",
"oque": """<p>O Halloween ganhou espaço no calendário brasileiro: escolas, cursos de idiomas, condomínios, buffets, bares e empresas promovem festas temáticas em outubro, e a procura por fantasias aumenta bastante nas semanas anteriores. Para o lojista, é uma segunda alta temporada que ajuda a girar o estoque fora do Carnaval.</p>
<p>A linha de Halloween da Tango Fantasias reúne os temas mais procurados: bruxas e feiticeiros, vampiros, caveiras, múmias, fantasmas, abóboras, gatos pretos, morcegos, esqueletos e figuras do terror clássico, em versões infantis — divertidas, sem exagero — e adultas. <!-- CONFIRMAR: modelos disponíveis --></p>
<p>Além das fantasias completas, trabalhamos peças e acessórios que ajudam a montar o visual com custo menor, como capas, chapéus, saias e tiaras, muito procurados para festas escolares.</p>""",
"destaques_titulo": "Destaques da linha de Halloween",
"destaques": [
 "Modelos infantis com visual divertido, adequado para escolas.",
 "Modelos adultos para festas, baladas e eventos.",
 "Capas, chapéus, saias e tiaras para montar o visual.",
 "Paleta clássica: preto, roxo, laranja e verde.",
 "Kits para festas escolares e cursos de idiomas.",
 "Pedidos antecipados para lojistas montarem o estoque de outubro.",
],
"passos": passos("Escolha os modelos de Halloween pelo WhatsApp ou na fábrica.",
                 "Separamos do estoque ou programamos a produção para chegar antes das festas de outubro."),
"qualidade_titulo": "Qualidade e cuidados",
"qualidade": QUALIDADE_PADRAO + """<p>Fantasias de Halloween costumam ser usadas em ambientes decorados com velas e luzes. Oriente seus clientes a manter as peças longe de chamas e fontes de calor e a supervisionar sempre as crianças.</p>""",
"publico": """<p>Lojas de fantasias e de festas, papelarias e lojas de presentes, revendedores, escolas e cursos de idiomas, buffets, casas noturnas, produtoras de eventos e o consumidor final. Lojistas podem conferir as <a href="@/atacado.html">condições de atacado</a>.</p>""",
"condicoes": CONDICOES,
"faq_titulo": "fantasias de Halloween",
"faq": [
 ("Quando devo comprar as fantasias de Halloween para revenda?", "O ideal é fechar o pedido com antecedência, para ter o estoque na loja no início de outubro."),
 ("Vocês têm fantasias de Halloween para crianças?", "Sim, com visual divertido e adequado para festas escolares."),
 ("Fazem kits para escolas de idiomas?", "Sim. Montamos pedidos em quantidade com modelos e tamanhos variados."),
 ("Vendem capa e chapéu de bruxa separados?", "Sim, trabalhamos peças avulsas e acessórios para montar o visual."),
 ("Posso comprar no varejo?", "Sim. Atendemos consumidor final e lojistas."),
],
"relacionados": ["fantasias-adultas", "fantasias-infantis", "acessorios-para-fantasias"],
},
# -------------------------------------------------------------- 5
{
"slug": "fantasias-de-festa-junina", "nome": "Fantasias de festa junina", "nome_curto": "Roupas de festa junina", "icone": "flag",
"resumo": "Vestidos de caipira, camisas xadrez, trajes de quadrilha e acessórios para arraiás.",
"title": "Roupa de Festa Junina no Atacado | Brás SP | Tango",
"desc": "Roupas de festa junina no atacado e varejo: vestidos caipiras, camisas xadrez e trajes de quadrilha infantis e adultos, direto da fábrica no Brás. Orçamento já.",
"h1": "Roupas de Festa Junina no Atacado e Varejo",
"lead": "Vestidos caipiras, camisas xadrez, trajes de quadrilha e acessórios para arraiás de escolas, empresas, condomínios e quadrilhas juninas.",
"img": "roupas-festa-junina-atacado.webp", "img_alt": "Vestidos caipiras floridos e camisas xadrez para festa junina com bandeirinhas",
"img_cap": "Imagem ilustrativa — substitua por fotos reais da linha junina.",
"oque_titulo": "Tudo para o arraiá, do infantil ao adulto",
"oque": """<p>As festas juninas e julinas movimentam escolas, igrejas, empresas, condomínios e clubes em todo o país, e a roupa caipira é presença obrigatória. É uma das temporadas mais fortes para lojas de fantasias e de artigos de festa, com grande procura por tamanhos infantis — muitas vezes em quantidade, para turmas inteiras.</p>
<p>A Tango Fantasias produz vestidos caipiras com babados, rendas e estampas floridas e xadrez, camisas xadrez, macacões e jardineiras, coletes, saias e trajes completos para quadrilhas. Para completar, trabalhamos acessórios como chapéus de palha, lenços e laços. <!-- CONFIRMAR: modelos e acessórios disponíveis --></p>
<p>Quadrilhas e escolas que precisam de figurinos padronizados podem encomendar lotes com cores e estampas combinadas, desde que o pedido seja feito com antecedência para garantir tecido e prazo.</p>""",
"destaques_titulo": "Destaques da linha junina",
"destaques": [
 "Vestidos caipiras infantis e adultos com babados e estampas floridas ou xadrez.",
 "Camisas xadrez, coletes, jardineiras e macacões.",
 "Trajes padronizados para quadrilhas e apresentações escolares.",
 "Acessórios: chapéus, lenços, laços e tiaras.",
 "Grades de tamanhos para turmas e revenda.",
 "Planejamento de pedidos para a temporada de junho e julho.",
],
"passos": passos("Escolha os modelos ou envie a referência do figurino da sua quadrilha ou escola.",
                 "Separamos do estoque ou produzimos o lote com as cores e estampas combinadas."),
"qualidade_titulo": "Conforto para dançar a quadrilha",
"qualidade": QUALIDADE_PADRAO + """<p>Os trajes juninos precisam permitir que a criança e o adulto dancem à vontade. Usamos modelagens com folga nos movimentos e acabamentos que resistem a várias festas na mesma temporada. Mantenha as roupas longe de fogueiras e fogos de artifício.</p>""",
"publico": """<p>Lojas de fantasias e de festas, armarinhos, revendedores, escolas, creches, quadrilhas juninas, igrejas, empresas, condomínios e famílias. Para revenda, confira as <a href="@/atacado.html">condições de atacado</a>.</p>""",
"condicoes": CONDICOES,
"faq_titulo": "roupas de festa junina",
"faq": [
 ("Vocês fazem roupa caipira para turmas de escola?", "Sim. Atendemos pedidos em quantidade com tamanhos variados para turmas e apresentações."),
 ("Fazem figurino para quadrilha junina?", "Sim, com cores e estampas combinadas. Faça o pedido com antecedência para garantirmos tecido e prazo."),
 ("Têm vestido caipira adulto?", "Sim, temos linha infantil e adulta."),
 ("Vendem chapéu de palha e acessórios?", "Trabalhamos acessórios juninos. Consulte a disponibilidade pelo WhatsApp."),
 ("Quando começa a venda da linha junina?", "Lojistas costumam fechar pedidos antes de maio. Fale conosco para planejar o seu."),
],
"relacionados": ["fantasias-infantis", "fantasias-para-escolas-e-apresentacoes", "acessorios-para-fantasias"],
},
# -------------------------------------------------------------- 6
{
"slug": "fantasias-para-escolas-e-apresentacoes", "nome": "Fantasias para escolas e apresentações", "nome_curto": "Escolas e apresentações", "icone": "theater",
"resumo": "Figurinos para peças, datas comemorativas, dança, formaturas infantis e eventos escolares.",
"title": "Figurinos para Escolas e Apresentações | Tango",
"desc": "Figurinos e fantasias para escolas, peças de teatro, dança e datas comemorativas. Pedidos em quantidade, direto da fábrica no Brás, São Paulo. Fale conosco.",
"h1": "Fantasias e Figurinos para Escolas e Apresentações",
"lead": "Figurinos para peças de teatro, apresentações de dança, datas comemorativas, folclore, formaturas infantis e eventos escolares, em pedidos para turmas inteiras.",
"img": "figurinos-escolas-apresentacoes.webp", "img_alt": "Figurinos coloridos organizados para apresentação escolar de dança e teatro",
"img_cap": "Imagem ilustrativa — substitua por fotos reais de figurinos produzidos.",
"oque_titulo": "Figurinos em quantidade, com padrão e prazo",
"oque": """<p>Escolas, creches, academias de dança e grupos de teatro precisam de figurinos para muitas ocasiões ao longo do ano: Dia das Crianças, Semana do Folclore, Dia do Índio, festas da primavera, Natal, peças de fim de ano, mostras culturais e formaturas da educação infantil. Nesses casos, o desafio não é uma fantasia, mas <strong>dezenas de peças iguais</strong>, em vários tamanhos, prontas na data certa.</p>
<p>Como somos fábrica, a Tango Fantasias consegue produzir lotes padronizados, com as cores e os temas definidos pela escola ou pelo professor. Trabalhamos personagens do folclore e de contos, animais, flores, elementos da natureza, profissões, personagens históricos, figurinos de dança e muito mais. <!-- CONFIRMAR: tipos de figurino que a empresa produz sob pedido --></p>
<p>Também atendemos famílias que precisam de uma fantasia específica para a apresentação do filho, com venda no varejo.</p>""",
"destaques_titulo": "O que produzimos para escolas e grupos",
"destaques": [
 "Lotes padronizados para turmas, com grade de tamanhos.",
 "Figurinos para teatro, dança, folclore e datas comemorativas.",
 "Saias, tutus, coletes, capas e peças básicas coloridas para montar figurinos.",
 "Acessórios como tiaras, asas, chapéus e máscaras.",
 "Atendimento a escolas, academias, ONGs e grupos culturais.",
 "Organização dos pedidos por turma ou por tamanho. <!-- CONFIRMAR -->",
],
"passos": passos("Envie o tema, a referência (foto ou desenho) e a lista de tamanhos da turma.",
                 "Confirmamos cores e materiais e produzimos o lote dentro do prazo combinado."),
"qualidade_titulo": "Qualidade pensada para crianças no palco",
"qualidade": QUALIDADE_PADRAO + """<p>Em apresentações, as crianças se movimentam, sentam no chão e trocam de roupa com pressa. Por isso, damos preferência a fechamentos simples, elásticos confortáveis e acabamentos que não pinicam. Sempre que possível, faça uma prova antes do dia do evento.</p>""",
"publico": """<p>Escolas públicas e particulares, creches, academias de dança e ballet, grupos de teatro, igrejas, ONGs, projetos sociais, associações de pais e mestres e famílias. Para pedidos institucionais, emitimos nota fiscal. <!-- CONFIRMAR --></p>""",
"condicoes": CONDICOES + "<p>Para eventos escolares, envie a data da apresentação logo no primeiro contato: ela define o prazo de produção.</p>",
"faq_titulo": "figurinos para escolas",
"faq": [
 ("Vocês fazem figurino para a turma toda?", "Sim. Produzimos lotes padronizados com grade de tamanhos para turmas inteiras."),
 ("Posso mandar uma foto de referência?", "Sim. Envie a referência pelo WhatsApp e avaliamos a viabilidade, os materiais e o prazo."),
 ("Qual o prazo para produzir figurinos?", "Depende da quantidade, do modelo e da época do ano. Informe a data do evento no primeiro contato."),
 ("Vocês emitem nota fiscal para escolas?", "Sim, emitimos nota fiscal nas vendas. Informe os dados da instituição no pedido."),
 ("Fazem figurino de ballet e dança?", "Atendemos figurinos de dança conforme o modelo. Consulte a viabilidade pelo WhatsApp."),
],
"relacionados": ["fantasias-infantis", "fantasias-de-festa-junina", "producao-sob-encomenda"],
},
# -------------------------------------------------------------- 7
{
"slug": "acessorios-para-fantasias", "nome": "Acessórios para fantasias", "nome_curto": "Acessórios", "icone": "crown",
"resumo": "Tiaras, coroas, capas, saias tutu, asas, chapéus e máscaras para completar o visual.",
"title": "Acessórios para Fantasias no Atacado | Brás SP",
"desc": "Acessórios para fantasias no atacado e varejo: tiaras, coroas, capas, saias tutu, asas, chapéus e máscaras. Direto da fábrica no Brás, SP. Peça orçamento.",
"h1": "Acessórios para Fantasias no Atacado e Varejo",
"lead": "Tiaras, coroas, capas, saias tutu, asas, chapéus, gravatas e máscaras para completar fantasias e montar visuais rápidos para festas, Carnaval e escola.",
"img": "acessorios-para-fantasias.webp", "img_alt": "Acessórios para fantasias: coroa, tiara, máscara de baile e saia tutu",
"img_cap": "Imagem ilustrativa — substitua por fotos reais dos acessórios.",
"oque_titulo": "O detalhe que completa a fantasia",
"oque": """<p>Acessórios são itens de giro rápido nas lojas: o cliente que compra uma fantasia quase sempre leva algo para completar, e quem não quer uma fantasia inteira monta o visual só com uma tiara, uma capa ou uma saia tutu. No Carnaval e no Halloween, esses itens estão entre os mais vendidos — e com boa margem para o lojista.</p>
<p>A Tango Fantasias trabalha acessórios que conversam com as nossas linhas de fantasias: capas de diversas cores e tamanhos, saias tutu, coroas e tiaras, asas, chapéus, gravatas-borboleta, laços, máscaras de baile e peças temáticas para Carnaval, Halloween e festa junina. <!-- CONFIRMAR: quais acessórios são fabricados e quais são revendidos --></p>
<p>Lojistas podem combinar acessórios com fantasias em kits, aumentando o ticket médio, e escolas usam acessórios para criar figurinos simples e econômicos para turmas inteiras.</p>
<p>Outra vantagem é a versatilidade: uma capa preta serve para vampiro no Halloween e para mágico numa festa infantil; uma saia tutu vira bailarina, fada ou parte de um visual de bloco no Carnaval. Por isso, os acessórios ajudam o lojista a vender o ano inteiro, não só nas grandes datas, e a aproveitar melhor o espaço de exposição na loja.</p>""",
"destaques_titulo": "Acessórios mais procurados",
"destaques": [
 "Capas em várias cores, infantis e adultas.",
 "Saias tutu em cores lisas e com brilho.",
 "Coroas, tiaras e arcos temáticos.",
 "Asas, chapéus, gravatas e laços.",
 "Máscaras de baile para Carnaval e festas temáticas.",
 "Kits para montar fantasias rápidas e econômicas.",
],
"passos": passos("Escolha os acessórios, cores e quantidades pelo WhatsApp ou na fábrica.",
                 "Separamos do estoque ou produzimos o lote nas cores escolhidas."),
"qualidade_titulo": "Qualidade e uso seguro",
"qualidade": QUALIDADE_PADRAO + """<p>Acessórios com peças pequenas, como pedrarias e enfeites, não devem ser usados por crianças muito pequenas sem supervisão. Oriente o consumidor a seguir as indicações de idade e de uso do produto.</p>""",
"publico": """<p>Lojas de fantasias, lojas de festas, armarinhos, papelarias, lojas de presentes, revendedores, escolas, buffets, produtoras de eventos e consumidor final. Condições para revenda na página de <a href="@/atacado.html">atacado</a>.</p>""",
"condicoes": CONDICOES,
"faq_titulo": "acessórios para fantasias",
"faq": [
 ("Posso comprar só acessórios no atacado?", "Sim. Lojistas podem comprar acessórios separados ou combinados com fantasias."),
 ("Vocês fazem capas em cores diferentes?", "Sim, trabalhamos capas em várias cores e tamanhos. Consulte as opções disponíveis."),
 ("Têm saia tutu adulto?", "Trabalhamos tamanhos infantis e adultos. Consulte a grade pelo WhatsApp."),
 ("Fazem kits com fantasia e acessórios?", "Sim, montamos kits para revenda e para escolas."),
 ("Vendem no varejo?", "Sim, atendemos consumidor final."),
],
"relacionados": ["fantasias-de-carnaval", "fantasias-infantis", "fantasias-de-halloween"],
},
# -------------------------------------------------------------- 8
{
"slug": "producao-sob-encomenda", "nome": "Produção de fantasias sob encomenda", "nome_curto": "Produção sob encomenda", "icone": "scissors",
"resumo": "Produção em lote para lojas, marcas, blocos, eventos e empresas, com modelos e cores definidos.",
"title": "Fábrica de Fantasias sob Encomenda | Brás SP",
"desc": "Fábrica de fantasias no Brás, SP: produção em lote sob encomenda para lojas, marcas, blocos, escolas e eventos, com cores e modelos combinados. Fale conosco.",
"h1": "Fábrica de Fantasias: Produção sob Encomenda",
"lead": "Produção de fantasias em lote para lojas, marcas próprias, blocos de Carnaval, escolas, empresas e eventos, com modelos, cores e tamanhos combinados com você.",
"img": "fabrica-de-fantasias-producao.webp", "img_alt": "Área de costura da fábrica de fantasias com tecidos coloridos e máquinas",
"img_cap": "Imagem ilustrativa — substitua por fotos reais da confecção.",
"oque_titulo": "Confecção própria no Brás",
"oque": """<p>A Tango Fantasias é uma indústria de confecção. Isso significa que, além de vender fantasias prontas, podemos <strong>produzir lotes sob encomenda</strong> para quem precisa de modelos específicos: lojas que querem uma linha exclusiva, marcas que vendem com a própria etiqueta, blocos e grupos que saem padronizados, empresas que fazem ações promocionais e escolas que montam apresentações.</p>
<p>O processo começa pela sua referência — uma foto, um desenho ou uma peça-piloto. A partir dela, avaliamos tecidos, aviamentos, modelagem e quantidade mínima viável, e enviamos o orçamento com prazo. <!-- CONFIRMAR: pedido mínimo por modelo, se faz peça-piloto/amostra, se faz etiqueta personalizada (private label) --></p>
<p>Estar no Brás, o maior polo atacadista de confecção de São Paulo, facilita o acesso a tecidos e aviamentos e agiliza a produção. Importante: produzimos peças em série, com grade de tamanhos; não fazemos roupas sob medida individual.</p>""",
"destaques_titulo": "O que podemos produzir",
"destaques": [
 "Linhas exclusivas para lojas e revendedores.",
 "Fantasias com etiqueta da sua marca. <!-- CONFIRMAR private label -->",
 "Lotes padronizados para blocos, cordões e grupos.",
 "Figurinos para escolas, academias e grupos culturais.",
 "Fantasias para ações promocionais e eventos de empresas.",
 "Reposição de modelos e produção em grades de tamanho.",
],
"passos": [
 ("Briefing", "Envie a referência (foto, desenho ou peça), a quantidade estimada, os tamanhos e a data em que precisa das peças."),
 ("Análise e orçamento", "Avaliamos tecidos, aviamentos, modelagem e prazo, e enviamos o orçamento por escrito."),
 ("Aprovação", "Confirmamos os detalhes do modelo e as condições de pagamento antes de iniciar. <!-- CONFIRMAR peça-piloto -->"),
 ("Produção", "Corte, costura e acabamento na nossa confecção, com acompanhamento de qualidade em cada etapa."),
 ("Entrega", "Retirada no Brás ou envio combinado, com nota fiscal."),
],
"qualidade_titulo": "Controle de qualidade em cada lote",
"qualidade": QUALIDADE_PADRAO + """<p>Em produções sob encomenda, conferimos medidas, costuras e acabamento durante o processo para manter o padrão entre as peças do lote. Variações pequenas de tonalidade entre lotes de tecido podem acontecer; por isso, recomendamos produzir de uma vez as peças que precisam ser idênticas.</p>""",
"publico": """<p>Lojas de fantasias e de festas, marcas de moda infantil, e-commerces, blocos de Carnaval, escolas de samba, escolas e academias, empresas, agências de eventos e de marketing promocional.</p>
<p><strong>Atenção a direitos autorais:</strong> não produzimos réplicas de personagens ou marcas registradas sem a autorização (licença) dos detentores dos direitos.</p>""",
"condicoes": "<p>Quantidade mínima, preço e prazo dependem do modelo, dos materiais e da época do ano, e são definidos no orçamento. Em períodos de alta demanda, como antes do Carnaval, a agenda de produção é disputada: planeje com antecedência.</p>",
"faq_titulo": "produção sob encomenda",
"faq": [
 ("Qual a quantidade mínima para produção sob encomenda?", "Depende do modelo e dos materiais. Informamos a quantidade mínima viável no orçamento."),
 ("Vocês fazem fantasia com a etiqueta da minha marca?", "Consulte a disponibilidade de produção com etiqueta personalizada pelo WhatsApp."),
 ("Posso enviar uma foto como referência?", "Sim. Com a foto ou desenho, avaliamos materiais, modelagem e prazo."),
 ("Vocês fazem roupa sob medida?", "Não. Produzimos em série, com grade de tamanhos, para lojas, grupos e eventos."),
 ("Produzem fantasia de personagem famoso?", "Somente com autorização dos detentores dos direitos. Podemos criar modelos com visual próprio inspirados em temas genéricos."),
],
"relacionados": ["fantasias-para-escolas-e-apresentacoes", "fantasias-de-carnaval", "fantasias-adultas"],
},
]
