"""
Automação de seleção de impressões via PyAutoGUI.

Localiza elementos na tela por imagem, realiza cliques com CTRL
para seleção múltipla (até 15 por página) e navega automaticamente
entre páginas clicando no botão "Próximo".

Requer: pyautogui + opencv-python
"""

import pyautogui
import time

def clickImpressoes(paginas=15):
    for pagina in range(paginas):
        print(f"\n🔁 Página {pagina + 1} de {paginas}")
        time.sleep(1.5)

        imagens = [
            r"Y:\DESIGNS\Guilherme(Link)\VSCODE\abrirImpressoes\img\hashtag2_azul.png",
            "hashtag2_azul.png",
            r"Y:\DESIGNS\Guilherme(Link)\VSCODE\abrirImpressoes\img\hashtag2_vermelho.png",
            "hashtag2_vermelho.png"
        ]

        i = 0
        clicados = set()

        for imagem in imagens:
            for pos in pyautogui.locateAllOnScreen(imagem, confidence=0.86):
                center = pyautogui.center(pos)
                ponto = (round(center[0], -1), round(center[1], -1))

                if ponto in clicados:
                    continue

                clicados.add(ponto)

                print(f"🖱️  Clicando em {center} com imagem {imagem}")
                pyautogui.keyDown('ctrl')
                pyautogui.click(center)
                pyautogui.keyUp('ctrl')
                time.sleep(0.3)

                i += 1
                if i >= 15:
                    break
            if i >= 15:
                break

        # 👉 Depois de clicar, tentar ir para próxima página
        proximo_btn = pyautogui.locateCenterOnScreen(r"Y:\DESIGNS\Guilherme(Link)\VSCODE\abrirImpressoes\img\proximo.png", confidence=0.9)
        if proximo_btn:
            print(f"➡️  Clicando no botão Próximo: {proximo_btn}")
            pyautogui.click(proximo_btn)
            time.sleep(2)
        else:
            print("❌ Botão 'Próximo' não encontrado. Parando.")
            break

if __name__ == "__main__":
    clickImpressoes(paginas=15)
