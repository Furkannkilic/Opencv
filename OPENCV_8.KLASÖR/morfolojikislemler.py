import cv2
import numpy as np

# Görüntüyü gri tonlamalı olarak oku
img = cv2.imread("C:\\Users\\furka\\Downloads\\helikopter.jpg", 0)

# 5x5 boyutunda bir kernel oluştur (beyaz pikselleri genişletmek ve daraltmak için kullanılır)
kernel = np.ones((5, 5), np.uint8)

# Genişletme (Dilation) işlemi: Beyaz alanları genişletir
dilation = cv2.dilate(img, kernel, iterations=5)

# Açılma (Opening) işlemi: Erozyon ve ardından genişletme uygular (gürültüyü kaldırmak için kullanılır)
opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)

# Kapanma (Closing) işlemi: Genişletme ve ardından erozyon uygular (küçük delikleri kapatmak için kullanılır)
closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)

# Morfolojik Gradyan işlemi: Genişletme ve erozyonun farkını alarak kenarları belirginleştirir
gradient = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)

# Aşındırma (Erosion) işlemi: Beyaz alanları küçültür
erosion = cv2.erode(img, kernel, iterations=5)

# Top Hat işlemi: Orijinal görüntü ile açılma işleminin farkını alır (aydınlık detayları öne çıkarır)
tophat = cv2.morphologyEx(img, cv2.MORPH_TOPHAT, kernel)


cv2.imshow("Erosion", erosion)
cv2.imshow("Dilation", dilation)
cv2.imshow("Opening", opening)
cv2.imshow("Closing", closing)
cv2.imshow("Gradient", gradient)
cv2.imshow("Tophat", tophat)

cv2.waitKey(0)
cv2.destroyAllWindows()
