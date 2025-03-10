import cv2
import numpy as np

# Görüntüyü gri tonlamalı olarak yükle
img = cv2.imread("C:\\Users\\furka\\Downloads\\helikopter.jpg", 0)

# Görüntünün satır ve sütun değerlerini al
row, col = img.shape

# Döndürme matrisi oluştur (Dönme merkezi: (col/5, row/3), Açı: 180 derece, Ölçek: 1)
M = cv2.getRotationMatrix2D((col / 5, row / 3), 180, 1)
# (Döndürme işlemi)
dst = cv2.warpAffine(img, M, (col, row))


cv2.imshow("dst", dst)


cv2.waitKey(0)


cv2.destroyAllWindows()
