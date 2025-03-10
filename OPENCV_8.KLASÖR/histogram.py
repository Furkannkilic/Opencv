import cv2
import numpy as np
from matplotlib import pyplot as plt


img = cv2.imread("C:\\Users\\furka\\Downloads\\smilewomen.jpg")

# Alternatif olarak boş bir görüntü oluşturmak için aşağıdaki kodu kullanabilirsiniz
# img = np.zeros((500,500), np.uint8) + 50  # 500x500 boyutunda gri bir görüntü oluştur ve parlaklığını 50 yap
# cv2.rectangle(img, (0,60), (200,150), (255,255,255), -1)  # Beyaz bir dikdörtgen ekle
# cv2.rectangle(img, (250,170), (350,200), (255,255,255), -1)  # İkinci beyaz dikdörtgeni ekle

# Görüntüyü BGR kanallarına ayırmak için aşağıdaki satırları kullanabilirsiniz
# b, g, r = cv2.split(img)  # Görüntüyü Mavi (B), Yeşil (G) ve Kırmızı (R) kanallarına ayır


cv2.imshow("img", img)

# Histogramı çiz
plt.hist(img.ravel(), 256, [0,256])  # Tüm kanalların birleşik histogramını çiz

# Alternatif olarak, her kanalın ayrı histogramını çizmek için aşağıdaki satırları kullanabilirsiniz
# plt.hist(b.ravel(), 256, [0,256])  # Mavi kanal histogramı
# plt.hist(g.ravel(), 256, [0,256])  # Yeşil kanal histogramı
# plt.hist(r.ravel(), 256, [0,256])  # Kırmızı kanal histogramı

# Histogramı göster
plt.show()


cv2.waitKey(0)
cv2.destroyAllWindows()
