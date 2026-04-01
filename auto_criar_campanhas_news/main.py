import pyautogui as pa
import time as tm
import pyperclip as pc

#Pausa entre cmds
pa.PAUSE = 0.2

#Variaveis editaveis
#====================================================================
assunto = [
    "📢 Comunicado Importante sobre nosso Funcionamento no Carnaval"
]

complemento_do_assunto = [
    "Parceria • Agilidade • Tranquilidade"
]

tags = [
    "antecipacao_demandas_carnaval_fevereiro_2026"
]

id_pagina = [
    "7176"
]

hora = [
    "2026-02-16 07:33"
]
#====================================================================

tm.sleep(3)

for indx in range(len(assunto)):
    tm.sleep(2)

    #Abrir nova guia
    pa.hotkey("ctrl", "t")
    pa.write("https://login.sendpulse.com/emailservice/tasks/")
    pa.press("enter")
    tm.sleep(10)
    pa.click(x=321, y=299)
    tm.sleep(7)
    
    pa.click(x=842, y=415)
    tm.sleep(0.4)

    pc.copy("🎈")
    pa.hotkey("ctrl", "v")

    #Selecionar todas as lista de email com 🎈
    for _ in range(10):
        tm.sleep(0.1)
        pa.press("enter")
        tm.sleep(0.1)
        pa.press("down")

    pa.click(x=1263, y=669)

    #Tempo para carregar os emails
    tm.sleep(13)

    for _ in range(5):
        pa.press("tab")

    pc.copy(assunto[indx])
    pa.hotkey("ctrl", "v")
    tm.sleep(0.5)

    for _ in range(4):
        pa.press("tab")
        tm.sleep(0.1)

    pa.press("enter")
    tm.sleep(5)

    #Abrindo nova guia para pegar o html da pagina
    pa.hotkey("ctrl", "t")
    pa.write("https://expanssiva.com.br/admin#/emails")
    pa.press("enter")
    tm.sleep(2)
    pa.write(id_pagina[indx])
    pa.press("enter")
    tm.sleep(0.5)

    for _ in range(8):
        pa.press("tab")
        tm.sleep(0.4)
        
    pa.press("enter")
    tm.sleep(2)

    pa.click(x=411, y=271)
    tm.sleep(2)

    pa.hotkey("ctrl", "u")
    tm.sleep(0.5)
    pa.hotkey("ctrl", "a")
    tm.sleep(0.5)
    pa.hotkey("ctrl", "c")
    tm.sleep(0.5)

    #Fechar as guias
    for _ in range(3):
        pa.hotkey("ctrl", "w")
        tm.sleep(0.4)

    #Chegar na opção de importar html
    pa.click(x=521, y=512)
    pa.sleep(0.4)

    for _ in range(4):
        pa.press("tab")
        tm.sleep(0.1)

    pa.press("enter")
    tm.sleep(0.4)
    pa.press("tab")

    #Copiar codigo html no campo
    pa.hotkey("ctrl", "v")
    tm.sleep(0.5)

    for _ in range(2):
        pa.press("tab")
        tm.sleep(0.2)
        
    pa.press("enter")    
    tm.sleep(3.5)

    for _ in range(2):
        pa.press("tab")
        tm.sleep(0.2)

    pa.press("enter")    
    tm.sleep(2.5)

    #Editar complemento de assunto
    for _ in range(6):
        pa.press("tab")
        tm.sleep(0.2)

    pa.press("enter")    
    tm.sleep(0.5)
    pc.copy(complemento_do_assunto[indx])
    pa.hotkey("ctrl", "v")
    tm.sleep(0.5)

    pa.press("enter")
    tm.sleep(0.5)

    #Salvar e continuar complemento de assunto
    for _ in range(8):
        pa.press("tab")
        tm.sleep(0.2)

    pa.press("enter")
    tm.sleep(2)

    #Adicionar tags
    pa.click(x=782, y=390)
    tm.sleep(0.4)
    pa.press("tab")
    pc.copy(tags[indx])
    pa.hotkey("ctrl", "v")

    #Continuar depois das tags
    for _ in range(10):
        pa.press("tab")
        tm.sleep(0.2)

    pa.press("enter")
    tm.sleep(6)

    #Selecionar hora e dia e partes email
    pa.press("down", presses=20)
    tm.sleep(0.4)
    pa.click(x=546, y=765)
    tm.sleep(0.4)
    pa.press("tab")
    tm.sleep(0.4)
    pc.copy(hora[indx])
    pa.hotkey("ctrl", "v")
    tm.sleep(0.4)
    pa.click(x=547, y=911)
    tm.sleep(0.4)
    pa.press("down", presses=10)
    tm.sleep(0.4)
    pa.click(x=803, y=726)
    tm.sleep(0.4)
    pa.press("tab")
    tm.sleep(0.4)
    pa.press("6")