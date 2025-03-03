import numpy as np
x=np.array([[1,2,3],[4,5,6]],np.int16)#iki boyutlu bir dizi oluşturduk
print(x)
print("----")
print(x[0])#çok boyutlu dizilerde sıfırıncı indeks 1.dizi oluyor
print(x[0,0])# ilk dizinin ilk elemanı
print("----")
print(x[:,0])#ilk parantezin içindeki her şeyi tarıycak bu parantezin içindeki sıfırıncı indeksleri alcak
print("----")
print(x[0,:])
print(x[1,:])#satırları çekme yöntemi
