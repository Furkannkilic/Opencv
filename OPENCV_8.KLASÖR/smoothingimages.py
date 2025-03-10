import cv2
import numpy as np

# Görüntüleri yükle
img_filter = cv2.imread("C:\\Users\\furka\\Downloads\\8.2 filter.png")
img_median = cv2.imread("C:\\Users\\furka\\Downloads\\8.1 median.png")
img_bilateral = cv2.imread("C:\\Users\\furka\\Downloads\\8.4 bilateral.png")

# Ortalama bulanıklaştırma 
blur = cv2.blur(img_filter, (7,7))

# Gauss bulanıklaştırma 
blur_g = cv2.GaussianBlur(img_filter, (5,5), cv2.BORDER_DEFAULT)

# Medyan bulanıklaştırma 
median_blur = cv2.medianBlur(img_median, 5)

# İki taraflı filtreleme 
bilateral_blur = cv2.bilateralFilter(img_bilateral, 9, 75, 75)

# Orijinal ve işlenmiş görüntüleri gösterme
cv2.imshow("Original Bilateral", img_bilateral)
cv2.imshow("Bilateral Blur", bilateral_blur)

# Alternatif gösterimler (aktif etmek için başlarındaki # işaretini kaldır)
# cv2.imshow("Original Median", img_median)
# cv2.imshow("Median Blur", median_blur)

# cv2.imshow("Original Filter", img_filter)
# cv2.imshow("Blur", blur_g)
# cv2.imshow("Blur 2", blur)

cv2.waitKey(0)
cv2.destroyAllWindows()
