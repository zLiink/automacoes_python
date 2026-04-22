"""
Automação de edição de páginas no painel administrativo.

Este script utiliza PyAutoGUI para automatizar a criação e edição de páginas
em um sistema web, substituindo o conteúdo HTML com base em uma lista de cidades.

Para cada cidade:
- Abre uma nova aba no navegador
- Acessa a página administrativa
- Busca pelo produto + nome da cidade
- Entra no modo de edição
- Substitui todo o conteúdo da página por um template HTML dinâmico
- Insere automaticamente o nome da cidade no conteúdo

Objetivo: agilizar a criação/atualização em massa de páginas personalizadas
para diferentes localidades.
"""

#IMPORTS
import pyautogui as pa
import pyperclip as pc
from time import sleep

#VARIAVEIS
webpage = "https://expanssiva.com.br/admin#/pages"
produto_busca = "Folders Personalizados em "
pa.PAUSE = 0.4

#cidades
cidades = [
"Sapiranga",
"Santana do Livramento",
"Ijuí",
"Guaíba",
"Erechim",
"Bento Gonçalves",
"Uruguaiana",
"Cachoeirinha",
"Santa Cruz do Sul",
"Alvorada",
"Rio Grande",
"Passo Fundo",
"São Leopoldo",
"Viamão",
"Novo Hamburgo",
"Gravataí",
"Santa Maria",
"Pelotas",
"Canoas",
"Caxias do Sul",
"Porto Alegre",
"Tubarão",
"Brusque",
"Balneário Camboriú",
"Lages",
"Palhoça",
"Jaraguá do Sul",
"Criciúma",
"Chapecó",
"Itajaí",
"São José",
"Blumenau",
"Florianópolis",
"Joinville",
"Umuarama",
"Arapongas",
"Pinhais",
"Apucarana",
"Toledo",
"Araucária",
"Guarapuava",
"Colombo",
"Foz do Iguaçu",
"São José dos Pinhais",
"Cascavel",
"Ponta Grossa",
"Maringá",
"Londrina",
"Curitiba",
"Passos",
"Araguari",
"Patos de Minas",
"Governador Valadares",
"Ribeirão das Neves",
"Nova Lima",
"Pouso Alegre",
"Ibirité",
"Poços de Caldas",
"Divinópolis",
"Santa Luzia",
"Sete Lagoas",
"Ipatinga",
"Uberaba",
"Montes Claros",
"Betim",
"Juiz de Fora",
"Contagem",
"Uberlândia",
"Belo Horizonte",
"Araraquara",
"Itu",
"Marília",
"Taboão da Serra",
"Sumaré",
"Limeira",
"Hortolândia",
"Presidente Prudente",
"Jacareí",
"Cotia",
"São Caetano do Sul",
"Americana",
"Franca",
"Itaquaquecetuba",
"Indaiatuba",
"Piracicaba",
"Mogi das Cruzes",
"Santos",
"São José do Rio Preto",
"Jundiaí",
"Barueri",
"Jundiaí",
"São José do Rio Preto",
"Sorocaba",
"Ribeirão Preto",
"São José dos Campos",
"Osasco",
"Santo André",
"São Bernardo do Campo",
"Guarulhos",
"São Paulo"
]

#TEMPO P/ INÍCIO AUTO
sleep(2)

