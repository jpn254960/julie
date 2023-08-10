from pyautogui import *
from os import system
while True:
    system('cls')  or None
    x,y=position()
    print(f'x={x} y={y}')