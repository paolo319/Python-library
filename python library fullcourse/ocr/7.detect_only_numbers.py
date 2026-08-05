import cv2
import pytesseract as detect

detect.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
img = cv2.imread("ocr/temp_image/image_ocr.png")
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
print(detect.image_to_string(img))

#detecting words
#print(detect.image_to_boxes(img))
HImg,wImg,_ = img.shape
conf = r"--oem 3 --psm 6 outputbase digits"
boxs = detect.image_to_data(img, config=conf)
print(boxs)#it display the rows and column with wide spaces
for x,b in enumerate(boxs.splitlines()):
    #print(b)
    if x!=0:
        b = b.split()
        print(b)#turn to list of string
        if len(b)==12:
            x,y,w,h = int(b[6]), int(b[7]), int(b[8]), int(b[9])#I dont understand either
            cv2.rectangle(img,(x,y),(w+x,h+y),(0,0,255),1)#this will highlight and detect the text properly
            cv2.putText(img,b[11],(x,y),cv2.FONT_HERSHEY_COMPLEX,1,(50,50,255),2)



cv2.imshow("result", img)
cv2.waitKey(0)