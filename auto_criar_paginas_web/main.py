"""
Automação de criação de páginas web em sistema interno.

Este script utiliza PyAutoGUI para automatizar o processo de criação de páginas
no painel administrativo, gerando conteúdos personalizados com base em uma lista
de cidades.

Para cada cidade, o script:
- Acessa o sistema
- Cria uma nova página
- Define o título dinamicamente
- Insere um template HTML com conteúdo personalizado

Objetivo: agilizar a criação em massa de páginas otimizadas para diferentes localidades.
"""

#IMPORTS
import pyautogui as pa
import pyperclip as pc
from time import sleep

#VARIAVEIS
webpage = "https://expanssiva.com.br/admin#/pages"
produto_criar = "Folders Personalizados em "
pa.PAUSE = 0.7

#cidades
cidades = [
    "Jundiaí",
    "São José do Rio Preto",
    "Santos",
    "Mogi das Cruzes",
    "Piracicaba",
    "Indaiatuba",
    "Itaquaquecetuba",
    "Franca",
    "Americana",
    "São Caetano do Sul",
    "Cotia",
    "Jacareí",
    "Presidente Prudente",
    "Hortolândia",
    "Limeira",
    "Sumaré",
    "Taboão da Serra",
    "Marília",
    "Itu",
    "Araraquara",
    "Belo Horizonte",
    "Uberlândia",
    "Contagem",
    "Juiz de Fora",
    "Betim",
    "Montes Claros",
    "Uberaba",
    "Ipatinga",
    "Sete Lagoas",
    "Santa Luzia",
    "Divinópolis",
    "Poços de Caldas",
    "Ibirité",
    "Pouso Alegre",
    "Nova Lima",
    "Ribeirão das Neves",
    "Governador Valadares",
    "Patos de Minas",
    "Araguari",
    "Passos",
    "Curitiba",
    "Londrina",
    "Maringá",
    "Ponta Grossa",
    "Cascavel",
    "São José dos Pinhais",
    "Foz do Iguaçu",
    "Colombo",
    "Guarapuava",
    "Araucária",
    "Toledo",
    "Apucarana",
    "Pinhais",
    "Arapongas",
    "Umuarama",
    "Joinville",
    "Florianópolis",
    "Blumenau",
    "São José",
    "Itajaí",
    "Chapecó",
    "Criciúma",
    "Jaraguá do Sul",
    "Palhoça",
    "Lages",
    "Balneário Camboriú",
    "Brusque",
    "Tubarão",
    "Porto Alegre",
    "Caxias do Sul",
    "Canoas",
    "Pelotas",
    "Santa Maria",
    "Gravataí",
    "Novo Hamburgo",
    "Viamão",
    "São Leopoldo",
    "Passo Fundo",
    "Rio Grande",
    "Alvorada",
    "Santa Cruz do Sul",
    "Cachoeirinha",
    "Uruguaiana",
    "Bento Gonçalves",
    "Erechim",
    "Guaíba",
    "Ijuí",
    "Santana do Livramento",
    "Sapiranga"
]

#TEMPO P/ INÍCIO AUTO
sleep(2)

for i in range(len(cidades)):
    #abrir nova aba
    pa.hotkey("ctrl", "t")
    pa.write(webpage)
    pa.press("enter")
    sleep(1.5)

    #clicar em editar a pagina buscada
    pa.click(r"imgs\nova_pagina.png")
    pa.moveTo(x=100, y=100)
    sleep(1)

    #insere o nome da pagina + cidade
    pa.write(produto_criar)
    pc.copy(cidades[i])
    pa.hotkey("ctrl", "v")
    pa.press("enter")
    sleep(1)

    #codigo da pagina
    cod_pagina = f"""<!-- TOPO -->
<x-page id="4326"/>

<div class="container">
    <br>
    <h1 style="text-align:center; font-size:clamp(16px,4vw,23px); margin:9 9 8px; color:#222;">
        Impressão de Folders para {cidades[i]} com Qualidade e Entrega Rápida
    </h1>
    <p style="text-align:center;">
        Dê visibilidade à sua marca com copos criativos, funcionais e cheios de personalidade!
    </p>
</div>

<!-- CONTEÚDO -->
<x-page id="4327"/>

<div class="container">
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

<!-- Comentários -->
<hr>
<br />
<x-page id="7236"/>
<br />"""

    #copiar e colar o codigo ja substituido
    pa.press("tab")
    pc.copy(cod_pagina)
    pa.hotkey("ctrl", "v")
    pa.click(x=1740, y=604)

    #descer a pagina para preencher os campos de title, keywords e description
    pa.press("down", presses=70)

    #variavel do title
    title = f"Folders em {cidades[i]}: Impressão e Entrega Rápida"
    kywords = f"folders em {cidades[i]}, impressão de folders {cidades[i]}, gráfica online entrega em {cidades[i]}, folders personalizados preço, onde fazer folders em {cidades[i]}, folders para empresas {cidades[i]}, gráfica de folders rápida, folder 2 dobras papel couchê, material promocional em {cidades[i]}"
    description = f"Precisa de folders em {cidades[i]}? Gráfica online especializada em folders personalizados com entrega em toda a região. Alta qualidade e melhor preço. Confira!"

    #preencher campos  title, kyewords e description
    pa.click(x=935, y=528)
    pc.copy(title)
    pa.hotkey("ctrl", "v")
    pa.press("tab")
    pc.copy(kywords)
    pa.hotkey("ctrl", "v")
    pa.press("tab")
    pc.copy(description)
    pa.hotkey("ctrl", "v")
    pa.press("tab")
    
    #salvar e fechar aba
    pa.hotkey("ctrl", "w")
    pa.press("enter")

    print(f"Pagina da cidade {cidades[i]} criada com sucesso!")