from PIL import Image
import cv2#opencv
import pytesseract

im_file = "ocr/temp_image/image_ocr.png" #getting inside of this folder

#im_file = "image_file/image_ocr.png" #getting from other folder
#im_file = "ocr/image_ocr.png"

im = Image.open(im_file)
print(im)# display the mode and size
#print(im.size) #displaying the size
#im.show() #showing the image
#im.rotate(180).show()
#im.save("image_file/image_ocr.png")
