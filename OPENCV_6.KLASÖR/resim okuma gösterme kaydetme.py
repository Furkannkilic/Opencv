import cv2
#img=cv2.imread("klon.jpg",cv2.IMREAD_GRAYSCALE=0)#Resmi gri tonlarda okumak için
img=cv2.imread("klon.jpg",0)
#print(img)#resimleri sayı olarak gösterir
cv2.namedWindow("IMAGE",cv2.WINDOW_NORMAL)# PENCERE İSMİNİ OLUŞTURMAYA VE ÇIKAN FOTOĞRAFIN BOYUTUNU DÜZENLEMEYE YARAR
cv2.imshow("IMAGE",img)
cv2.imwrite("klon1.jpg",img)#resmi kaydetmek için kullanılır
cv2.waitKey(0)#resim kısa süre açlıp kapanıyor bu yüzden cv2.waitKeyin içine 0 yazarak herhangi bir tuşa basmadan kapanmamasını sağlarız
cv2.destroyAllWindows()#tüm pencereleri kapatır