import matplotlib.pyplot as plt
import numpy as np
x=np.arange(3)
plt.plot(x,[y**2 for y in x])
plt.plot(x,[y**3 for y in x])
plt.plot(x,2*x)
plt.plot(x,5.2*x)
plt.legend(['x**2','x***3','2*x','5.2*x'])#doğruların hangi maine ait olduğunu belirtir
plt.grid(True)#ızgara grafik haline gelir
#print(plt.axis())#doğuların başlangıç sonlanışını gösterir
plt.axis([0,2,0,10])#sınırları kendimizin verdiği yerde biter doğrular
plt.show()
