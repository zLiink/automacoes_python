import pyautogui as pa
import time
from controller import clicar_em

def executar_receituario():

    time.sleep(2)

    clicar_em(r"Y:\DESIGNS\Guilherme(Link)\VSCODE\interface\img15x21\contorno1.png", "contorno1.png", duplo_clique=True)
    time.sleep(1)

    pa.hotkey(r"ctrl","p")
    time.sleep(1)

    clicar_em(r"Y:\DESIGNS\Guilherme(Link)\VSCODE\interface\img15x21\isuImpressao2.png", "isuImpressao2.png", duplo_clique=False)
    time.sleep(1.2)

    clicar_em(r"Y:\DESIGNS\Guilherme(Link)\VSCODE\interface\img15x21\imposicao3.png", "imposicao3.png", duplo_clique=False)
    time.sleep(0.6)

    clicar_em(r"Y:\DESIGNS\Guilherme(Link)\VSCODE\interface\img15x21\quant4.png", "quant4.png", duplo_clique=True)
    time.sleep(0.6)

    pa.write("2")
    time.sleep(0.6)

    pa.press('ENTER')
    time.sleep(0.7)

    clicar_em(r"Y:\DESIGNS\Guilherme(Link)\VSCODE\interface\img15x21\meio5.png", "meio5.png", duplo_clique=False)
    time.sleep(1)

    clicar_em(r"Y:\DESIGNS\Guilherme(Link)\VSCODE\interface\img15x21\espacamento6.png","espacamento6.png", duplo_clique=True)
    time.sleep(1)

    pa.write("3")
    time.sleep(0.6)

    pa.press('ENTER')
    time.sleep(0.7)

    pa.hotkey('alt','c')
    time.sleep(1)

    clicar_em(r"Y:\DESIGNS\Guilherme(Link)\VSCODE\interface\img15x21\aplicar7.png","aplicar7.png", duplo_clique=True)
    time.sleep(1)

if __name__ == "__main__":
    executar_receituario()