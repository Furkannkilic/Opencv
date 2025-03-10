import cv2
import numpy as np
from matplotlib import pyplot as plt

# Görüntüyü gri tonlamalı  olarak yükle
img = cv2.imread("C:\\Users\\furka\\Downloads\\helikopter.jpg", 0)

# Basit eşikleme (Thresholding) işlemi:  
# Piksel değeri 180'in üzerindeyse 220'ye, değilse 0'a ayarlanır.
ret, th1 = cv2.threshold(img, 180, 220, cv2.THRESH_BINARY)

# Adaptif eşikleme  - Ortalama yöntemi
# Çevredeki piksellerin ortalamasına göre eşik değeri belirlenir.
th2 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)

# Adaptif eşikleme (Adaptive Thresholding) - Gaussian yöntemi
# Çevredeki piksellerin ağırlıklı ortalaması alınarak eşik değeri belirlenir.
th3 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 21, 2)

cv2.imshow("Orijinal Görüntü", img)
cv2.imshow("Basit Eşikleme (THRESH_BINARY)", th1)
cv2.imshow("Adaptif Eşikleme - Ortalama", th2)
cv2.imshow("Adaptif Eşikleme - Gaussian", th3)

cv2.waitKey(0)
cv2.destroyAllWindows()
