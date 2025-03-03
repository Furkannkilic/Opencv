import matplotlib.pyplot as plt
import numpy as np
x=np.arange(5)#içerisine girdiğimiz sayıya kadar bize sayı üretir
print(x)
print(type(x))
print("----")
y=x
#plt.plot(x,y)#arka planda grafiğin çizimini yapar
#plt.show()# grafiği göstermek için
#plt.plot(x,y,"o-")#grafikteki doğruyu farklı bir yöntemle gösterir
#plt.show()
plt.plot(x,y,"o--")#grafikteki doğruyu farklı bir yöntemle gösterir
plt.plot(x,-y)#tek grafik üzerinde yorumlamamızı sağlar
plt.plot(-x,y,"o-")#tek grafik üzerinde yorumlamamızı sağlar
plt.title("ilk grafiğim")#grafiğe isim vermeye yarar
plt.show()