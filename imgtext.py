import pytesseract
import os
from PIL import Image

pytesseract.pytesseract.tesseract_cmd= r"D:\python_udemy\RohitNVSP.png"

def Hello():
    img=Image.open('D:\python_udemy\RohitNVSP.png')
    text=pytesseract.image_to_string(img)
    print(text)

Hello()

