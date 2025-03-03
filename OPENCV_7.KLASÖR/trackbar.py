import cv2
import numpy as np
def nothing(x):
    pass
img=np.zeros((512,512,3),np.uint8)
cv2.namedWindow("image")# ad vermemizin nedeni trackbar arayüzünü bu rengini değiştirceğimiz pencereye yerleştirceğimizi belirtmektir
cv2.createTrackbar("R","image",0,255,nothing)#girilen ilk parametre kızağın adı olacak kırmızı için R girdim ikinci parametre bu kızağın yerleşeceği pencerenin adı olacak 3. ve 4. parametre kızağın başlangıç ve bitiş değerleri olacak
cv2.createTrackbar("G","image",0,255,nothing)#girilen ilk parametre kızağın adı olacak kırmızı için R girdim ikinci parametre bu kızağın yerleşeceği pencerenin adı olacak 3. ve 4. parametre kızağın başlangıç ve bitiş değerleri olacak
cv2.createTrackbar("B","image",0,255,nothing)#girilen ilk parametre kızağın adı olacak kırmızı için R girdim ikinci parametre bu kızağın yerleşeceği pencerenin adı olacak 3. ve 4. parametre kızağın başlangıç ve bitiş değerleri olacak
switch="0:OFF,1:ON"#anahtar adı
cv2.createTrackbar(switch,"image",0,1,nothing)

while True:
    cv2.imshow("image",img)
    if cv2.waitKey(1)& 0xFF==ord("q"):
        break

    r=cv2.getTrackbarPos("R","image")
    g=cv2.getTrackbarPos("G","image")
    b=cv2.getTrackbarPos("B","image")
    s=cv2.getTrackbarPos(switch,"image")

    if s==0:#anahtar off sa siyah versin çalışmasın
        img[:]==[0,0,0]
    if s==1:#anahtar on sa
        img[:]=[b,g,r]#yukarda aldığımız değerleri renk değişmesi için pencereye yansıtıyoruz


cv2.waitKey(0)
cv2.destroyAllWindows()