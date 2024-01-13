import random
import pyautogui as pg
import time
x =('monkey', 'donkey', 'dog')
time.sleep(8)
for i in range(500):
    a=random.choice(x)
    pg.write("You are a"+a)
    pg.press('enter')