from rapidocr_onnxruntime import RapidOCR
import cv2

engine = RapidOCR()
img = cv2.imread('rapid_ocr_lesson/student.jpg')
result = engine(img)

for i in result:
    box = i[0]
    text = i[1]
    score = i[2]
    print(text, score)