import numpy as np
import pandas as pds

a = [1, 2, 3, 4]
b = np.array(a)

print("#No.1:\n", type(b))
print(b.shape)
print(b.size)
print('--------------------')
print(b.argmax())
print(b.argmin())
print(b.max())
print(b.min())
print(b.mean())

c = [[1, 2], [3, 4]]
d = np.array(c)
print('#No.2:\n',d.max(axis=0))
print(d.max(axis=1))
print(d.mean(axis=1))
print(d.flatten())
print(d.ravel())


arr = np.arange(10)
print("----------------------")
print(arr)
print(arr[0])
arr[5:8]=12

print(arr)

arr_slice = arr[5:8]
arr_slice[1]=12345

print(arr)

arr_slice[:]=64

print(arr)


arr = np.arange(12).reshape(4,3)
print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
print(arr[0])

print(arr - arr[0])

frame = pds.DataFrame(arr,columns=list('bde'),index=['Utah','Ohio','Texas','Oregon'])
series = frame.ix[:2]
print(frame)
print(series)

b = np.array([[1,2,3],[4,5,6],[7,8,9]])
c = np.array([1,0,1])
print(np.dot(b,c))
print(np.dot(b.T,c))
print(np.trace(b))

x = np.array([[1,2,3],[4,5,6]])
#y = np.array([4,5,6])
#z = np.array([7,8,9])
print(np.trace(x))

#np.linspace()

print(np.random.seed(42))