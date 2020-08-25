#COde for Face Detection
import cv2
face_cascade=cv2.CascadeClassifier('C:\\Users\\Ankan\\anaconda3\\Lib\\site-packages\\cv2\\data\\haarcascade_frontalface_default.xml') #create CascadeClassifier object
img1 =cv2.imread("E:\\Ankita\Ankita\img\M4.jpg") #fetching the image
gray_img=cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY) #convert & read file as grayscale image
faces=face_cascade.detectMultiScale(gray_img,1.3, 4)
print(faces)
print(type(faces))
for x,y,w,h in faces:
    img1=cv2.rectangle(img1,(x,y),(x+w,y+h),(0,255,0),3) #we are drawing a rectangle, 1 is the image, 2 & 3 are corrdiantes of starting & ending points of rect., 4 is the color BGR, 5 is align width/thickness of rect.
cv2.imshow("half",img1)
cv2.waitKey()
cv2.destroyAllWindows()


