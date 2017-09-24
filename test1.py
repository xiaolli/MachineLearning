import numpy as np
from numpy import *
import matplotlib.pyplot as plt
import json

myeye = np.eye(5)
print ("#no.1:",myeye)

myones = np.ones([5,5])
print("#no.2:",myeye+myones)
print("#no.3:",myones-myeye)


myrand=np.random.rand(3,4)
print ("#no.4:",myrand)



myzero = np.zeros([3,5])
print ("#no.5:",myzero)
myzero = np.ones([3,5])
print ("#no.6:",myzero)



dataset = [[1,2],[3,4],[5,6],[7,8],[9,10]]
mymatrix = mat(dataset)
print("#no7:",mymatrix.sum())
dataMat = mat(dataset).T

myarray = np.array(dataMat)

x = myarray[0]
y = myarray[1]

print ("#no.8:",x,y)

fig = plt.figure()
ax1 = fig.add_subplot(111)
ax1.set_title('Scatter Plot')
#设置X轴标签
plt.xlabel('X')
#设置Y轴标签
plt.ylabel('Y')

ax1.scatter(x,y,c = 'r',marker = 'o')
#plt.scatter(dataMat[0],dataMat[1])

plt.legend('x1')

X=np.linspace(-2,2,100)
Y = 2.8 * X + 9

plt.plot(X,Y)
plt.show()