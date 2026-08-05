import cv2
import re
import pandas as pd
from rapidocr_onnxruntime import RapidOCR

cap = cv2.VideoCapture(0)
engine = RapidOCR()

pattern = re.compile(r'^\d{2}[-\s]\d{4}[-\s]\d{6}$')
excel = pd.read_csv("data_excel.csv")
select = excel["Id_no"].astype(str).tolist()

while True:
    ret, frame = cap.read()

    if pattern.match(text):
        if text in select:
         print("Connected")
        else:
            print("Correct but not found")
    else:
        print("Invalid")

    cv2.imshow('frame', frame)
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()