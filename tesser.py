import cv2
import pytesseract 
import os
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
#print(pytesseract.image_to_string(Image.open('test-european.jpg'), lang='fra'))
img=cv2.imread('5.jpg')
img2=cv2.imread('4.jpg')
#print(pytesseract.image_to_string(img))
out = pytesseract.image_to_string(img2, lang='hin')

from translation import (set_default_translation, set_default_language,
    set_default_proxies, get, ConnectError)

set_default_translation('google')
set_default_language('auto', 'zh-CN')
set_default_proxies({'http': '127.0.0.1:1080'})
try:
    print(get('hello world!'))
except ConnectError:
    print('Invaild proxy')

