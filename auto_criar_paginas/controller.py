import pyautogui as pa
import time

# Função auxiliar para clicar por imagem
def clicar_em(imagem, descricao="", confianca=0.8, esperar=10, duplo_clique=False):
    print(f"[BUSCANDO] {descricao or imagem}...")
    inicio = time.time()
    pos = None
    while time.time() - inicio < esperar:
        pos = pa.locateCenterOnScreen(imagem, confidence=confianca)
        if pos:
            pa.moveTo(pos)
            if duplo_clique:
                pa.doubleClick()
                print(f"[OK] Duplo clique em: {descricao or imagem}")
            else:
                pa.click()
                print(f"[OK] Clique em: {descricao or imagem}")
            return True
        time.sleep(0.5)
    print(f"[ERRO] Não encontrado: {descricao or imagem}")
    return False

