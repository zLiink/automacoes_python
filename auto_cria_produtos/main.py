"""
Automação de criação de produtos via PyAutoGUI.

Preenche códigos de produtos em um sistema interno, executa ações
na interface e aguarda o processamento entre cada item.

Requer: pyautogui
"""

import pyautogui as pa
import time as tm

tm.sleep(3)

produtos = ["08154", "18923", "05053", "06013", "06014", "06015", "06015A", "08308", "P@14594", "15044", "15203", "15233", "15234", "15235", "12204"]

pa.PAUSE = 0.7

for produto in produtos:

    pa.click(x=417, y=321)
    pa.hotkey('ctrl', 'a')
    pa.write(produto)
    pa.press("enter")
    pa.click(x=1578, y=451)
    pa.click(x=1095, y=428)
    tm.sleep(70)
