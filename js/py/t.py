from pyautogui import click,hotkey
from time import sleep
for c in range(0,10):
    sleep(1)
    print(c+1)
hotkey('f5')
while True:
    click()
ta