for i in range(len(cidades)):
    #abrir nova aba
    pa.hotkey("ctrl", "t")
    pa.write(webpage)
    pa.press("enter")
    sleep(1.5)

    #pesquisar cidade
    pc.copy(produto_busca)
    pa.hotkey("ctrl", "v")
    pc.copy(cidades[i])
    pa.hotkey("ctrl", "v")
    pa.press("enter")
    sleep(1)

    #clicar em editar a pagina buscada
    caminho_img_editar = r"Y:\DESIGNS\Guilherme_link\VSCODE\Automacoes_em_py\auto_alterar_paginas_existentes\imgs\editar.png"
    pa.click(pa.locateCenterOnScreen(caminho_img_editar, confidence=0.9))
    pa.moveTo(x=100, y=100)
    sleep(1)

    #selecionar codigo p/ substituir
    pa.press("tab")
    pa.hotkey("ctrl", "a")

    #codigo da pagina
    cod_pagina = f"""
    <!--Topo-->
<x-page id="4326" />

<!--Conteudo variado 1-->
<div style="text-align:center; padding: 9px;">
    <h1 style="font-size: clamp(18px, 5vw, 26px); margin: 0 0 4px;">
        Impressão de Folders com Entrega Rápida em {cidades[i]}
    </h1>

    <p style="color:#6b6b6b; font-size:1rem; line-height:1.3;">
        Produção ágil e impressão de alto padrão para divulgar sua empresa com resultado.
    </p>
</div>

<!--Conteúdo 1-->
<x-page id="4327" />

<!--Conteudo variado 2-->
<div style="text-align:center; padding: 10px 2px; background:#f6631d; border-radius:0px;">
    <p style="color:#ffffff; font-size:1.6rem; font-weight:600; letter-spacing:-0.5px; margin-bottom:10px;">
        Sua Marca em Destaque com Impressão Profissional em <b>{cidades[i]}</b>
    </p>
    <p style="color:#ffffff; font-size:1.3rem; line-height:1.5;">
        Qualidade profissional para empresas que querem se <b>destacar</b>.
    </p>
</div>

<!--TEXTO SEO-->
<div class="container" style="padding: 20px 2px;">
    <article>
        <h2>Impressão de Folders em {cidades[i]}: A Solução Ideal para sua Divulgação</h2>

        <p>
            Se você está buscando <strong>impressão de folders em {cidades[i]}</strong>, sabe que a agilidade e a qualidade do material são fundamentais para o sucesso de uma estratégia de marketing offline. Em uma cidade com economia pulsante e um setor de serviços tão competitivo, apresentar sua empresa com um material gráfico de alto padrão não é apenas um detalhe, é uma necessidade estratégica para se destacar no mercado campineiro.
        </p>

        <p>
            Nossa plataforma atua como uma gráfica online especializada, conectando as necessidades das empresas de <strong>{cidades[i]}</strong> às melhores tecnologias de impressão digital e offset. Seja para um evento corporativo ou para prospecção direta nos bairros mais movimentados da cidade, entregamos folders que comunicam autoridade e profissionalismo, integrando perfeitamente o seu mix de <strong><a href="/papelaria-personalizada">papelaria</a></strong> institucional.
        </p>

        <h2>Folders Personalizados em {cidades[i]} com Entrega Rápida</h2>

        <p>
            Entendemos que para o empresário local o tempo é um recurso escasso. Por isso, otimizamos nossa logística para garantir que a <strong>entrega de <a href="/categoria/folders">folders em {cidades[i]}</a></strong> seja feita com o máximo de eficiência. Ao optar por nossa gráfica online, você tem a conveniência de fazer o pedido sem sair do seu escritório, contando com um sistema de rastreio moderno e prazos que respeitam o cronograma de vendas da sua empresa.
        </p>

        <p>
            Atendemos desde pequenos comércios locais até grandes indústrias instaladas nos principais polos comerciais de <strong>{cidades[i]}</strong>. Nosso foco é garantir que o seu material promocional chegue em suas mãos com cores vibrantes e acabamento impecável, reforçando a identidade visual da sua marca em toda a cidade.
        </p>

        <h3>Modelos e Utilidades para sua Estratégia em {cidades[i]}</h3>

        <ul>
            <li><strong>Folder 1 dobra:</strong> Conhecido como meia dobra, é ideal para comunicados diretos, convites corporativos e apresentações rápidas de impacto.</li>
            <li><strong>Folder 2 dobras:</strong> O formato mais versátil, excelente para apresentações institucionais, lançamentos de produtos e materiais de vendas estruturados.</li>
            <li><strong>Folder 3 dobras (Sanfona ou Carteira):</strong> Oferece maior área útil, sendo perfeito para guias detalhados de serviços, manuais de produtos e fluxos de informações complexas.</li>
            <li><strong>Papel Couchê 90g a 150g:</strong> Proporciona o equilíbrio ideal entre custo-benefício, resistência e qualidade de impressão para grandes tiragens.</li>
            <li><strong>Acabamentos Premium:</strong> Aplicações de verniz total ou localizado que elevam o status do material, garantindo um impacto visual profissional e duradouro.</li>
        </ul>

        <h2>Por que escolher nossa Gráfica Online para atender {cidades[i]}?</h2>

        <p>
            Muitos clientes buscam por <strong>onde fazer folders em {cidades[i]}</strong> e precisam de uma solução que una qualidade de agência e preço de fábrica. Nossa proposta é oferecer exatamente isso para quem precisa contratar <strong>folders para empresas em {cidades[i]}</strong>, com a facilidade de um processo 100% digital e suporte especializado.
        </p>

        <ol>
            <li><strong>Custo-benefício superior:</strong> Preços competitivos com acabamento profissional em toda a linha de materiais impressos.</li>
            <li><strong>Tecnologia de ponta:</strong> Impressoras de última geração que garantem fidelidade de cores em CMYK e alta definição.</li>
            <li><strong>Facilidade no Orçamento:</strong> Sistema intuitivo para selecionar configurações e visualizar o investimento da sua campanha na hora.</li>
        </ol>

        <h2>Folders em {cidades[i]}: Impacto Visual que Converte Clientes Reais</h2>

        <p>
            A distribuição de material impresso continua sendo uma das formas mais eficazes de conversão em <strong>{cidades[i]}</strong>. O uso de <strong>folders personalizados preço</strong> justo permite que você escale sua panfletagem sem comprometer o orçamento. Para maximizar o impacto das suas ações, considere integrar o uso de folders com <strong><a href="/brindes-personalizados">brindes corporativos</a></strong> personalizados, criando uma experiência de marca muito mais poderosa e memorável.
        </p>

        <p>
            O folder é uma ferramenta tátil: ele permanece na mesa do seu cliente, garantindo que sua mensagem seja lembrada por muito mais tempo. Em uma cidade dinâmica como <strong>{cidades[i]}</strong>, essa presença física e a qualidade da sua <strong>papelaria</strong> são diferenciais importantes frente à concorrência digital.
        </p>

        <h3>Dicas para um Layout de Folder que Gere Resultados</h3>

        <p>
            Para que seu investimento em uma <strong>gráfica de folders rápida</strong> traga retorno, considere incluir um título chamativo que resolva uma dor do seu cliente e um <em>Call to Action</em> (CTA) claro, como um QR Code direcionando para o seu WhatsApp de vendas em <strong>{cidades[i]}</strong>.
        </p>

        <h2>Solicite sua Impressão de Folders para {cidades[i]}</h2>

        <p>
            Não deixe sua comunicação para depois. Se você busca um <strong>folder 2 dobras papel couchê</strong> ou materiais com acabamentos especiais, nossa plataforma está pronta para atender sua demanda em <strong>{cidades[i]}</strong> com agilidade. Configuramos nossos processos para oferecer a melhor experiência de compra online de materiais gráficos e soluções para empresas.
        </p>

        <p>
            Seja para uma feira de negócios, um lançamento regional ou para reforçar sua presença de marca, conte com nossa expertise em impressão e logística para <strong>{cidades[i]}</strong>. Garanta agora materiais profissionais que vendem por você!
        </p>
    </article>
</div>

<!--COMENTÁRIOS DE CLIENTES-->
<x-page id="7236"/>
<br/>"""

    #copiar e colar o codigo ja substituido
    pc.copy(cod_pagina)
    pa.hotkey("ctrl", "v")

    #descer a pagina para preencher os campos de title, keywords e description
    pa.click(x=1717, y=534) #posicao fora do editor de txto para evitar interferencia
    pa.press("down", presses=70)

    #variavel do title
    title = f"Folders {cidades[i]} com Entrega Rápida e Alta Qualidade"
    keywords = f"folders em {cidades[i]}, impressão de folders {cidades[i]}, folders personalizados {cidades[i]}, gráfica com entrega em {cidades[i]}, folders para empresas {cidades[i]}, onde fazer folders {cidades[i]}"
    description = f"Folders em {cidades[i]} com produção rápida e qualidade profissional. Perfeitos para atrair clientes e fortalecer sua marca. Peça seu orçamento agora!"

    #preencher campos  title, keywords e description
    pa.click(x=935, y=528)
    pa.hotkey("ctrl", "a")
    pc.copy(title)
    pa.hotkey("ctrl", "v")
    pa.press("tab")
    pa.hotkey("ctrl", "a")
    pc.copy(keywords)
    pa.hotkey("ctrl", "v")
    pa.press("tab")
    pa.hotkey("ctrl", "a")
    pc.copy(description)
    pa.hotkey("ctrl", "v")
    pa.press("tab")
    
    #salvar e fechar aba
    pa.press("f3")
    sleep(1)
    pa.hotkey("ctrl", "w")
    
    print(f"Pagina da cidade {cidades[i]} alterada com sucesso!")

