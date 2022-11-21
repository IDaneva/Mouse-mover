import random
import time
import pyautogui

while True:
    x = random.randint(600, 700)
    y = random.randint(200, 600)
    pyautogui.moveTo(x, y, 0.5)
    time.sleep(2)


# TODO: make a GUI
# TODO: make it possible to be ran outside the console

