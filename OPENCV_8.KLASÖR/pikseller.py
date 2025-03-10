import cv2
import numpy as np
img=cv2.imread("klon.jpg")
dimension=img.shape#shape img içerisinde tutlan resmin boyutlarını ve kanal verisini verir
print(dimension)
color=img[420,500]
print(color)
blue=img[420,500,0]#herhangi bir koordinattaki mavi değerine ulaşmak için
print("blue:",blue)
green=img[420,500,1]#herhangi bir koordinattaki yeşil değerine ulaşmak için
print("green:",green)
red=img[420,500,2]#herhangi bir koordinattaki kırmızı değerine ulaşmak için
print("red:",red)
cv2.imshow("klon asker",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
