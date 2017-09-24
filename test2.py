import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


myarray = np.array([1,2,3])
print(myarray)
print(myarray.shape)

index = ['a','b','c']

myseries=pd.Series(myarray,index=index)
print(myseries,myseries[1:2])


myarray1 = np.array([[1,2,3],[2,3,4],[3,4,5]])
print(myarray1)
print(myarray1.shape)

print("this is 2row & 3col  : %s" %myarray1[1,2])


myarray2=np.array([[11,21,31],[21,31,41],[31,41,51]])
rowindex =['row1','row2','row3']
colname = ['col1','col2','col3']

mydataframe = pd.DataFrame(data=myarray2,index=rowindex,columns=colname)
print(mydataframe)
print(mydataframe['col3'])

print(myarray1 + myarray2)

print(myarray1 * myarray2)


plt.plot(myarray1)
plt.scatter(myarray,myarray2[0])
plt.xlabel('x axis')
plt.ylabel('y axis')

plt.show()