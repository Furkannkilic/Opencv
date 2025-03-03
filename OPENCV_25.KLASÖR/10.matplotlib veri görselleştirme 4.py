import matplotlib.pyplot as plt
import numpy as np
img = plt.imread(r'C:\Users\furka\Downloads\10.1 coins.jpg')
 #resmi okumaya yarar
plt.imshow(img)#resmi göstermeye yarar
plt.show()#resmi göstermeye yarar üsttekiyle birlikte kullanılır"
# Görüntü bilgilerini yazdır
print(img)
print("type: ", type(img))
print("shape: ", img.shape)
print("ndim: ", img.ndim)
print("size: ", img.size)

# Piksel değerlerini yazdır
print("red channel: ", img[50, 50, 0])  # R = 0, G = 1, B = 2
print("green channel: ", img[50, 50, 1])
print("blue channel: ", img[50, 50, 2])
print("rgb channel value: ", img[50, 50,:])
