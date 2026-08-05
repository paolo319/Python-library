from rapidocr_onnxruntime import RapidOCR
import cv2

engine = RapidOCR()
img = cv2.imread('rapid_ocr_lesson/student.jpg')
result = engine(img)
print(result)