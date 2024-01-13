import pyautogui
import time
import tkinter as tk

def screenshot():
    name=int(round(time.time()*1000))                                   #for Random number generrating
    name='D:/python_udemy/ScreenShot Data/{}.png'.format(name)          #save into the file with random number and.png format
    time.sleep(5)                                                       
    img=pyautogui.screenshot(name)                                      #Screenshot Function inbuilt into the pyautogui
    img.show()                                                          #Display Screenshot

#screenshot()                                                            #calling function
root=tk.Tk()                                                            #root is variable TK is Standard GUI library
frame=tk.Frame(root)                                                    #Frame is a container it contain pack of buttons text and other 
frame.pack()                                                            #set the positions of button and etc.

button=tk.Button(                                                       #Button Function
    frame,
    text="Take Screenshot",
    command=screenshot)
button.pack(side=tk.LEFT)                                               #position of Button into the pack placed at frame

close=tk.Button(
    frame,
    text="Quit",
    command=quit)
close.pack(side=tk.LEFT)

root.mainloop()                                                       #it run the application in infinite loop