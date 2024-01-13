import pyautogui
import time

def screenshot():
    name=int(round(time.time()*1000))                                   #for Random number generrating
    name='H:/python_udemy/ScreenShot Data/{}.png'.format(name)          #save into the file with random number and.png format
    time.sleep(5)                                                       
    img=pyautogui.screenshot(name)                                      #Screenshot Function inbuilt into the pyautogui
    img.show()                                                          #Display Screenshot

screenshot()                                                            #calling function