import pyautogui
import time

time.sleep(5)
for i in range(500):
    n = str(i+1)
    pyautogui.typewrite(n)
    pyautogui.typewrite(" Hello")
    pyautogui.press('enter')
    print(i+1)
