import cv2
import pytesseract as detect

detect.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
img = cv2.imread("ocr/temp_image/id_sample.jpg")
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
print(detect.image_to_string(img))#it display the text from image in terminal
cv2.imshow("result", img)
cv2.waitKey(0)#it you put 3 it, the display will last in 3 seconds

