"""
Automação de edição em massa de páginas no painel administrativo.

Este script utiliza PyAutoGUI para automatizar o processo de criação e atualização
de páginas em um sistema web, substituindo completamente o conteúdo HTML com base
em dados estruturados (JSON).

A automação percorre uma lista de cidades e, para cada uma:
- Abre uma nova aba no navegador e acessa o painel administrativo
- Pesquisa automaticamente pelo termo (produto + cidade)
- Localiza e acessa a página correspondente para edição
- Substitui todo o conteúdo HTML por um template dinâmico
- Injeta variáveis personalizadas (cidade + blocos de texto exclusivos)
- Preenche automaticamente campos de SEO (title, keywords e description)
- Salva a página e fecha a aba

O template HTML é padronizado, porém enriquecido com conteúdo dinâmico,
incluindo seções institucionais, SEO local, FAQ e blocos variáveis para
evitar repetição e melhorar indexação orgânica.

Objetivo:
Automatizar a geração e manutenção em larga escala de páginas locais,
reduzindo trabalho manual, aumentando consistência e otimizando SEO
para múltiplas localidades.
"""

#IMPORTS
import pyautogui as pa
import pyperclip as pc
from time import sleep
import json

# VARIAVEIS
webpage = "https://expanssiva.com.br/admin#/pages"
produto_busca = "Panfletos em "
pa.PAUSE = 0.4
cidades_encontradas = 0
cidades_nao_encontradas = 0
cidades_encontradas_list = []
cidades_nao_encontradas_list = []


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
    sleep(1.7)

    # pesquisar cidade
    pc.copy(produto_busca + cidade)
    pa.hotkey("ctrl", "v")
    pa.press("enter")
    sleep(1)

    try:
        # clicar editar
        caminho_img_editar = r"Y:\DESIGNS\Guilherme_link\VSCODE\Automacoes_em_py\auto_alterar_paginas_existentes\imgs\editar.png"
        pa.click(pa.locateCenterOnScreen(caminho_img_editar, confidence=0.9))
        pa.moveTo(x=100, y=100)
        sleep(1)
        cidades_encontradas += 1
        cidades_encontradas_list.append(cidade)

    except:
        print(f"Página para {cidade} não encontrada.")
        cidades_nao_encontradas += 1
        cidades_nao_encontradas_list.append(cidade)
        pa.hotkey("ctrl", "w")
        continue

    # selecionar tudo
    pa.press("tab", presses=3)
    pa.hotkey("ctrl", "a")

    # TEMPLATE DINÂMICO
    cod_pagina = f"""
    <!--Topo-->
<x-page id="3211" />

<!--Conteudo variado 1-->
<div style="text-align:center; padding: 9px;">
    <h1 style="font-size: clamp(18px, 5vw, 26px); margin: 0 0 4px;">
     Panfletos Personalizados com Entrega Rápida em {cidade}
    </h1>

    <p style="color:#6b6b6b; font-size:1rem; line-height:1.3;">
Material que chega na mão do seu cliente — digital ou offset, em qualquer tiragem. </p>
</div>

<!--Conteúdo 1-->
<x-page id="3212" />

<!--TEXTO SEO-->
<div class="container" style="padding:20px 16px;">
<article itemscope itemtype="https://schema.org/Article">

<h2 style="font-family:'Montserrat',Arial,sans-serif; font-size:clamp(1.2rem,3vw,1.6rem); font-weight:800; color:#222; margin:0 0 16px; line-height:1.3;">
    <strong>Panfletos Personalizados</strong> com Entrega em <strong>{cidade}</strong>: Material que Chega na Mão do Seu Cliente
</h2>

<p style="font-family:'Montserrat',Arial,sans-serif; font-size:0.95rem; color:#555; line-height:1.8; margin:0 0 28px;">
Panfletos continuam sendo uma das ferramentas de marketing local com melhor custo por impacto — distribuídos em pontos estratégicos, chegam diretamente nas mãos de quem pode se tornar seu próximo cliente. 
<br>
	Milhares de empresas já escolheram a ExpanSSiva para produzir panfletos de alto padrão, com entrega rápida em <strong style="color:#222;">{cidade}</strong> e em todo o Brasil.
</p>

<!-- BOX DESTAQUE — FIXO -->
<div style="background:#fff7f3; border-left:4px solid #f6631d; border-radius:0 10px 10px 0; padding:20px 24px; margin:0 0 32px;">
    <p style="font-family:'Montserrat',Arial,sans-serif; font-size:0.88rem; font-weight:700; color:#f6631d; margin:0 0 8px; text-transform:uppercase; letter-spacing:1px;">Por que panfletos ainda funcionam?</p>
    <div style="display:flex; flex-wrap:wrap; gap:10px;">
        <span style="font-family:'Montserrat',Arial,sans-serif; font-size:0.8rem; color:#444; background:#fff; border:1px solid #fde0d0; padding:5px 12px; border-radius:20px;">✋ Material tátil e memorável</span>
        <span style="font-family:'Montserrat',Arial,sans-serif; font-size:0.8rem; color:#444; background:#fff; border:1px solid #fde0d0; padding:5px 12px; border-radius:20px;">💰 Baixo custo por impacto</span>
        <span style="font-family:'Montserrat',Arial,sans-serif; font-size:0.8rem; color:#444; background:#fff; border:1px solid #fde0d0; padding:5px 12px; border-radius:20px;">🎯 Segmentação local eficaz</span>
        <span style="font-family:'Montserrat',Arial,sans-serif; font-size:0.8rem; color:#444; background:#fff; border:1px solid #fde0d0; padding:5px 12px; border-radius:20px;">🖨️ Digital e offset disponível</span>
        <span style="font-family:'Montserrat',Arial,sans-serif; font-size:0.8rem; color:#444; background:#fff; border:1px solid #fde0d0; padding:5px 12px; border-radius:20px;">🔄 Pequenas e grandes tiragens</span>
    </div>
</div>

<!-- ##BLOCO_VAR_1## -->
<p style="font-family:'Montserrat',Arial,sans-serif; font-size:0.95rem; color:#555; line-height:1.8; margin:0 0 28px;">
{bloco_1}
</p>

<h3 style="font-family:'Montserrat',Arial,sans-serif; font-size:1.1rem; font-weight:700; color:#222; margin:0 0 20px; border-left:4px solid #f6631d; padding-left:12px;">
    Tamanhos e Papéis Disponíveis
</h3>

<table style="width:100%; border-collapse:collapse; font-size:15px; margin:0 0 32px;">
    <tr style="background:#f6631d; color:#fff;">
        <th style="padding:10px; text-align:left; font-family:'Montserrat',Arial,sans-serif;">Papel</th>
        <th style="padding:10px; text-align:left; font-family:'Montserrat',Arial,sans-serif;">Gramatura</th>
        <th style="padding:10px; text-align:left; font-family:'Montserrat',Arial,sans-serif;">Ideal para</th>
    </tr>
    <tr style="background:#f9f9f9;">
        <td style="padding:10px; font-family:'Montserrat',Arial,sans-serif;"><strong>Couchê</strong></td>
        <td style="padding:10px; font-family:'Montserrat',Arial,sans-serif; font-size:0.85rem; color:#555;">90g e 120g</td>
        <td style="padding:10px; font-family:'Montserrat',Arial,sans-serif; font-size:0.85rem; color:#555;">Distribuição em massa</td>
    </tr>
    <tr>
        <td style="padding:10px; font-family:'Montserrat',Arial,sans-serif;"><strong>Couchê Premium</strong></td>
        <td style="padding:10px; font-family:'Montserrat',Arial,sans-serif; font-size:0.85rem; color:#555;">150g e 170g</td>
        <td style="padding:10px; font-family:'Montserrat',Arial,sans-serif; font-size:0.85rem; color:#555;">Material de alto impacto</td>
    </tr>
    <tr style="background:#f9f9f9;">
        <td style="padding:10px; font-family:'Montserrat',Arial,sans-serif;"><strong>Com Laminação</strong></td>
        <td style="padding:10px; font-family:'Montserrat',Arial,sans-serif; font-size:0.85rem; color:#555;">Brilho ou fosco</td>
        <td style="padding:10px; font-family:'Montserrat',Arial,sans-serif; font-size:0.85rem; color:#555;">Acabamento premium</td>
    </tr>
    <tr>
        <td style="padding:10px; font-family:'Montserrat',Arial,sans-serif;"><strong>Sulfite</strong></td>
        <td style="padding:10px; font-family:'Montserrat',Arial,sans-serif; font-size:0.85rem; color:#555;">75g e 90g</td>
        <td style="padding:10px; font-family:'Montserrat',Arial,sans-serif; font-size:0.85rem; color:#555;">Econômico e funcional</td>
    </tr>
    <tr style="background:#f9f9f9;">
        <td style="padding:10px; font-family:'Montserrat',Arial,sans-serif;"><strong>Reciclado</strong></td>
        <td style="padding:10px; font-family:'Montserrat',Arial,sans-serif; font-size:0.85rem; color:#555;">90g</td>
        <td style="padding:10px; font-family:'Montserrat',Arial,sans-serif; font-size:0.85rem; color:#555;">Marcas sustentáveis</td>
    </tr>
</table>

<h3 style="font-family:'Montserrat',Arial,sans-serif; font-size:1.1rem; font-weight:700; color:#222; margin:0 0 20px; border-left:4px solid #f6631d; padding-left:12px;">
    Perfis de Impressão
</h3>

<div style="display:grid; grid-template-columns:repeat(auto-fit,minmax(240px,1fr)); gap:16px; margin:0 0 32px;">
    <div style="background:#ffffff; border:1px solid #ebebeb; border-radius:12px; padding:20px; border-top:3px solid #f6631d;">
        <p style="font-family:'Montserrat',Arial,sans-serif; font-size:1.5rem; margin:0 0 8px;">⚡</p>
        <h4 style="font-family:'Montserrat',Arial,sans-serif; font-size:0.95rem; font-weight:700; color:#222; margin:0 0 8px;">Impressão Digital</h4>
        <p style="font-family:'Montserrat',Arial,sans-serif; font-size:0.82rem; color:#666; line-height:1.6; margin:0;">Ideal para até 1.000 unidades — entrega ultra rápida sem comprometer qualidade. Perfeito para campanhas relâmpago e promoções pontuais.</p>
    </div>
    <div style="background:#ffffff; border:1px solid #ebebeb; border-radius:12px; padding:20px; border-top:3px solid #f6631d;">
        <p style="font-family:'Montserrat',Arial,sans-serif; font-size:1.5rem; margin:0 0 8px;">🏭</p>
        <h4 style="font-family:'Montserrat',Arial,sans-serif; font-size:0.95rem; font-weight:700; color:#222; margin:0 0 8px;">Impressão Offset</h4>
        <p style="font-family:'Montserrat',Arial,sans-serif; font-size:0.82rem; color:#666; line-height:1.6; margin:0;">Para acima de 1.000 unidades — custo por unidade muito mais baixo com qualidade superior. Ideal para distribuição em larga escala.</p>
    </div>
</div>

<!-- ##BLOCO_VAR_2## -->
<p style="font-family:'Montserrat',Arial,sans-serif; font-size:0.95rem; color:#555; line-height:1.8; margin:0 0 28px;">
{bloco_2}
</p>

<h3 style="font-family:'Montserrat',Arial,sans-serif; font-size:1.1rem; font-weight:700; color:#222; margin:0 0 20px; border-left:4px solid #f6631d; padding-left:12px;">
    Para Quem São os Panfletos
</h3>

<div style="display:grid; grid-template-columns:repeat(auto-fit,minmax(240px,1fr)); gap:16px; margin:0 0 32px;">
    <div style="background:#ffffff; border:1px solid #ebebeb; border-radius:12px; padding:20px; border-top:3px solid #f6631d;">
        <p style="font-family:'Montserrat',Arial,sans-serif; font-size:1.5rem; margin:0 0 8px;">🏪</p>
        <h4 style="font-family:'Montserrat',Arial,sans-serif; font-size:0.95rem; font-weight:700; color:#222; margin:0 0 8px;">Comércio Local</h4>
        <p style="font-family:'Montserrat',Arial,sans-serif; font-size:0.82rem; color:#666; line-height:1.6; margin:0;">Restaurantes, lojas, mercados e prestadores de serviço — panfletos que chegam direto no bairro do cliente.</p>
    </div>
    <div style="background:#ffffff; border:1px solid #ebebeb; border-radius:12px; padding:20px; border-top:3px solid #f6631d;">
        <p style="font-family:'Montserrat',Arial,sans-serif; font-size:1.5rem; margin:0 0 8px;">💇</p>
        <h4 style="font-family:'Montserrat',Arial,sans-serif; font-size:0.95rem; font-weight:700; color:#222; margin:0 0 8px;">Serviços e Beleza</h4>
        <p style="font-family:'Montserrat',Arial,sans-serif; font-size:0.82rem; color:#666; line-height:1.6; margin:0;">Cabeleireiros, manicures, clínicas e estúdios — panfletos que constroem presença local e atraem novos clientes.</p>
    </div>
    <div style="background:#ffffff; border:1px solid #ebebeb; border-radius:12px; padding:20px; border-top:3px solid #f6631d;">
        <p style="font-family:'Montserrat',Arial,sans-serif; font-size:1.5rem; margin:0 0 8px;">🎪</p>
        <h4 style="font-family:'Montserrat',Arial,sans-serif; font-size:0.95rem; font-weight:700; color:#222; margin:0 0 8px;">Eventos e Promoções</h4>
        <p style="font-family:'Montserrat',Arial,sans-serif; font-size:0.82rem; color:#666; line-height:1.6; margin:0;">Lançamentos, inaugurações, liquidações e campanhas sazonais — material impresso que reforça a ação digital.</p>
    </div>
    <div style="background:#ffffff; border:1px solid #ebebeb; border-radius:12px; padding:20px; border-top:3px solid #f6631d;">
        <p style="font-family:'Montserrat',Arial,sans-serif; font-size:1.5rem; margin:0 0 8px;">🏫</p>
        <h4 style="font-family:'Montserrat',Arial,sans-serif; font-size:0.95rem; font-weight:700; color:#222; margin:0 0 8px;">Educação e Cursos</h4>
        <p style="font-family:'Montserrat',Arial,sans-serif; font-size:0.82rem; color:#666; line-height:1.6; margin:0;">Escolas, cursos livres, faculdades e treinamentos — panfletos que comunicam diferenciais e atraem matrículas.</p>
    </div>
</div>

<h3 style="font-family:'Montserrat',Arial,sans-serif; font-size:1.1rem; font-weight:700; color:#222; margin:0 0 12px; border-left:4px solid #f6631d; padding-left:12px;">
    Arte e Personalização
</h3>

<p style="font-family:'Montserrat',Arial,sans-serif; font-size:0.92rem; color:#555; line-height:1.8; margin:0 0 28px;">
Envie sua arte pronta ou conte com nossa equipe de design para criar um layout que maximize o impacto visual do seu material. Trabalhamos com as melhores práticas de hierarquia visual, cores e CTA para garantir que seu panfleto realmente converta.
<br><br>
Nossa equipe de pré-impressão confere cada arquivo antes de produzir — e sempre enviamos uma <strong style="color:#222;">prova digital para aprovação</strong> antes de iniciar a impressão.
</p>

<h3 style="font-family:'Montserrat',Arial,sans-serif; font-size:1.1rem; font-weight:700; color:#222; margin:0 0 12px; border-left:4px solid #f6631d; padding-left:12px;">
    Por Que a ExpanSSiva
</h3>

<p style="font-family:'Montserrat',Arial,sans-serif; font-size:0.92rem; color:#555; line-height:1.8; margin:0 0 28px;">
<strong style="color:#222;">Milhares de clientes atendidos</strong> em todo o Brasil — de pequenos comércios a grandes redes.
<br><br>
<strong style="color:#222;">Impressão digital e offset</strong> — tecnologia adequada para cada volume e prazo.
<br><br>
<strong style="color:#222;">Pequenas e grandes tiragens</strong> — demanda ajustada à sua necessidade.
<br><br>
<strong style="color:#222;">Suporte técnico no arquivo</strong> — nossa equipe confere cada arte antes de produzir.
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
            <p style="font-family:'Montserrat',Arial,sans-serif; font-size:0.8rem; font-weight:700; color:#222; margin:0 0 4px;">Configure o pedido</p>
            <p style="font-family:'Montserrat',Arial,sans-serif; font-size:0.75rem; color:#666; margin:0; line-height:1.4;">Tamanho, papel e quantidade</p>
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
    <strong style="color:#222;">Qual a quantidade mínima para panfletos?</strong><br>
    A demanda é ajustada à sua necessidade — de pequenas tiragens para testes até grandes volumes para distribuição em massa. Consulte a página do produto para verificar a disponibilidade.
</p>
<p style="font-family:'Montserrat',Arial,sans-serif; font-size:0.92rem; color:#555; line-height:1.8; margin:0 0 16px;">
    <strong style="color:#222;">Qual o prazo de entrega para {cidade}?</strong><br>
    A maioria dos pedidos é despachada em até 5 dias úteis após aprovação da prova digital. O prazo final depende da modalidade de frete escolhida.
</p>
<p style="font-family:'Montserrat',Arial,sans-serif; font-size:0.92rem; color:#555; line-height:1.8; margin:0 0 16px;">
    <strong style="color:#222;">Qual a diferença entre impressão digital e offset?</strong><br>
    A digital é mais ágil e indicada para até 1.000 unidades. O offset é mais econômico por unidade para volumes acima de 1.000 — ideal para campanhas de grande escala.
</p>
<p style="font-family:'Montserrat',Arial,sans-serif; font-size:0.92rem; color:#555; line-height:1.8; margin:0 0 16px;">
    <strong style="color:#222;">Qual papel é mais indicado para panfletos?</strong><br>
    O couchê 115g é o mais popular — equilíbrio entre resistência e custo. Para material premium recomendamos couchê 150g com laminação fosca ou brilho.
</p>
<p style="font-family:'Montserrat',Arial,sans-serif; font-size:0.92rem; color:#555; line-height:1.8; margin:0 0 28px;">
    <strong style="color:#222;">Quais tamanhos estão disponíveis?</strong><br>
    Os tamanhos mais populares são 10x15 cm e 15x21 cm (A5). Também produzimos em formatos personalizados — consulte nossa equipe para projetos com dimensões especiais.
</p>

<!-- ##BLOCO_VAR_3## -->
<p style="font-family:'Montserrat',Arial,sans-serif; font-size:0.95rem; color:#555; line-height:1.8; margin:0 0 28px;">
{bloco_3}
</p>

<!-- CTA FINAL — FIXO -->
<div style="background:#1a1a1a; border-radius:12px; padding:28px 24px; text-align:center; margin:0 0 8px;">
    <p style="font-family:'Montserrat',Arial,sans-serif; font-size:0.7rem; font-weight:700; letter-spacing:2.5px; text-transform:uppercase; color:#f6631d; margin:0 0 8px;">Pronto para começar?</p>
    <h3 style="font-family:'Montserrat',Arial,sans-serif; font-size:1.2rem; font-weight:800; color:#ffffff; margin:0 0 6px;">Simule agora o preço dos seus Panfletos com Entrega em {cidade}</h3>
    <p style="font-family:'Montserrat',Arial,sans-serif; font-size:0.85rem; color:rgba(255,255,255,0.55); margin:0 0 20px;">Sem compromisso. Preço na hora. Entrega garantida em {cidade}.</p>
    <a href="/categoria/panfletos" style="display:inline-flex; align-items:center; gap:8px; background:#f6631d; color:#fff; font-family:'Montserrat',Arial,sans-serif; font-size:0.88rem; font-weight:700; padding:12px 28px; border-radius:8px; text-decoration:none;">
        Ver todos os Panfletos →
    </a>
</div>

</article>
</div>


<!--COMENTÁRIOS DE CLIENTES-->
<x-page id="3213"/>
<br/>
"""

    # colar código
    pc.copy(cod_pagina)
    pa.hotkey("ctrl", "v")

    # scroll
    pa.click(x=1717, y=534)
    pa.press("down", presses=70)

    # SEO dinâmico
    title = f"Panfletos Personalizados com Entrega Rápida em {cidade}"
    keywords = f"panfleto personalizado {cidade}, impressão de panfleto {cidade}, panfleto couchê {cidade}, panfleto offset {cidade}, panfleto digital {cidade}, gráfica panfleto {cidade}"
    description = f"🚀 Panfletos personalizados com entrega rápida em {cidade}. Couchê 120g a 170g, digital ou offset — 10x15 cm, A5 e formatos especiais. Demanda ajustada à sua necessidade. Peça agora!"

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

print(f"Cidades encontradas: {cidades_encontradas}")
print("Cidades encontradas:", cidades_encontradas_list)

print(f"Cidades não encontradas: {cidades_nao_encontradas}")
print("Cidades não encontradas:", cidades_nao_encontradas_list)