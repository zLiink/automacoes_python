"""
Automação para programar stories no Meta Business:
- Faz upload de mídia de uma pasta
- Preenche datas e horários
- Move arquivos enviados
- Trata erros de vídeos longos e falhas de programação

Resolução recomendada: 1920x1080
"""

# IMPORTS
import pyautogui as pa
import shutil as sh
from pyperclip import copy, paste
from time import sleep
import random as rd
from datetime import timedelta, date
import sys
import os
#=============================


#=============================
#=============================
#=============================
#CONFIGURAÇÕES
#Dias
dias = 5
#Data inicio
data_atual = date(2026, 4, 24)
#=============================
#=============================
#=============================

#site do meta
site_meta = "https://business.facebook.com/latest/content_calendar"

#contagem de abas
contagem_de_abas = 0

#Atalhos pastas
pasta_1 = r"Y:\DESIGNS\Guilherme(Link)\VSCODE\Stories\imgs_teste_pasta_1"
pasta_2 = r"Y:\DESIGNS\Guilherme(Link)\VSCODE\Stories\imgs_teste_pasta_2"

#Tempo para inicio e tempo entre cmds
pa.PAUSE = 0.7
tempo_inicio = 2
#=============================

#IMAGENS DE CLICK AND ERROR
img_add_midia = r"Y:\DESIGNS\Guilherme(Link)\VSCODE\Stories\img_click\adcionar_foto_video.png"
img_programar = r"Y:\DESIGNS\Guilherme(Link)\VSCODE\Stories\img_click\programar.png"
img_erro_video_longo = r"Y:\DESIGNS\Guilherme(Link)\VSCODE\Stories\img_click\erro_video_longo.png"
img_programar_azul = r"Y:\DESIGNS\Guilherme(Link)\VSCODE\Stories\img_click\programar_azul.png"
#=============================

#INICIO AUTOMAÇÃO
sleep(tempo_inicio)
#=============================

# ABRIR NAVEGADOR
pa.press("win")
pa.write("brave")
pa.press("enter")
sleep(4)
#=============================

#LOOP DE DIAS
for dia in range(dias):

    hora = ["21"]
    minutos = ["03"]
    extensoes_ordem = [".mp4"]

    #=============================
    #=============================

    #hora = ["11", "15", "18"]
    #minutos = ["53", "33", "53"]
    #extensoes_ordem = [".mp4", ".jpg", ".mp4"]
    
    qnt_horarios = len(hora)

    #=============================

    #Somar dias
    data_mais_um = data_atual + timedelta(days=dia+1)

    #Formatar para dd/mm/aaaa
    data_formatada = data_mais_um.strftime("%d/%m/%Y")
    #=============================

    #LOOP DE POSTS
    for i in range(qnt_horarios):
        
        #Gera escolha aleatoria
        item_aleatorio = rd.randint(0, 20)

        #ABRIR ABA E ACESSAR META
        pa.hotkey("ctrl", "t")

        #Contagem de abas
        contagem_de_abas += 1

        pa.write(site_meta)
        pa.press("enter")
        sleep(5)
        #=============================

        # CRIAR STORY
        pa.click(x=1819, y=152)
        sleep(1)

        pa.click(x=1659, y=206)
        sleep(4)

        #Acha o botao de adcionar mídia e já serve como validação tbm, pq se n encontrar encerra a automação
        encontrar_botao_adc_midia = pa.locateOnScreen(img_add_midia, confidence=0.5)
        if encontrar_botao_adc_midia:
            pos = pa.center(encontrar_botao_adc_midia)
            pa.click(pos)
            sleep(1.5)
        else:
            print("Botão de adcionar mídia nao encontrado, encerrando automação")
            sys.exit(1)
        #=============================

        # ACESSAR PASTA
        pa.hotkey("ctrl", "l")
        sleep(1)

        copy(pasta_1)
        pa.hotkey("ctrl", "v")
        pa.press("enter")
        #=============================

        # PESQUISAR EXTENSÃO
        pa.hotkey("ctrl", "f")
        pa.write(extensoes_ordem[i])
        pa.press("enter")
        sleep(2)
        #=============================

        # SELECIONAR 1 ARQUIVO
        pa.click(x=313, y=123)
        pa.press("down", presses=item_aleatorio)
        #=============================

        # PEGAR NOME DO ARQUIVO
        pa.press("f2")
        pa.hotkey("ctrl", "c")
        nome_item = paste().strip()
        pa.press("enter", presses=2)
        sleep(1)
        #=============================
        
        # PROGRAMAR POST
        pa.click(img_programar)
        sleep(1)

        #Arrasta a pagina para baixo
        pa.press("down", presses=4)
        sleep(1)

        #Preencher datas
        for _ in range(2):
            pa.press("tab")
            sleep(1)
            pa.hotkey("ctrl", "a")
            copy(data_formatada)
            pa.hotkey("ctrl", "v")
            pa.press("enter")
            pa.press("tab")
            pa.write(hora[i])
            pa.press("tab")
            pa.write(minutos[i])

        pa.press("tab")
        #=============================

        #AGUARDAR CARREGAMENTO
        sleep(20)
        #=============================

        #MOVER ARQUIVO
        #Garante que não duplica extensão
        if not nome_item.lower().endswith(extensoes_ordem[i]):
            nome_item += extensoes_ordem[i]

        origem = os.path.join(pasta_1, nome_item)

        try:
            if os.path.exists(origem):
                sh.move(origem, pasta_2)
                print("Movido:", nome_item)
            else:
                print("Arquivo não encontrado:", origem)

        except Exception as e:
            print("Erro ao mover:", e)
        #=============================

#VERIFICAÇÃO FINAL DE ERROS P/ PROGRAMAR
sleep(10)
for _ in range(contagem_de_abas):
    pa.press("up", presses=10)
    try:
        erro = pa.locateOnScreen(img_erro_video_longo, confidence=0.8)
        sleep(2)
        pa.click(x=701, y=255)
        pa.press("tab")
        pa.press("enter")
        sleep(1)
        pos = pa.locateOnScreen(img_programar_azul, confidence=0.7)
        print("Erro encontrado X - corrigido e programado com sucesso.")

        if pos:
            pa.click(pa.center(pos))

        sleep(5)
        pa.hotkey("ctrl", "w")
    except pa.ImageNotFoundException:
        print("Erro nao encontrado V - programado com sucesso.")
        sleep(2)
        pos = pa.locateOnScreen(img_programar_azul, confidence=0.7)

        if pos:
            pa.click(pa.center(pos))

        sleep(6)
        pa.hotkey("ctrl", "w")
#==============FIM===============