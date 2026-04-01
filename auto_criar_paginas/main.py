"""
Automação de criação de páginas em sistema interno.

Gera páginas automaticamente a partir de um template, substituindo
variáveis (como cidade, título, keywords e descrição) e preenchendo
os campos via PyAutoGUI no navegador.

Requer: pyautogui, pyperclip
"""

import webbrowser as wb
import time as tm
from controller import clicar_em
import pyautogui as pa
import pyperclip

def acessarPaginas():
    variaveis_1 = [
    "Ribeirão Pires",
    "Igarassu",
    "Simões Filho",
    "Catalão",
    "Codó",
    "Eunápolis",
    "Itabira",
    "Paulo Afonso",
    "Itanhaém",
    "Cubatão",
    "Passos",
    "Marituba",
    "Nova Lima",
    "Araxá",
    "São Lourenço da Mata",
    "Sorriso",
    "Paulínia",
    "Tubarão",
    "Itumbiara",
    "Luís Eduardo Magalhães",
    "Santana",
    "Cambé",
    "Breves",
    "Açailândia",
    "Tangará da Serra",
    "Jataí",
    "Erechim",
    "Nova Serrana",
    "Paragominas",
    "Maranguape",
    "Planaltina",
    "Lavras",
    "Coronel Fabriciano",
    "Muriaé",
    "São Pedro da Aldeia",
    "Ourinhos",
    "Novo Gama",
    "Poá",
    "Bacabal",
    "Itacoatiara",
    "Itabaiana",
    "Ubá",
    "Patos",
    "Camboriú",
    "Santo Antônio de Jesus",
    "Ituiutaba",
    "Manacapuru",
    "Balsas",
    "Lagarto",
    "Assis",
    "Itaperuna"
    ]

    for variavel_1 in variaveis_1:
        pagina = {
            "xxxx": variavel_1,
            "titulo_pagina":f"Copos Personalizados em {variavel_1}",
            "titulo": f"Copos Personalizados em  {variavel_1} – Criatividade para Brindes, Eventos e Lembranças",
            "keywords": f"copos personalizados em {variavel_1}, brindes personalizados {variavel_1}, copo térmico Lajeado, copo acrílico personalizado, personalização de copos em {variavel_1}, onde fazer copo personalizado {variavel_1}, copos para festas em {variavel_1}, copo termico, copos de brinde",
            "description": f"Descubra os melhores copos personalizados em {variavel_1} para eventos, empresas e brindes! Escolha modelos incríveis com personalização criativa, entrega rápida e qualidade garantida."   
        }

        # 1. Lê e personaliza o template e faz as substituições do arquivo codigo.txt.
        with open("codigo.txt", "r", encoding="utf-8") as arquivo:
            conteudo = arquivo.read()

        for chave, valor in pagina.items():
            conteudo = conteudo.replace(f"{{{{{chave}}}}}", valor)
            conteudo = conteudo.replace(chave, valor)  # cuidado: pode substituir palavras genéricas.

        print(f"\n🔧 Criando página: {pagina['titulo_pagina']}")

        # 2. Abre o navegador na página desejada
        wb.open("https://expanssiva.com.br/admin#/pages")
        tm.sleep(2.5)

        # 3. Clica no botão "nova página"
        clicar_em(r"Y:\DESIGNS\Guilherme(Link)\VSCODE\Cria paginas manual\img\nova_pagina.png", "nova_pagina.png", duplo_clique=False)
        tm.sleep(1.5)

        # 4. Preenche o nome da página.
        pyperclip.copy(pagina["titulo_pagina"])
        pa.hotkey("ctrl", "v")
        tm.sleep(0.1)
        pa.hotkey('tab')
        tm.sleep(0.1)

        # 5. Copia e cola o conteúdo.
        pyperclip.copy(conteudo)
        tm.sleep(0.1)
        pa.hotkey("ctrl", "v")
        tm.sleep(0.1)

        # 6. Move o mouse para fora do campo.
        pa.moveTo(1000, 500)
        tm.sleep(0.1)

        # 7. Rola a tela para garantir visibilidade.
        pa.scroll(-1000)
        tm.sleep(0.5)

        # 8. Clica e preenche as informações de baixo.
        clicar_em(r"Y:\DESIGNS\Guilherme(Link)\VSCODE\Cria paginas manual\img\titulo.png", "titulo.png", duplo_clique=False, confianca=0.85)
        pyperclip.copy(pagina["titulo"])
        pa.hotkey("ctrl", "v")
        tm.sleep(0.1)
        pa.hotkey('tab')
        tm.sleep(0.1)

        pyperclip.copy(pagina["keywords"])
        pa.hotkey("ctrl", "v")
        tm.sleep(0.1)
        pa.hotkey('tab')
        tm.sleep(0.1)

        pyperclip.copy(pagina["description"])
        pa.hotkey("ctrl", "v")
        tm.sleep(0.1)
        pa.hotkey('tab')
        tm.sleep(0.1)

        # 9. Salvar
        pa.press("f3")
        tm.sleep(1.5)

        # 10. Fechas guia
        pa.hotkey("ctrl", "w")
        tm.sleep(0.5)

if __name__ == "__main__":
    acessarPaginas()
