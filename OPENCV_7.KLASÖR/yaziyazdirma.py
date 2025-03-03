import cv2
import numpy as np
canvas=np.zeros((512,512,3),dtype=np.uint8)+255

font1=cv2.FONT_HERSHEY_SIMPLEX
font2=cv2.FONT_HERSHEY_COMPLEX
font3=cv2.FONT_HERSHEY_SCRIPT_COMPLEX

cv2.putText(canvas,"opencv",(30,100),font1,3,(0,0,0),cv2.LINE_AA)#yazılıcak metin girilir sonra metnin yerleşeceği koordinatı gircez sonra yazı tipi daha sonra yazı tipinin büyüklüğü sonra rengi sonra yazının tipi girilir
cv2.imshow("Canvas",canvas)
cv2.waitKey(0)
cv2.destroyAllWindows()