import cv2
from PIL import Image
from pytesseract import pytesseract
#from rapidocr_onnxruntime import RapidOCR

cam=cv2.VideoCapture(0)
while True:
    _,image=cam.read()
    cv2.imshow('Text detection', image)
    if cv2.waitKey(1)& 0xFF==ord('s'):
        cv2.imwrite('test1.jpg', image)
        break
cam.release()
cv2.destroyAllWindows()

def tess():
    path=r"C:\Program Files\Tesseract-OCR\tesseract.exe"
    image_path='test1.jpg'
    pytesseract.tesseract_cmd = path
    text=pytesseract.image_to_string(Image.open(image_path))
    print(text[:-1])
tess()