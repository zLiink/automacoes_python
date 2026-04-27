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
produto_busca = "Canetas Personalizadas em "
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
    pa.press("tab")
    pa.hotkey("ctrl", "a")

    # TEMPLATE DINÂMICO
    cod_pagina = f"""
    <!--Topo-->
<x-page id="4362" />

<!--Conteudo variado 1-->
<div style="text-align:center; padding: 9px;">
    <h1 style="font-size: clamp(18px, 5vw, 26px); margin: 0 0 4px;">
        Canetas Personalizadas com Entrega Rápida em {cidade}
    </h1>

    <p style="color:#6b6b6b; font-size:1rem; line-height:1.3;">
        Sua marca no brinde mais usado do dia a dia corporativo.
    </p>
</div>

<!--Conteúdo 1-->
<x-page id="4363" />

<!--TEXTO SEO-->
<div class="container" style="padding:20px 16px;">
<article itemscope itemtype="https://schema.org/Article">

    <!-- TÍTULO -->
    <h2 style="font-family:'Montserrat',Arial,sans-serif; font-size:clamp(1.2rem,3vw,1.6rem); font-weight:800; color:#222; margin:0 0 16px; line-height:1.3;">
        <strong>Canetas Personalizadas</strong> com Entrega em <strong>{cidade}</strong>
    </h2>

    <p style="font-family:'Montserrat',Arial,sans-serif; font-size:0.95rem; color:#555; line-height:1.8; margin:0 0 28px;">
        Milhares de empresas já escolheram a ExpanSSiva para transformar canetas em ferramentas de marca. Simples, úteis e sempre presentes no dia a dia — as <strong style="color:#222;">canetas personalizadas</strong> são um dos brindes corporativos com melhor custo-benefício do mercado, entregues rapidamente em <strong style="color:#222;">{cidade}</strong>.
    </p>

    <!-- ##BLOCO_VAR_1## -->
<p style="font-family:'Montserrat',Arial,sans-serif; font-size:0.95rem; color:#555; line-height:1.8; margin:0 0 28px;">
{bloco_1}
</p>

    <!-- BOX DESTAQUE -->
    <div style="display:flex; align-items:flex-start; gap:16px; background:#f4f4f4; border-left:4px solid #f6631d; border-radius:0 10px 10px 0; padding:20px 24px; margin:0 0 32px;">
        <div style="font-size:2rem; line-height:1; flex-shrink:0;">✏️</div>
        <div>
            <p style="font-family:'Montserrat',Arial,sans-serif; font-size:0.9rem; font-weight:700; color:#f6631d; margin:0 0 6px; text-transform:uppercase; letter-spacing:1px;">O brinde que todo mundo usa</p>
            <p style="font-family:'Montserrat',Arial,sans-serif; font-size:0.88rem; color:#555; line-height:1.7; margin:0;">
                Diferente de outros brindes que ficam guardados, a caneta é usada diariamente — no trabalho, em reuniões, em eventos. Cada uso é uma exposição da sua marca para novas pessoas. Combinada com um <a href="/categoria/cadernos-personalizados" style="color:#f6631d; font-weight:600;">caderno personalizado</a>, forma um kit promocional completo que reforça a identidade visual da sua empresa no dia a dia do cliente.
            </p>
        </div>
    </div>

    <!-- MODELOS -->
    <h3 style="font-family:'Montserrat',Arial,sans-serif; font-size:1.1rem; font-weight:700; color:#222; margin:0 0 16px; border-left:4px solid #f6631d; padding-left:12px;">
        Modelos Disponíveis
    </h3>

    <div style="display:grid; grid-template-columns:repeat(auto-fit,minmax(200px,1fr)); gap:12px; margin:0 0 32px;">

        <div style="background:#fff; border:1px solid #ebebeb; border-radius:12px; padding:18px 16px; border-top:3px solid #f6631d;">
            <p style="font-size:1.4rem; margin:0 0 8px;">🖊️</p>
            <p style="font-family:'Montserrat',Arial,sans-serif; font-size:0.88rem; font-weight:700; color:#222; margin:0 0 4px;">Caneta Clássica</p>
            <p style="font-family:'Montserrat',Arial,sans-serif; font-size:0.75rem; color:#888; margin:0 0 6px; line-height:1.4;">Brindes em massa com melhor custo-benefício</p>
            <span style="font-family:'Montserrat',Arial,sans-serif; font-size:0.65rem; font-weight:700; color:#f6631d; background:#fff7f3; padding:2px 8px; border-radius:20px;">Mais Popular</span>
        </div>

        <div style="background:#fff; border:1px solid #ebebeb; border-radius:12px; padding:18px 16px; border-top:3px solid #f6631d;">
            <p style="font-size:1.4rem; margin:0 0 8px;">🌿</p>
            <p style="font-family:'Montserrat',Arial,sans-serif; font-size:0.88rem; font-weight:700; color:#222; margin:0 0 4px;">Caneta Ecológica</p>
            <p style="font-family:'Montserrat',Arial,sans-serif; font-size:0.75rem; color:#888; margin:0 0 6px; line-height:1.4;">Material reciclado para marcas sustentáveis</p>
            <span style="font-family:'Montserrat',Arial,sans-serif; font-size:0.65rem; font-weight:700; color:#f6631d; background:#fff7f3; padding:2px 8px; border-radius:20px;">Sustentável</span>
        </div>

        <div style="background:#fff; border:1px solid #ebebeb; border-radius:12px; padding:18px 16px; border-top:3px solid #f6631d;">
            <p style="font-size:1.4rem; margin:0 0 8px;">💼</p>
            <p style="font-family:'Montserrat',Arial,sans-serif; font-size:0.88rem; font-weight:700; color:#222; margin:0 0 4px;">Caneta Executiva</p>
            <p style="font-family:'Montserrat',Arial,sans-serif; font-size:0.75rem; color:#888; margin:0 0 6px; line-height:1.4;">Acabamento sofisticado para brindes premium</p>
            <span style="font-family:'Montserrat',Arial,sans-serif; font-size:0.65rem; font-weight:700; color:#f6631d; background:#fff7f3; padding:2px 8px; border-radius:20px;">Premium</span>
        </div>

        <div style="background:#fff; border:1px solid #ebebeb; border-radius:12px; padding:18px 16px; border-top:3px solid #f6631d;">
            <p style="font-size:1.4rem; margin:0 0 8px;">🏷️</p>
            <p style="font-family:'Montserrat',Arial,sans-serif; font-size:0.88rem; font-weight:700; color:#222; margin:0 0 4px;">Caneta com Nome</p>
            <p style="font-family:'Montserrat',Arial,sans-serif; font-size:0.75rem; color:#888; margin:0 0 6px; line-height:1.4;">Nome e profissão para presente personalizado</p>
            <span style="font-family:'Montserrat',Arial,sans-serif; font-size:0.65rem; font-weight:700; color:#f6631d; background:#fff7f3; padding:2px 8px; border-radius:20px;">Exclusivo</span>
        </div>

        <div style="background:#fff; border:1px solid #ebebeb; border-radius:12px; padding:18px 16px; border-top:3px solid #f6631d;">
            <p style="font-size:1.4rem; margin:0 0 8px;">🎯</p>
            <p style="font-family:'Montserrat',Arial,sans-serif; font-size:0.88rem; font-weight:700; color:#222; margin:0 0 4px;">Caneta com Logo</p>
            <p style="font-family:'Montserrat',Arial,sans-serif; font-size:0.75rem; color:#888; margin:0 0 6px; line-height:1.4;">Identidade visual completa no brinde corporativo</p>
            <span style="font-family:'Montserrat',Arial,sans-serif; font-size:0.65rem; font-weight:700; color:#f6631d; background:#fff7f3; padding:2px 8px; border-radius:20px;">Corporativo</span>
        </div>

    </div>

    <!-- ##BLOCO_VAR_2## -->
<p style="font-family:'Montserrat',Arial,sans-serif; font-size:0.95rem; color:#555; line-height:1.8; margin:0 0 28px;">
{bloco_2}
</p>

    <!-- ARTE E PERSONALIZAÇÃO -->
    <h3 style="font-family:'Montserrat',Arial,sans-serif; font-size:1.1rem; font-weight:700; color:#222; margin:0 0 12px; border-left:4px solid #f6631d; padding-left:12px;">
        Arte e Personalização
    </h3>

    <p style="font-family:'Montserrat',Arial,sans-serif; font-size:0.92rem; color:#555; line-height:1.8; margin:0 0 12px;">
        Você pode enviar sua própria arte diretamente pelo site ou contar com nossa equipe de design para criar o layout ideal. Personalizamos com logo, nome, profissão ou mensagem — em pequenas ou grandes quantidades, sempre com qualidade e sem perder o custo-benefício.
    </p>

    <!-- AVISO IMPORTANTE -->
    <div style="display:flex; align-items:flex-start; gap:12px; background:#fffbf0; border:1px solid #fde68a; border-radius:10px; padding:16px 18px; margin:0 0 32px;">
        <span style="font-size:1.2rem; flex-shrink:0;">⚠️</span>
        <p style="font-family:'Montserrat',Arial,sans-serif; font-size:0.82rem; color:#555; line-height:1.6; margin:0;">
            <strong style="color:#222;">Atenção:</strong> antes de finalizar o pedido é essencial confirmar com nossos consultores a disponibilidade da cor escolhida, pois canetas são produtos de estoque dinâmico.
        </p>
    </div>

    <!-- POR QUE A EXPANSSIVA -->
    <h3 style="font-family:'Montserrat',Arial,sans-serif; font-size:1.1rem; font-weight:700; color:#222; margin:0 0 16px; border-left:4px solid #f6631d; padding-left:12px;">
        Por Que a ExpanSSiva
    </h3>

    <div style="display:grid; grid-template-columns:repeat(auto-fit,minmax(200px,1fr)); gap:10px; margin:0 0 32px;">
        <div style="display:flex; align-items:center; gap:12px; background:#f4f4f4; border-radius:10px; padding:14px 16px;">
            <span style="font-size:20px; flex-shrink:0;">🏆</span>
            <div>
                <p style="font-family:'Montserrat',Arial,sans-serif; font-size:0.78rem; font-weight:700; color:#222; margin:0 0 2px;">Referência Nacional</p>
                <p style="font-family:'Montserrat',Arial,sans-serif; font-size:0.67rem; color:#777; margin:0; line-height:1.3;">Milhares de clientes em todo o Brasil</p>
            </div>
        </div>
        <div style="display:flex; align-items:center; gap:12px; background:#f4f4f4; border-radius:10px; padding:14px 16px;">
            <span style="font-size:20px; flex-shrink:0;">📦</span>
            <div>
                <p style="font-family:'Montserrat',Arial,sans-serif; font-size:0.78rem; font-weight:700; color:#222; margin:0 0 2px;">Pequenas Quantidades</p>
                <p style="font-family:'Montserrat',Arial,sans-serif; font-size:0.67rem; color:#777; margin:0; line-height:1.3;">Personalize sem precisar de grandes volumes</p>
            </div>
        </div>
        <div style="display:flex; align-items:center; gap:12px; background:#f4f4f4; border-radius:10px; padding:14px 16px;">
            <span style="font-size:20px; flex-shrink:0;">🔍</span>
            <div>
                <p style="font-family:'Montserrat',Arial,sans-serif; font-size:0.78rem; font-weight:700; color:#222; margin:0 0 2px;">Suporte Técnico</p>
                <p style="font-family:'Montserrat',Arial,sans-serif; font-size:0.67rem; color:#777; margin:0; line-height:1.3;">Nossa equipe confere cada arte antes de produzir</p>
            </div>
        </div>
        <div style="display:flex; align-items:center; gap:12px; background:#f4f4f4; border-radius:10px; padding:14px 16px;">
            <span style="font-size:20px; flex-shrink:0;">💰</span>
            <div>
                <p style="font-family:'Montserrat',Arial,sans-serif; font-size:0.78rem; font-weight:700; color:#222; margin:0 0 2px;">Simulação Instantânea</p>
                <p style="font-family:'Montserrat',Arial,sans-serif; font-size:0.67rem; color:#777; margin:0; line-height:1.3;">Insira seu CEP e veja valores em tempo real</p>
            </div>
        </div>
    </div>

    <!-- FAQ -->
    <h3 style="font-family:'Montserrat',Arial,sans-serif; font-size:1.1rem; font-weight:700; color:#222; margin:0 0 16px; border-left:4px solid #f6631d; padding-left:12px;">
        Perguntas Frequentes
    </h3>

    <div style="display:flex; flex-direction:column; gap:10px; margin:0 0 32px;">

        <div style="background:#fff; border:1px solid #ebebeb; border-radius:10px; padding:16px 18px;">
            <p style="font-family:'Montserrat',Arial,sans-serif; font-size:0.85rem; font-weight:700; color:#222; margin:0 0 6px;">Qual a quantidade mínima para canetas personalizadas?</p>
            <p style="font-family:'Montserrat',Arial,sans-serif; font-size:0.82rem; color:#666; margin:0; line-height:1.6;">A quantidade mínima varia por modelo. Consulte a página de cada produto para verificar o mínimo disponível.</p>
        </div>

        <div style="background:#fff; border:1px solid #ebebeb; border-radius:10px; padding:16px 18px;">
            <p style="font-family:'Montserrat',Arial,sans-serif; font-size:0.85rem; font-weight:700; color:#222; margin:0 0 6px;">Qual o prazo de entrega para {cidade}?</p>
            <p style="font-family:'Montserrat',Arial,sans-serif; font-size:0.82rem; color:#666; margin:0; line-height:1.6;">A maioria dos pedidos é despachada em até 5 dias úteis após aprovação do arquivo. O prazo final depende da modalidade de frete escolhida.</p>
        </div>

        <div style="background:#fff; border:1px solid #ebebeb; border-radius:10px; padding:16px 18px;">
            <p style="font-family:'Montserrat',Arial,sans-serif; font-size:0.85rem; font-weight:700; color:#222; margin:0 0 6px;">Posso personalizar com nome e profissão?</p>
            <p style="font-family:'Montserrat',Arial,sans-serif; font-size:0.82rem; color:#666; margin:0; line-height:1.6;">Sim. Temos modelos específicos para personalização individual com nome, profissão e outros dados.</p>
        </div>

        <div style="background:#fff; border:1px solid #ebebeb; border-radius:10px; padding:16px 18px;">
            <p style="font-family:'Montserrat',Arial,sans-serif; font-size:0.85rem; font-weight:700; color:#222; margin:0 0 6px;">Como verifico a disponibilidade de cores?</p>
            <p style="font-family:'Montserrat',Arial,sans-serif; font-size:0.82rem; color:#666; margin:0; line-height:1.6;">Após escolher o modelo entre em contato com nossos consultores antes de finalizar o pedido para confirmar a cor disponível em estoque.</p>
        </div>

    </div>

    <!-- ##BLOCO_VAR_3## -->
<p style="font-family:'Montserrat',Arial,sans-serif; font-size:0.95rem; color:#555; line-height:1.8; margin:0 0 28px;">
{bloco_3}
</p>

    <!-- CTA FINAL -->
    <div style="background:#1a1a1a; border-radius:12px; padding:28px 24px; text-align:center;">
        <p style="font-family:'Montserrat',Arial,sans-serif; font-size:0.7rem; font-weight:700; letter-spacing:2.5px; text-transform:uppercase; color:#f6631d; margin:0 0 8px;">Pronto para começar?</p>
        <h3 style="font-family:'Montserrat',Arial,sans-serif; font-size:1.2rem; font-weight:800; color:#ffffff; margin:0 0 6px;">Simule o preço das suas Canetas agora</h3>
        <p style="font-family:'Montserrat',Arial,sans-serif; font-size:0.82rem; color:rgba(255,255,255,0.5); margin:0 0 20px; line-height:1.6;">Insira seu CEP e receba valores instantâneos de produção e entrega para <strong style="color:rgba(255,255,255,0.8);">{cidade}</strong>.</p>
        <a href="/categoria/canetas-personalizadas" style="display:inline-flex; align-items:center; gap:8px; background:#f6631d; color:#fff; font-family:'Montserrat',Arial,sans-serif; font-size:0.88rem; font-weight:700; padding:12px 28px; border-radius:8px; text-decoration:none;">
            Ver todas as Canetas →
        </a>
    </div>

</article>
</div>


<!--COMENTÁRIOS DE CLIENTES-->
<x-page id="3040"/>
<br/>
"""

    # colar código
    pc.copy(cod_pagina)
    pa.hotkey("ctrl", "v")

    # scroll
    pa.click(x=1717, y=534)
    pa.press("down", presses=70)

    # SEO dinâmico
    title = f"Canetas Personalizadas com Entrega Rápida em {cidade}"
    keywords = f"caneta personalizada {cidade}, caneta corporativa personalizada {cidade}, caneta com logo {cidade}, caneta ecológica personalizada {cidade}, brinde caneta personalizada {cidade}, caneta com nome {cidade}"
    description = f"🚀 Canetas personalizadas com entrega rápida em {cidade}. Clássica, ecológica ou executiva — com sua logo ou nome. Brinde corporativo de alto impacto. Solicite seu orçamento agora!"

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