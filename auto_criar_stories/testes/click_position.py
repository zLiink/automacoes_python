from pyautogui import position
from time import sleep

sleep(2)
x, y = position()

print(f"x={x}, y={y}")