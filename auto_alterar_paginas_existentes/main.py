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
produto_busca = "Gráfica em "
pa.PAUSE = 0.7

#cidades
cidades = [
    "Minas Novas",
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
    <!-- Topo -->
<x-page id="4356" />

<div style="display:flex; flex-direction:column; align-items:center; text-align:center; padding: 6px 6px;">

    <h1 style="font-size: clamp(18px, 5vw, 28px); margin: 0 0 1px 0; max-width: 90%;">
        Gráfica Online com Entrega Rápida em {cidades[i]}
    </h1>

    <span style="color:#6b6b6b; font-size:1.0rem; line-height:1.3; margin-bottom:6px;">
        Impressos que fortalecem sua marca.
    </span>

</div>

<!-- Conteúdo 01 -->
<x-page id="735" />

<!-- Conteúdo pagina variavel -->
<div class="container">
    <div style="text-align:center; padding: 20px 10px;">

        <div style="margin-bottom: 8px;">
            <span style="color:#6b6b6b; font-size:1.6rem; font-weight:600; letter-spacing:-0.5px;">
                Sua Marca em Destaque com Impressão Profissional em <b>{cidades[i]}</b>
            </span>
        </div>

        <div>
            <span style="color:#6b6b6b; font-size:1.3rem; line-height:1.5;">
                Qualidade profissional para empresas que querem se <b>destacar</b>.
            </span>
        </div>
    </div>
</div> <!-- fecha container -->

<!-- Conteúdo 02 -->
<x-page id="4351" />

<!-- TEXTO SEO -->
<div style="max-width: 1220px; margin: 0 auto; padding: 20px;">
    <h2>
        <strong>Gráfica em {cidades[i]}</strong>: Impressão de Qualidade e Estratégia de Entrega Rápida
    </h2>

    <p>
    Somos um modelo inovador de <strong><a href="/" title="Gráfica Online com Entrega Rápida de Papelaria e Brindes">gráfica online</a></strong>, projetado para romper as barreiras da distância e oferecer para <strong>{cidades[i]}</strong> o que há de mais moderno em tecnologia de impressão. Nossa missão é unir qualidade impecável, preço de fábrica e uma criatividade sem limites, permitindo que sua marca atinja objetivos ambiciosos em todas as frentes de divulgação, desde o ambiente físico até o digital.
</p>

<p>
    Entendemos que o mercado de <strong>{cidades[i]}</strong> exige agilidade e um padrão estético superior. Por isso, nossa plataforma não funciona apenas como um balcão de pedidos, mas como um parceiro estratégico. Ao escolher nossos serviços, você elimina intermediários e acessa um fluxo de produção industrial de alta performance, garantindo que cada impresso seja uma ferramenta real de conversão para o seu negócio.
</p>

<h3 style="font-size:20px; color:#333;">
    Papelaria Corporativa de Alto Padrão em <strong>{cidades[i]}</strong>
</h3>

<p>
    A <strong>
        <a href="/papelaria-personalizada" title="Papelaria Personalizada para Empresas com Impressão Profissional">
    papelaria personalizada
</a>
    </strong>
    é, muitas vezes, o primeiro ponto de contato físico entre sua empresa e seu cliente. Em <strong>{cidades[i]}</strong>, onde o profissionalismo é um diferencial competitivo, oferecemos soluções completas: cartões de visita com acabamentos especiais (como laminação fosca e verniz localizado), papéis timbrados que transmitem credibilidade, pastas profissionais, envelopes e blocos de notas personalizados.
</p>

<p>
    Cada detalhe da nossa <strong>impressão gráfica</strong> é calibrado para garantir a fidelidade das cores da sua identidade visual. Ter uma papelaria coordenada e bem impressa não é apenas um custo, mas um investimento em autoridade que fortalece a percepção de valor da sua marca diante do público teresopolitano.
</p>

<h3 style="font-size:20px; color:#333;">
    Brindes Personalizados: Fidelização e Presença de Marca
</h3>

<p>
    Para quem busca <strong>
       <a href="/brindes-personalizados" title="Brindes Personalizados para Empresas com Alta Qualidade">
    brindes personalizados
</a> em {cidades[i]}
    </strong>, oferecemos um catálogo diversificado que transforma itens cotidianos em embaixadores da sua marca. De canetas e squeezes a agendas e kits corporativos luxuosos, nossa linha de produtos é pensada para criar conexões emocionais. Além da papelaria, nossa expertise se estende à <strong>comunicação visual</strong>, com banners, adesivos e embalagens que garantem um <i>unboxing</i> memorável para seus clientes.
</p>

<p>
    O grande diferencial de nossos <strong>brindes personalizados</strong> é a durabilidade e o design. Entendemos que um brinde de baixa qualidade pode prejudicar sua imagem; por isso, selecionamos materiais resistentes e técnicas de gravação avançadas, assegurando que sua logomarca permaneça em evidência por muito mais tempo na rotina dos seus parceiros em <strong>{cidades[i]}</strong>.
</p>

<h3 style="font-size:20px; color:#333;">
    Logística Inteligente e Consultoria Dedicada para <strong>{cidades[i]}</strong>
</h3>

<p>
    Um dos grandes receios de quem contrata serviços fora de sua cidade é o prazo e o suporte. Nós resolvemos isso com uma <strong>rede logística otimizada</strong> para o estado do Rio de Janeiro. Possuímos uma vasta carteira de clientes em <strong>{cidades[i]}</strong> e arredores, e a entrega é feita de forma super rápida através de parcerias estratégicas que garantem preços competitivos de frete, tanto para pequenos volumes quanto para grandes demandas industriais.
</p>

<p>
    Além da rapidez, todos os pedidos são acompanhados por um <strong>consultor técnico</strong> exclusivo. Este profissional mantém contato constante com você durante todas as etapas — da conferência do arquivo à expedição — garantindo uma experiência satisfatória do início ao fim. Para nós, a tecnologia é o meio, mas o sucesso das pessoas em <strong>{cidades[i]}</strong> é o nosso objetivo final. Você pode realizar simulações de prazos e valores diretamente em nosso site e comprovar a eficiência do nosso modelo de negócio.
</p>
	<x-page id="3952"/>
</div>

<!-- COMENTÁRIOS DE CLIENTES -->
<x-page id="25"/>
<br/>"""

    #copiar e colar o codigo ja substituido
    pc.copy(cod_pagina)
    pa.hotkey("ctrl", "v")

    #descer a pagina para preencher os campos de title, keywords e description
    pa.click(x=1717, y=534) #posicao fora do editor de txto para evitar interferencia
    pa.press("down", presses=70)

    #variavel do title
    title = f"Gráfica em {cidades[i]} com Impressão Rápida e Alta Qualidade"
    keywords = f"gráfica em {cidades[i]}, gráfica {cidades[i]} rj, gráfica rápida {cidades[i]}, impressão digital {cidades[i]}, brindes personalizados {cidades[i]}, gráfica online {cidades[i]}, serviços gráficos {cidades[i]}, impressão de alta qualidade {cidades[i]}, gráfica para empresas {cidades[i]}"
    description = f"Precisa de gráfica em {cidades[i]}? Impressos com alta qualidade, produção rápida e atendimento ágil. Solicite seu orçamento agora mesmo! ⚡"

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
    pa.hotkey("ctrl", "w")
    
    print(f"Pagina da cidade {cidades[i]} alterada com sucesso!")

