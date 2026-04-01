import time as tm
from controller import clicar_em
import pyautogui as pa

tm.sleep(2)

def acessarPaginas():

   while True:
         
        clicar_em(r"Y:\DESIGNS\Guilherme(Link)\VSCODE\Cria paginas manual\img\desativar.png", descricao="desativar.png", duplo_clique=False, confianca=0.9)
        tm.sleep(0.5)
            
        pa.hotkey('f3')
        tm.sleep(0.5)

        pa.hotkey("ctrl", "w")
        tm.sleep(0.5)

if __name__ == "__main__":
    acessarPaginas()