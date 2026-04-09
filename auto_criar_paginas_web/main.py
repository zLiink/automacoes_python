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

title = f"Folders Personalizados para "
kywords = "folders personalizados, folders personalizados com fotos, folders personalizados para divulgação de produtos e serviços, folders personalizados para eventos, folders personalizados para feiras, folders personalizados para pontos de venda, folders personalizados para envio direto, gráfica online especializada em folders personalizados, produção ágil de folders personalizados, envio rápido de folders personalizados"
description = "Somos uma gráfica online especializada na criação e impressão de folders personalizados, atendendo desde pequenas até grandes tiragens com total flexibilidade. Oferecemos produção ágil e envio eficiente para diversas localidades, garantindo que seus folders personalizados cheguem rapidamente até você."

#cidades
cidades = [
    "São Paulo",
    "Campinas"
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
    pa.press("tab")
    pc.copy(cod_pagina)
    pa.hotkey("ctrl", "v")
    pa.click(x=1740, y=604)

    #descer a pagina para preencher os campos de title, keywords e description
    pa.press("down", presses=60)

    #preencher campos  title, kyewords e description
    pa.click(x=935, y=528)
    pc.copy(title + cidades[i])
    pa.hotkey("ctrl", "v")
    pa.press("tab")
    pc.copy(kywords)
    pa.hotkey("ctrl", "v")
    pa.press("tab")
    pc.copy(description)
    pa.hotkey("ctrl", "v")
    pa.press("tab")
    pa.press("enter")

    #salvar e fechar aba
    pa.hotkey("ctrl", "w")

    print(f"Pagina da cidade{cidades[i]} criada com sucesso!")