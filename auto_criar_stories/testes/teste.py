#=============================
# IMPORTS
import pyautogui as pa
import shutil as sh
from pyperclip import copy, paste
from time import sleep
import random as rd
from datetime import datetime, timedelta, date
#=============================

# CONFIGURAÇÕES
dias = 2
site_meta = "https://business.facebook.com/latest/content_calendar"

#contagem de abas
contagem_de_abas = 0

pasta_1 = r"Y:\DESIGNS\Guilherme(Link)\VSCODE\Stories\imgs_teste_pasta_1"
pasta_2 = r"Y:\DESIGNS\Guilherme(Link)\VSCODE\Stories\imgs_teste_pasta_2"

pa.PAUSE = 0.7
tempo_inicio = 4
#=============================

# IMAGENS DE CLICK AND ERROR
img_criar_post = r"Y:\DESIGNS\Guilherme(Link)\VSCODE\Stories\img_click\criar_post.png"
img_criar_story = r"Y:\DESIGNS\Guilherme(Link)\VSCODE\Stories\img_click\criar_story.png"
img_add_midia = r"Y:\DESIGNS\Guilherme(Link)\VSCODE\Stories\img_click\adcionar_foto_video.png"
img_programar = r"Y:\DESIGNS\Guilherme(Link)\VSCODE\Stories\img_click\programar.png"
img_erro_video_longo = r"Y:\DESIGNS\Guilherme(Link)\VSCODE\Stories\img_click\erro_video_longo.png"
img_programar_azul = r"Y:\DESIGNS\Guilherme(Link)\VSCODE\Stories\img_click\programar_azul.png"
#=============================

for _ in range(2):
    pa.press("up", presses=10)
    try:
        erro = pa.locateOnScreen(img_erro_video_longo, confidence=0.8)
        print("erro encontrado")
        sleep(2)
        pa.click(x=701, y=255)
        pa.press("tab")
        pa.press("enter")
        x,y = pa.locateOnScreen(img_programar_azul, confidence=0.7)
        pa.click(x,y)
        sleep(5)
        pa.hotkey("ctrl", "w")
    except pa.ImageNotFoundException:
        print("erro nao encontrado")
        sleep(2)
        x,y = pa.locateOnScreen(img_programar_azul, confidence=0.7)
        pa.click(x,y)
        sleep(5)
        pa.hotkey("ctrl", "w")
#=============================
