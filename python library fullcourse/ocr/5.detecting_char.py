import cv2
import pytesseract as detect

detect.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
img = cv2.imread("ocr/temp_image/image_ocr.png")
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
print(detect.image_to_string(img))

#detecting char
#print(detect.image_to_boxes(img))
HImg,wImg,_ = img.shape
#conf = r"--oem 3 --psm 6 outputbase digits" both i comment is come from the part 7
#boxs = detect.image_to_data(img, config=conf)
boxs = detect.image_to_boxes(img)
for b in boxs.splitlines():
    #print(b)
    b = b.split(" ")
    #print(b)#turn to list of string
    x,y,w,h = int(b[1]), int(b[2]), int(b[3]), int(b[4])
    #cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),1)
    cv2.rectangle(img,(x,HImg-y),(w,HImg-h),(0,0,255),1)#this will highlight and detect the text properly
    
    cv2.putText(img,b[0],(x,HImg-y+25),cv2.FONT_HERSHEY_COMPLEX,1,(50,50,255),2)
    #above will highlight and display below to detect text to ensure its correct
    #for now its doesnt display properly because the image i used

cv2.imshow("result", img)
cv2.waitKey(0)#it you put 3 it, the display will last in 3 seconds
