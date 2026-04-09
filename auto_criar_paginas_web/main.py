#IMPORTS
import pyautogui as pa
import pyperclip as pc
from time import sleep

#VARIAVEIS
webpage = "https://expanssiva.com.br/admin#/pages"
produto_busca = "Revistas Personalizadas em "
pa.PAUSE = 0.7

#cidades
cidades = [
    "Gramado",
    "Canoas"
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
    pa.write(produto_busca)
    pc.copy(cidades[i])
    pa.hotkey("ctrl", "v")
    pa.press("enter")
    sleep(1)

    #clicar em editar a pagina buscada
    pa.click(r"imgs\editar.png")
    pa.moveTo(x=100, y=100)
    sleep(1)

    #selecionar codigo p/ substituir
    pa.press("tab")
    pa.hotkey("ctrl", "a")

    #codigo da pagina
    cod_pagina = f"""<!-- Topo -->
    <x-page id="4315"/> 

    <div class="container"> 
        <h1 style="text-align:center; color:#222; font-size:1.6rem; padding-top:13px; margin-bottom:3px; line-height:1.2; font-weight:700;">
            Revistas Personalizadas para {cidades[i]} com Entrega Rápida
        </h1>

        <!-- Produtos PG Revistas -->
        <x-page id="4318"/>
    </div>

    <div class="container">

        <h2 class="h2-pg">Revistas Personalizadas para {cidades[i]} com Impressão de Alta Qualidade</h2>

        <p>
            Somos uma <strong>gráfica online especializada</strong> na criação e impressão de materiais gráficos voltados para divulgação, apresentação e fortalecimento de marcas. Produzimos 
            <a href="/categoria/revistas"><strong>revistas personalizadas</strong></a> 
            com alto padrão de qualidade, atendendo desde pequenas até grandes tiragens com total flexibilidade.
        </p>

        <p>
            Você pode configurar sua revista conforme a sua necessidade, escolhendo o tipo de papel da capa e do miolo, além de acabamentos como 
            <strong>laminação fosca ou brilho</strong>, garantindo maior durabilidade e um visual sofisticado. Trabalhamos com produção ágil e envio eficiente para {cidades[i]} e região.
        </p>

        <h2 class="h2-pg">Para que servem as revistas personalizadas?</h2>

        <ul>
            <li>Divulgação de produtos e serviços</li>
            <li>Apresentações institucionais</li>
            <li>Catálogos comerciais</li>
            <li>Materiais para eventos e feiras</li>
            <li>Projetos editoriais e promocionais</li>
        </ul>

        <p>
            As revistas são uma ferramenta estratégica de marketing, permitindo apresentar informações de forma organizada, visualmente atrativa e com grande impacto no público.
        </p>

        <h2 class="h2-pg">Tamanhos mais utilizados para revistas personalizadas</h2>

        <p>
            As revistas podem ser produzidas conforme o seu projeto gráfico, desde que respeitem os padrões técnicos para impressão. Confira alguns dos formatos mais utilizados:
        </p>

        <ul>
            <li>10,5 x 15 cm (fechada) – 21 x 15 cm (aberta)</li>
            <li>15 x 21 cm (fechada) – 30 x 21 cm (aberta)</li>
            <li>21 x 30 cm (fechada) – 42 x 30 cm (aberta)</li>
        </ul>

        <p>
            É importante considerar sempre a diferença entre o tamanho aberto e fechado para garantir um layout bem aplicado.
        </p>

        <h2 class="h2-pg">Criação de arte para revistas personalizadas</h2>

        <p>
            Você pode enviar sua própria arte durante o processo de compra. Caso não possua um layout pronto, nosso time criativo está preparado para desenvolver um projeto exclusivo, focado em 
            <strong>comunicação visual eficiente e apresentação profissional</strong>.
        </p>

        <p>
            Criamos materiais pensados para gerar impacto, transmitir credibilidade e valorizar seus produtos ou serviços.
        </p>

        <h2 class="h2-pg">Revistas personalizadas com fotos</h2>

        <p>
            As <strong>revistas personalizadas com fotos</strong> são ideais para registrar momentos especiais como eventos, viagens, comemorações ou projetos pessoais. Com impressão de alta qualidade, você transforma memórias em um material durável e sofisticado.
        </p>

        <p>
            Personalize com imagens, textos e diagramação exclusiva, criando uma peça única e cheia de significado.
        </p>

        <h2 class="h2-pg">Revistas para divulgação de produtos e serviços</h2>

        <p>
            Utilize revistas como uma poderosa ferramenta de marketing para apresentar seus produtos e serviços de forma detalhada e profissional.
        </p>

        <ul>
            <li>Inclua fotos e descrições completas</li>
            <li>Apresente diferenciais competitivos</li>
            <li>Utilize gráficos e elementos visuais</li>
            <li>Fortaleça sua marca com material impresso de alto padrão</li>
        </ul>

        <p>
            Esse tipo de material é ideal para distribuição em eventos, feiras, pontos de venda ou envio direto para clientes.
        </p>

        <h2 class="h2-pg">Por que escolher nossa gráfica para atender {cidades[i]}?</h2>

        <ul>
            <li>Alta qualidade de impressão</li>
            <li>Flexibilidade de tiragem</li>
            <li>Acabamentos profissionais</li>
            <li>Produção rápida</li>
            <li>Atendimento especializado</li>
        </ul>

        <h2 class="h2-pg">Produção ágil e envio rápido para {cidades[i]}</h2>

        <p>
            Oferecemos <strong>produção eficiente e logística otimizada</strong>, garantindo que suas revistas personalizadas cheguem rapidamente até você em {cidades[i]}.
        </p>

        <p>
            Simule agora mesmo o seu pedido: clique em <strong>simular preço</strong>, informe seu CEP e visualize prazos e valores de forma prática.
        </p>

        <hr>

    </div>

    <!-- Comentários de Clientes -->
    <x-page id="2799"/>"""

    #copiar e colar o codigo ja substituido
    pc.copy(cod_pagina)
    pa.hotkey("ctrl", "v")
    pa.press("f3")
    pa.hotkey("ctrl", "w")

    print(f"{cidades[i]}")
