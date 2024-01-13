import pyautogui
import time
time.sleep(3)
digits = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

for i in range(10):
    for digit in digits:
        pyautogui.typewrite(digit)
        pyautogui.press("enter")


