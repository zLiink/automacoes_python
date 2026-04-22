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
import json

# VARIAVEIS
webpage = "https://expanssiva.com.br/admin#/pages"
produto_busca = "Gráfica em "
pa.PAUSE = 0.4

# LER JSON
with open("dados.json", "r", encoding="utf-8") as f:
    dados = json.load(f)

#TEMPO DE ESPERA PARA O USUÁRIO ABRIR O NAVEGADOR E COLOCAR NA TELA DE LOGIN
sleep(2)

# LOOP CORRETO
for item in dados:

    cidade = item["cidade"]
    bloco_1 = item["bloco_1"]
    bloco_2 = item["bloco_2"]
    bloco_3 = item["bloco_3"]

    # abrir nova aba
    pa.hotkey("ctrl", "t")
    pa.write(webpage)
    pa.press("enter")
    sleep(1.5)

    # pesquisar cidade
    pc.copy(produto_busca + cidade)
    pa.hotkey("ctrl", "v")
    pa.press("enter")
    sleep(1)

    # clicar editar
    caminho_img_editar = r"Y:\DESIGNS\Guilherme_link\VSCODE\Automacoes_em_py\auto_alterar_paginas_existentes\imgs\editar.png"
    pa.click(pa.locateCenterOnScreen(caminho_img_editar, confidence=0.9))
    pa.moveTo(x=100, y=100)
    sleep(1)

    # selecionar tudo
    pa.press("tab")
    pa.hotkey("ctrl", "a")

    # TEMPLATE DINÂMICO
    cod_pagina = f"""
    <!--Topo-->
<x-page id="4356" />

<!--Conteudo variado 1-->
<div style="text-align:center; padding: 6px;">
    <h1 style="font-size: clamp(18px, 5vw, 26px); margin: 0 0 4px;">
        Gráfica Online com Entrega Rápida em {cidade}
    </h1>

    <p style="color:#6b6b6b; font-size:1rem; line-height:1.3;">
        Impressos que fortalecem sua marca.
    </p>
</div>

<!--Conteúdo 1-->
<x-page id="735" />

<!--Conteudo variado 2-->
<div class="container" style="text-align:center; padding: 10px 2px;">
    <p style="color:#6b6b6b; font-size:1.6rem; font-weight:600; letter-spacing:-0.5px; margin-bottom:8px;">
        Sua Marca em Destaque com Impressão Profissional em <b>{cidade}</b>
    </p>

    <p style="color:#6b6b6b; font-size:1.3rem; line-height:1.5;">
        Qualidade profissional para empresas que querem se <b>destacar</b>.
    </p>
</div>

<!--Conteúdo 2-->
<x-page id="4351" />

<!--TEXTO SEO-->
<div style="max-width: 1220px; margin: 0 auto; padding: 20px;">

	<article itemscope itemtype="https://schema.org/Article">

<h2 style="font-family:'Montserrat',Arial,sans-serif; font-size:clamp(1.2rem,3vw,1.6rem); font-weight:800; color:#222; margin:0 0 16px; line-height:1.3;">
    <strong>Gráfica em {cidade}</strong>: Impressão de Qualidade e Entrega Rápida para sua Marca
</h2>

<p style="font-family:'Montserrat',Arial,sans-serif; font-size:0.95rem; color:#555; line-height:1.8; margin:0 0 28px;">
Somos um modelo inovador de <strong><a href="/" title="Gráfica Online com Entrega Rápida de Papelaria e Brindes" style="color:#f6631d; text-decoration:none;">gráfica online</a></strong> projetado para romper as barreiras da distância — oferecendo para empresas em <strong style="color:#222;">{cidade}</strong> o que há de mais moderno em tecnologia de impressão. Nossa missão é unir qualidade impecável, melhor preço e criatividade sem limites em cada projeto de <strong><a href="/papelaria-personalizada" title="Papelaria Personalizada para Empresas com Impressão Profissional" style="color:#f6631d; text-decoration:none;">papelaria personalizada</a></strong>, brindes e comunicação visual — com entrega rápida para {cidade} e para todo o Brasil, independente do tamanho do seu pedido.
</p>

<!-- BOX DESTAQUE — FIXO -->
<div style="background:#fff7f3; border-left:4px solid #f6631d; border-radius:0 10px 10px 0; padding:20px 24px; margin:0 0 32px;">
    <p style="font-family:'Montserrat',Arial,sans-serif; font-size:0.88rem; font-weight:700; color:#f6631d; margin:0 0 8px; text-transform:uppercase; letter-spacing:1px;">Por que escolher a ExpanSSiva para sua empresa em {cidade}?</p>
    <div style="display:flex; flex-wrap:wrap; gap:10px;">
        <span style="font-family:'Montserrat',Arial,sans-serif; font-size:0.8rem; color:#444; background:#fff; border:1px solid #fde0d0; padding:5px 12px; border-radius:20px;">🏭 Produção industrial</span>
        <span style="font-family:'Montserrat',Arial,sans-serif; font-size:0.8rem; color:#444; background:#fff; border:1px solid #fde0d0; padding:5px 12px; border-radius:20px;">🚀 Entrega rápida</span>
        <span style="font-family:'Montserrat',Arial,sans-serif; font-size:0.8rem; color:#444; background:#fff; border:1px solid #fde0d0; padding:5px 12px; border-radius:20px;">💰 Melhor preço</span>
        <span style="font-family:'Montserrat',Arial,sans-serif; font-size:0.8rem; color:#444; background:#fff; border:1px solid #fde0d0; padding:5px 12px; border-radius:20px;">🎨 Suporte criativo</span>
        <span style="font-family:'Montserrat',Arial,sans-serif; font-size:0.8rem; color:#444; background:#fff; border:1px solid #fde0d0; padding:5px 12px; border-radius:20px;">📦 Pequenas e grandes tiragens</span>
    </div>
</div>

<!-- ##BLOCO_VAR_1## -->
<p style="font-family:'Montserrat',Arial,sans-serif; font-size:0.95rem; color:#555; line-height:1.8; margin:0 0 28px;">
{bloco_1}
</p>
		
<h3 style="font-family:'Montserrat',Arial,sans-serif; font-size:1.1rem; font-weight:700; color:#222; margin:0 0 20px; border-left:4px solid #f6631d; padding-left:12px;">
    O Que Produzimos para Empresas em {cidade}
</h3>

<div style="display:grid; grid-template-columns:repeat(auto-fit,minmax(240px,1fr)); gap:16px; margin:0 0 32px;">
    <div style="background:#ffffff; border:1px solid #ebebeb; border-radius:12px; padding:20px; border-top:3px solid #f6631d;">
        <p style="font-family:'Montserrat',Arial,sans-serif; font-size:1.5rem; margin:0 0 8px;">📄</p>
        <h4 style="font-family:'Montserrat',Arial,sans-serif; font-size:0.95rem; font-weight:700; color:#222; margin:0 0 8px;">Papelaria Corporativa</h4>
        <p style="font-family:'Montserrat',Arial,sans-serif; font-size:0.82rem; color:#666; line-height:1.6; margin:0;">Cartões de visita, papel timbrado, pastas, envelopes e blocos — com acabamentos especiais como laminação fosca e verniz localizado que transmitem autoridade.</p>
    </div>
    <div style="background:#ffffff; border:1px solid #ebebeb; border-radius:12px; padding:20px; border-top:3px solid #f6631d;">
        <p style="font-family:'Montserrat',Arial,sans-serif; font-size:1.5rem; margin:0 0 8px;">🎁</p>
        <h4 style="font-family:'Montserrat',Arial,sans-serif; font-size:0.95rem; font-weight:700; color:#222; margin:0 0 8px;">Brindes Personalizados</h4>
        <p style="font-family:'Montserrat',Arial,sans-serif; font-size:0.82rem; color:#666; line-height:1.6; margin:0;">Canetas, garrafas, cadernos, canecas, chaveiros e kits corporativos — itens que transformam sua marca em presença constante no dia a dia dos clientes.</p>
    </div>
    <div style="background:#ffffff; border:1px solid #ebebeb; border-radius:12px; padding:20px; border-top:3px solid #f6631d;">
        <p style="font-family:'Montserrat',Arial,sans-serif; font-size:1.5rem; margin:0 0 8px;">📢</p>
        <h4 style="font-family:'Montserrat',Arial,sans-serif; font-size:0.95rem; font-weight:700; color:#222; margin:0 0 8px;">Comunicação Visual</h4>
        <p style="font-family:'Montserrat',Arial,sans-serif; font-size:0.82rem; color:#666; line-height:1.6; margin:0;">Banners, faixas, adesivos, placas e displays — materiais de alto impacto para pontos de venda, eventos e ambientes corporativos.</p>
    </div>
    <div style="background:#ffffff; border:1px solid #ebebeb; border-radius:12px; padding:20px; border-top:3px solid #f6631d;">
        <p style="font-family:'Montserrat',Arial,sans-serif; font-size:1.5rem; margin:0 0 8px;">📖</p>
        <h4 style="font-family:'Montserrat',Arial,sans-serif; font-size:0.95rem; font-weight:700; color:#222; margin:0 0 8px;">Catálogos e Revistas</h4>
        <p style="font-family:'Montserrat',Arial,sans-serif; font-size:0.82rem; color:#666; line-height:1.6; margin:0;">Materiais editoriais de alto padrão para apresentar produtos, serviços e a identidade da sua marca com sofisticação e credibilidade.</p>
    </div>
    <div style="background:#ffffff; border:1px solid #ebebeb; border-radius:12px; padding:20px; border-top:3px solid #f6631d;">
        <p style="font-family:'Montserrat',Arial,sans-serif; font-size:1.5rem; margin:0 0 8px;">🎟️</p>
        <h4 style="font-family:'Montserrat',Arial,sans-serif; font-size:0.95rem; font-weight:700; color:#222; margin:0 0 8px;">Credenciais e Eventos</h4>
        <p style="font-family:'Montserrat',Arial,sans-serif; font-size:0.82rem; color:#666; line-height:1.6; margin:0;">Credenciais, cordões, crachás e materiais de identificação para eventos corporativos, feiras e congressos com entrega no prazo certo.</p>
    </div>
    <div style="background:#ffffff; border:1px solid #ebebeb; border-radius:12px; padding:20px; border-top:3px solid #f6631d;">
        <p style="font-family:'Montserrat',Arial,sans-serif; font-size:1.5rem; margin:0 0 8px;">📦</p>
        <h4 style="font-family:'Montserrat',Arial,sans-serif; font-size:0.95rem; font-weight:700; color:#222; margin:0 0 8px;">Embalagens e Rótulos</h4>
        <p style="font-family:'Montserrat',Arial,sans-serif; font-size:0.82rem; color:#666; line-height:1.6; margin:0;">Rótulos adesivos, etiquetas e embalagens personalizadas que valorizam o produto e fortalecem a identidade visual da marca no ponto de venda.</p>
    </div>
</div>

<!-- ##BLOCO_VAR_2## -->
<p style="font-family:'Montserrat',Arial,sans-serif; font-size:0.95rem; color:#555; line-height:1.8; margin:0 0 28px;">
{bloco_2}
</p>
		
<h3 style="font-family:'Montserrat',Arial,sans-serif; font-size:1.1rem; font-weight:700; color:#222; margin:0 0 12px; border-left:4px solid #f6631d; padding-left:12px;">
    Logística e Consultoria para {cidade}
</h3>

<p style="font-family:'Montserrat',Arial,sans-serif; font-size:0.92rem; color:#555; line-height:1.8; margin:0 0 28px;">
Nossa plataforma não funciona apenas como um balcão de pedidos — é um <strong style="color:#222;">parceiro estratégico</strong> para empresas em {cidade}. Ao escolher a ExpanSSiva, você elimina intermediários e acessa um fluxo de produção industrial de alta performance, com preços competitivos e logística otimizada para entrega rápida em qualquer região.
<br><br>
Todos os pedidos são acompanhados por um <strong style="color:#222;">consultor técnico exclusivo</strong> — da conferência do arquivo à expedição. Esse suporte especializado garante que cada detalhe do seu material seja produzido com precisão, seja para itens de papelaria corporativa ou para a linha completa de <strong><a href="/brindes-personalizados" title="Brindes Personalizados para Empresas com Alta Qualidade" style="color:#f6631d; text-decoration:none;">brindes personalizados</a></strong>. Você pode realizar simulações de prazos e valores diretamente no site, com resposta instantânea para apoiar decisões rápidas e sem comprometer o seu prazo.
</p>

<h3 style="font-family:'Montserrat',Arial,sans-serif; font-size:1.1rem; font-weight:700; color:#222; margin:0 0 12px; border-left:4px solid #f6631d; padding-left:12px;">
    Por Que a ExpanSSiva
</h3>

<p style="font-family:'Montserrat',Arial,sans-serif; font-size:0.92rem; color:#555; line-height:1.8; margin:0 0 28px;">
<strong style="color:#222;">Milhares de clientes atendidos</strong> em todo o Brasil — de pequenos empreendedores a grandes corporações.
<br><br>
<strong style="color:#222;">Pequenas e grandes tiragens</strong> — flexibilidade total para qualquer demanda.
<br><br>
<strong style="color:#222;">Suporte técnico no arquivo</strong> — nossa equipe confere cada arte antes de produzir.
<br><br>
<strong style="color:#222;">Prova digital antes da produção</strong> — aprovação garantida antes de qualquer impressão.
<br><br>
<strong style="color:#222;">Simulação online instantânea</strong> — insira seu CEP e veja valores de produção e entrega em tempo real.
</p>

<!-- BOX PROCESSO — FIXO -->
<div style="background:#f4f4f4; border-radius:12px; padding:24px; margin:0 0 32px;">
    <p style="font-family:'Montserrat',Arial,sans-serif; font-size:0.75rem; font-weight:700; letter-spacing:2px; text-transform:uppercase; color:#f6631d; margin:0 0 16px;">Como funciona o processo</p>
    <div style="display:grid; grid-template-columns:repeat(auto-fit,minmax(160px,1fr)); gap:16px;">
        <div style="text-align:center;">
            <div style="width:36px; height:36px; background:#f6631d; border-radius:50%; display:flex; align-items:center; justify-content:center; margin:0 auto 8px;">
                <span style="color:#fff; font-family:'Montserrat',Arial,sans-serif; font-weight:800; font-size:0.85rem;">1</span>
            </div>
            <p style="font-family:'Montserrat',Arial,sans-serif; font-size:0.8rem; font-weight:700; color:#222; margin:0 0 4px;">Escolha o produto</p>
            <p style="font-family:'Montserrat',Arial,sans-serif; font-size:0.75rem; color:#666; margin:0; line-height:1.4;">Papelaria, brinde ou impresso</p>
        </div>
        <div style="text-align:center;">
            <div style="width:36px; height:36px; background:#f6631d; border-radius:50%; display:flex; align-items:center; justify-content:center; margin:0 auto 8px;">
                <span style="color:#fff; font-family:'Montserrat',Arial,sans-serif; font-weight:800; font-size:0.85rem;">2</span>
            </div>
            <p style="font-family:'Montserrat',Arial,sans-serif; font-size:0.8rem; font-weight:700; color:#222; margin:0 0 4px;">Envie sua arte</p>
            <p style="font-family:'Montserrat',Arial,sans-serif; font-size:0.75rem; color:#666; margin:0; line-height:1.4;">Ou criamos para você</p>
        </div>
        <div style="text-align:center;">
            <div style="width:36px; height:36px; background:#f6631d; border-radius:50%; display:flex; align-items:center; justify-content:center; margin:0 auto 8px;">
                <span style="color:#fff; font-family:'Montserrat',Arial,sans-serif; font-weight:800; font-size:0.85rem;">3</span>
            </div>
            <p style="font-family:'Montserrat',Arial,sans-serif; font-size:0.8rem; font-weight:700; color:#222; margin:0 0 4px;">Aprove a prova</p>
            <p style="font-family:'Montserrat',Arial,sans-serif; font-size:0.75rem; color:#666; margin:0; line-height:1.4;">Prova digital antes de produzir</p>
        </div>
        <div style="text-align:center;">
            <div style="width:36px; height:36px; background:#f6631d; border-radius:50%; display:flex; align-items:center; justify-content:center; margin:0 auto 8px;">
                <span style="color:#fff; font-family:'Montserrat',Arial,sans-serif; font-weight:800; font-size:0.85rem;">4</span>
            </div>
            <p style="font-family:'Montserrat',Arial,sans-serif; font-size:0.8rem; font-weight:700; color:#222; margin:0 0 4px;">Receba seu pedido</p>
            <p style="font-family:'Montserrat',Arial,sans-serif; font-size:0.75rem; color:#666; margin:0; line-height:1.4;">Entrega rápida para todo o Brasil</p>
        </div>
    </div>
</div>

<!-- FAQ — FIXO -->
<h3 style="font-family:'Montserrat',Arial,sans-serif; font-size:1.1rem; font-weight:700; color:#222; margin:0 0 20px; border-left:4px solid #f6631d; padding-left:12px;">
    Perguntas Frequentes
</h3>

<p style="font-family:'Montserrat',Arial,sans-serif; font-size:0.92rem; color:#555; line-height:1.8; margin:0 0 16px;">
    <strong style="color:#222;">A ExpanSSiva atende empresas em {cidade} mesmo sem ter sede lá?</strong><br>
    Sim. Somos uma gráfica online com produção centralizada e logística nacional — atendemos empresas em todo o Brasil com a mesma qualidade, prazo e suporte independente da localização.
</p>
<p style="font-family:'Montserrat',Arial,sans-serif; font-size:0.92rem; color:#555; line-height:1.8; margin:0 0 16px;">
    <strong style="color:#222;">Qual o prazo de entrega para {cidade}?</strong><br>
    A maioria dos pedidos é despachada em até 5 dias úteis após aprovação da prova digital. O prazo final depende da modalidade de frete escolhida no momento do pedido.
</p>
<p style="font-family:'Montserrat',Arial,sans-serif; font-size:0.92rem; color:#555; line-height:1.8; margin:0 0 16px;">
    <strong style="color:#222;">Posso pedir papelaria e brindes no mesmo pedido?</strong><br>
    Sim. Nossa plataforma permite combinar diferentes produtos no mesmo pedido — com simulação de frete unificada e acompanhamento centralizado de todas as etapas.
</p>
<p style="font-family:'Montserrat',Arial,sans-serif; font-size:0.92rem; color:#555; line-height:1.8; margin:0 0 16px;">
    <strong style="color:#222;">Vocês criam a arte se eu não tiver um designer?</strong><br>
    Sim. Nossa equipe criativa desenvolve layouts exclusivos para qualquer produto — papelaria, brindes, materiais de comunicação visual ou impressos editoriais.
</p>
<p style="font-family:'Montserrat',Arial,sans-serif; font-size:0.92rem; color:#555; line-height:1.8; margin:0 0 28px;">
    <strong style="color:#222;">Como simulo o preço e prazo de entrega para {cidade}?</strong><br>
    Na página de cada produto clique em simular preço, configure o pedido e insira seu CEP — você recebe valores de produção e entrega em tempo real, sem compromisso.
</p>

<!-- ##BLOCO_VAR_3## -->
		<p style="font-family:'Montserrat',Arial,sans-serif; font-size:0.95rem; color:#555; line-height:1.8; margin:0 0 28px;">
{bloco_3}
</p>
<!-- CTA FINAL — FIXO -->
<div style="background:#1a1a1a; border-radius:12px; padding:28px 24px; text-align:center; margin:0 0 8px;">
    <p style="font-family:'Montserrat',Arial,sans-serif; font-size:0.7rem; font-weight:700; letter-spacing:2.5px; text-transform:uppercase; color:#f6631d; margin:0 0 8px;">Pronto para começar?</p>
    <h3 style="font-family:'Montserrat',Arial,sans-serif; font-size:1.2rem; font-weight:800; color:#ffffff; margin:0 0 6px;">Simule agora o preço do seu pedido com Entrega em {cidade}</h3>
    <p style="font-family:'Montserrat',Arial,sans-serif; font-size:0.85rem; color:rgba(255,255,255,0.55); margin:0 0 20px;">Sem compromisso. Preço na hora. Entrega garantida em {cidade}.</p>
    <a href="/brindes-personalizados" style="display:inline-flex; align-items:center; gap:8px; background:#f6631d; color:#fff; font-family:'Montserrat',Arial,sans-serif; font-size:0.88rem; font-weight:700; padding:12px 28px; border-radius:8px; text-decoration:none;">
        Ver todos os Produtos →
    </a>
</div>
</article>
	
	
	<x-page id="3952"/>
</div>

<!--COMENTÁRIOS DE CLIENTES-->
<x-page id="25"/>
<br/>
"""

    # colar código
    pc.copy(cod_pagina)
    pa.hotkey("ctrl", "v")

    # scroll
    pa.click(x=1717, y=534)
    pa.press("down", presses=70)

    # SEO dinâmico
    title = f"Gráfica em {cidade} com Impressão Rápida e Alta Qualidade"
    keywords = f"gráfica em {cidade}, gráfica {cidade} rj, gráfica rápida {cidade}, impressão digital {cidade}, brindes personalizados {cidade}, gráfica online {cidade}, serviços gráficos {cidade}, impressão de alta qualidade {cidade}, gráfica para empresas {cidade}"
    description = f"Precisa de gráfica em {cidade}? Impressos com alta qualidade, produção rápida e atendimento ágil. Solicite seu orçamento agora mesmo! ⚡"

    # preencher campos
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

    # salvar
    pa.press("f3")
    sleep(1)
    pa.hotkey("ctrl", "w")

    print(f"Página da cidade {cidade} alterada com sucesso!")