import numpy as np
x=np.empty([3,3],np.uint8)#3 x 3 lük boş dizi oluşturmaya yarar uint ise negatif sayılarla çalışmadığımızı gösterir
print("x: ",x)
print("----")
y=np.full((3,3,3),dtype=np.int16,fill_value=5)#3x3 lük ve derinlik olarak 3 lük bir dizi oluşturur.fill_value diziyi doldurmak istediğimiz sayıyı belirler
print("y: ",y)
print("----")
z=np.ones((2,5,5),dtype=np.int8)#5x5lik ve 2 derinliğinde bir dizi oluşturur.1 lerle doldurur
print("z: ",z)
print("----")
j=np.zeros((2,5,5),dtype=np.int8)#5x5lik ve 2 derinliğinde bir dizi oluşturur.0 larla doldurur
print("j: ",j)