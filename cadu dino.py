import subprocess
import pyautogui
import time
import os
import keyboard
car=True
pyautogui.press('win')
pyautogui.write('chrome')
pyautogui.press('enter')
time.sleep(5)
pyautogui.leftClick()
pyautogui.hotkey('ctrl', 't')
pyautogui.write('https://trex-runner.com/')
pyautogui.press('enter')
time.sleep(4)
dino_x, dino_y =827,650
color =pyautogui.pixel(dino_x, dino_y)
print(f"color chose was {color}")
print(f"pixel chose was {dino_x}, {dino_y}")
pyautogui.press('space')
while car:
    game=pyautogui.pixel(1065,569)
    cactus=pyautogui.pixel(dino_x, dino_y)
    if color != cactus:
        pyautogui.press('space')
        print("jump")
        time.sleep(0.1)    
    if color != game:         
        if keyboard.is_pressed('0'):
            car=False
            print("stopped")                 
        if keyboard.is_pressed('9'):
            play=False
            print(f"color chose was {color}")
            print(f"pixel chose was {dino_x}, {dino_y}")
            pyautogui.press('space')
            play=True        