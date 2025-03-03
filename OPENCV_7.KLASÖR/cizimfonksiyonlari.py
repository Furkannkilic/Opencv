import cv2
import numpy as np
canvas=np.zeros((512,512,3),dtype=np.uint8)+255

cv2.line(canvas,(50,50),(512,512),(120,0,255),thickness=5)#ilk çizginin başlangıç noktası sonra bitiş noktası daha sonra bu çizginin rengini belirliycez sonrada kalınlık girilcek
cv2.line(canvas,(100,100),(255,255),(255,100,255),thickness=7)

cv2.rectangle(canvas,(20,20),(80,80),(255,0,0),-1)#dikdörtgen çiziyor eğer içi dolu bir dikdörtgen istioyarsak kalınlık -1 olcak
cv2.circle(canvas,(250,250),100,(160,255,0),8 )#çember çiziyor.ilk olarak merkezini gircez daha sonra yarıçap değerini gircez
p1=(100,200)
p2=(50,50)
p3=(300,100)
cv2.line(canvas,p1,p2,(0,0,0),4)
cv2.line(canvas,p2,p3,(0,0,0),4)
cv2.line(canvas,p1,p3,(0,0,0),4)

points=np.array([[[110,200],[330,200],[290,220],[100,100]]],np.int32)
cv2.polylines(canvas,[points],True,(0,0,100),5)



cv2.imshow("Canvas",canvas)
cv2.waitKey(0)
cv2.destroyAllWindows()