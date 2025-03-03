import cv2
import numpy as np
canvas=np.zeros((512,512,3),dtype=np.uint8)+255 #canvas tuval oluştururken kullanılır  np.zeros fonksiyonunun amacı ise belli bir alanı siyah olan tuval oluşturmaktır beyaz yapmak istiyosak 255 ekle
cv2.imshow("Canvas",canvas)
cv2.waitKey(0)
cv2.destroyAllWindows()