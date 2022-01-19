import re
import cv2
import pytesseract
from pytesseract import Output

pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files (x86)/Tesseract-OCR/tesseract.exe'
img = cv2.imread('C://Users//Admin//Desktop//Julio//TCC//python//Aplicacao//Images//conta.jpeg', cv2.COLOR_BAYER_BG2BGR);

d = pytesseract.image_to_data(img, output_type=Output.DICT)
print(d.keys())

n_boxes = len(d['text'])

for i in range(n_boxes):
    if int(float(d['conf'][i])>20):
        (x,y,w,h) = (d['left'][i], d['top'][i], d['width'][i], d['height'][i],)
        img = cv2.rectangle(img, (x,y), ( x+w , y +h), (0,255,0),2)

cv2.imshow('Conta de Energia',img)
cv2.waitKey(0)        