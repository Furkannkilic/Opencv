import numpy as np
x=np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]],np.int16)
print(x)
print(x[0,0,0])#en dıştaki köşeli parantezin içine girip 0 a gidiyoruz 0.indeksinde [[[1,2,3],[4,5,6]] bunun 0.indeksinde [1,2,3] bunun 0.indeksinde ise 1 vardır
print(x[0,1,0])
print(x[1,1,1])