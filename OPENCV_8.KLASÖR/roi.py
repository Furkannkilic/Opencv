import cv2
img=cv2.imread("klon.jpg")
#pirnt(img.shape[:2]) resmin boyutlarını öğren
roi=img[30:200,200:400]#resimden istediğimiz kısmı almaya yarar 
cv2.imshow("klon",img)
cv2.imshow("ROI",roi)
cv2.waitKey(0)
cv2.destroyAllWindows()