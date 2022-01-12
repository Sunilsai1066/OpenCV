import cv2
import numpy as np

print("Imported")
# Read Image
Kernal = np.ones((5,5))
Img = cv2.imread("Resources/Lenna.png")
ImgGray = cv2.cvtColor(Img,cv2.COLOR_BGR2GRAY)
ImgBlur = cv2.GaussianBlur(ImgGray,(9,9),0)
ImgCanny = cv2.Canny(Img,100,200)
ImgDialate = cv2.dilate(ImgCanny,Kernal,iterations=1)
ImgEroded = cv2.erode(ImgDialate,Kernal,iterations=1)

cv2.imshow("RGB Image",Img)
cv2.imshow("Grey Image", ImgGray)
cv2.imshow("Blur Image",ImgBlur)
cv2.imshow("Canny Image",ImgCanny)
cv2.imshow("Dilated Image",ImgDialate)
cv2.imshow("Eroded Image", ImgEroded)
cv2.waitKey(0)
print("Window Closed")