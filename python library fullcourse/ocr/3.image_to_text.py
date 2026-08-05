import cv2 

img = cv2.imread('ocr/temp_image/id_sample.jpg', 1)

#to resize the images
img = cv2.resize(img, (400, 400))
#to rotate images
#img = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
#adding new folder
cv2.imwrite('new_folder.jpg', img)

cv2.imshow('picture',img)
cv2.waitKey(0)
cv2.destroyAllWindows()