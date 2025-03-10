import cv2
img=cv2.imread("klon.jpg")
img_rgb=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)#Resmi BGR renk uzayından RGB renk uzayına dönüştürür.
img_hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)#Resmi BGR renk uzayından HSV renk uzayına dönüştürür.
img_gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)#Resmi BGR renk uzayından GRAY renk uzayına dönüştürür.
cv2.imshow("klon BGR",img)
#cv2.imshow("klon RGB",img_rgb)
#cv2.imshow("klon HSV",img_hsv)
cv2.imshow("klon GRAY",img_gray)
cv2.waitKey(0)
cv2.destroyAllWindows()