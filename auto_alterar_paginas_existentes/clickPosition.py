"""
Script utilitário para obter a posição atual do mouse:
- Aguarda 3 segundos para posicionar o cursor.
- Captura as coordenadas x e y do mouse.
- Exibe no console para facilitar a automação de cliques.
"""

import pyautogui as pa
import time

time.sleep(3)

x,y = pa.position()
print(f"x={x}, y={y}")
