import matplotlib.pyplot as plt
import numpy as np
"""n=11
x=np.linspace(0,10,n)#girilen aralikta istediğimiz kadar  veri üretiyor
print(x)
y=x
plt.plot(x,y,"o--")
plt.axis("off")#eksenleri yok ediyor
plt.show()"""
x=[1,2,3,4]
plt.plot(x,[y**2 for y in x])
plt.show()