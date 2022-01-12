import cv2

print("Imported")
"""
# Reading A Image
Img = cv2.imread('Resources/Lenna.png')
# Printing Image
cv2.imshow("Lenna Image", Img)
# It Waits Till We Close - O Means Infinite Delay We Can Mention Delay In Milliseconds Like 1000 =  1Sec
cv2.waitKey(0)
"""
"""
# Read Video
Cap = cv2.VideoCapture("Resources/TestVideo.mp4")
while(True):
    ReturnValue,Img = Cap.read()
    if(ReturnValue == False):
        break
    cv2.imshow("Nature Video",Img)
    if(cv2.waitKey(1) & 0xFF == ord("q")):
        print("Exited Playing Video")
        break
print("Played Video")
"""
# Read Video From WebCam
CamCap = cv2.VideoCapture(0)
while(True):
    ReturnStatus,Img = CamCap.read()
    cv2.imshow("WebCam Feed",Img)
    if(cv2.waitKey(1) & 0xFF == ord('q')):
        break
print("Taken Cam Feed")