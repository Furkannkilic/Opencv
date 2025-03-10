import cv2
import numpy as np

# Görüntüyü gri tonlamalı
img = cv2.imread("C:\\Users\\furka\\Downloads\\helikopter.jpg", 0)

# Görüntünün satır ve sütun  bilgilerini al
row, col = img.shape

# Dönüşüm matrisi oluştur (x ve y ekseninde 100 piksel kaydırma)
Matrix = np.float32([[1, 0, 100], [0, 1, 100]])

# Görüntüyü verilen dönüşüm matrisi ile kaydır
dst = cv2.warpAffine(img, Matrix, (row, col))

cv2.imshow("dst", dst)

cv2.waitKey(0)
cv2.destroyAllWindows()
