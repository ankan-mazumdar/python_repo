import cv2
# cv2 reads images as numpy arrays (matrix) that is numpy 's few functionalityies are included in CV

img1 =cv2.imread("E:\\Ankita\Ankita\img\M3.jpg",1) # read the image in RGB/colored format # 3-D matrix
img2 =cv2.imread("E:\\Ankita\Ankita\img\M3.jpg",0) # read the image as gray scale/ black & white image #2-D matrix

print(type(img1))
print(img1.shape)
print(img1)
print(type(img2))
print(img2)
print(img2.shape)

cv2.imshow("ABC",img1)
new_size=cv2.resize(img2,(600,600)) #resizing parameters must be a tuple. puted inside ()
cv2.imshow("Panu",new_size)
# half_size=cv2.resize(img2,(int(img2.shape[1]/2),int(img2.shape[0]/2))) #new_image= old_image/2 #int type casted bcoz TypeError: integer argument expected, got float
# cv2.imshow("half",half_size)
# onethird_size=cv2.resize(img2,(int(img2.shape[1]/4),int(img2.shape[0]/4))) #new_image= old_image/2 #int type casted bcoz TypeError: integer argument expected, got float
# cv2.imshow("onethird",onethird_size)

# double=cv2.resize(img2,(int(img2.shape[1]*2),int(img2.shape[0]*2))) #new_image= old_image/2 #int type casted bcoz TypeError: integer argument expected, got float
# cv2.imshow("doubloo",double)
# # cv2.imshow("XYZ",img2) # it wil return RGB or an gray scale image dpend upon imread
cv2.waitKey() #waitkey() has bydefaault 0 as value i.e. cv2.waitKey(0) , it means press any key to destroy the opened image
# cv2.waitKey(10000)
cv2.destroyAllWindows()




