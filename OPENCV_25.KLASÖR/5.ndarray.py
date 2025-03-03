import numpy as np
x=np.array([[-2,-1,0,5,],[9,4,5,-7]],np.int8)
print(x)
print(x.shape)#dizinin 2x4 oluştuğunun bilgisini verir
print(x.ndim)#kaç boyutlu olduğunu söyler
print(x.dtype)#veri tipini verir
print(x.size)#eleman sayisini verir
print(x.T)#elimizdeki dizinin transpozunu (devriğini) alır