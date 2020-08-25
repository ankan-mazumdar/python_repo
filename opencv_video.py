# Code for camera light on
# import cv2,time

# video=cv2.VideoCapture(0,cv2.CAP_DSHOW)
# time.sleep(25)
# cv2.waitKey(0)
# video.release()
# cv2.destroyAllWindows()

#Code for cap a picture using camera 
# import cv2

# camera = cv2.VideoCapture(0,cv2.CAP_DSHOW)
# # Check if the webcam is opened correctly
# if not camera.isOpened():
#     raise IOError("Cannot open webcam")

# return_value, image = camera.read()
# print("We take a picture of you, check the folder")
# print(return_value)
# print(image)
# cv2.imwrite("chodnar_chhobi.png", image)
# cv2.imshow("boss", image)
# cv2.waitKey(0)
# camera.release() # Error is here
# cv2.destroyAllWindows()

#Code for cap a picture using camera 
import cv2

camera = cv2.VideoCapture(0,cv2.CAP_DSHOW)
# Check if the webcam is opened correctly
if not camera.isOpened():
    raise IOError("Cannot open webcam")

a=1
while True:
    a= a + 1

    return_value, image = camera.read()
    print("We take a video of you, count the loops")
    print(return_value)

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    print(image)

    cv2.imshow("captured video", image)
    # cv2.imwrite("chodnar_chalanta_chhobi.mp4", image)
    k=cv2.waitKey(1) # wait for 1 millisecond
    if k == 27:
        break   

print(a)
camera.release() # Error is here
cv2.destroyAllWindows()