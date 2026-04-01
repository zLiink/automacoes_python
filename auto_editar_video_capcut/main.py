"""
Automação para editar vídeos no CapCut:
- Ajusta escala, posição e velocidade do vídeo.
- Configura áudio e ruído, corta a música para o tamanho do vídeo.
- Executa exportação final automaticamente.
"""

import pyautogui as pa
import time as tm
import pyperclip as pc

#antes de iniciar ja adicionar o video no +
tm.sleep(2)

pa.PAUSE = 0.5
#escala
pa.doubleClick(x=1816, y=204)
pa.write("126")
pa.press("enter")

#posição y
pa.doubleClick(x=1627, y=281)
pa.write("123")
pa.press("enter")

#audio
pa.click(x=1439, y=54)

#Ruido
pa.click(x=1370, y=528)
tm.sleep(0.4)

#velocidade
pa.click(x=1508, y=58)
pa.click(x=1854, y=184)
pa.hotkey("ctrl", "a")
pa.write("1.1")
pa.press("enter")

#pega tamanho do video
pa.click(x=1848, y=242)
pa.hotkey("ctrl", "a")
pa.hotkey("ctrl", "c")
tamanho_video = pc.paste()
tamanho_video = float(tamanho_video)

#audio, deixar em favoritos já
pa.click(x=84, y=52)
#clica no +
pa.click(x=596, y=149)

#baixa o volume
pa.click(x=1815, y=156)
pa.hotkey("ctrl", "a")
pa.write("-20")
pa.press("enter")

#copia a musica dnv se o tamanho do video for maior que a musica
if tamanho_video > 200:
    pa.hotkey("ctrl", "c")
    pa.press("down")
    pa.hotkey("ctrl", "v")

#cortar a musica no msm tamanho do video
pa.press("down")
pa.press("w")

#click em exportar
pa.click(x=1762, y=21)
