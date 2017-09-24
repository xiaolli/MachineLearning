
from numpy import *
mymatrix1 = mat([[1,2,3],[4,5,6],[7,8,9]])
mymatrix2 = 1.5*ones([3,3])

print ("#No.1:\n",multiply(mymatrix1,mymatrix2))
print("#No.2:\n",power(mymatrix1,2))


print("#No.3:\n",mymatrix1.T)
print("#No.4:\n",mymatrix1.transpose())

print("#No.5:\n",mymatrix1.shape[0],"\n#No.6:\n",mymatrix1.shape[1])

print("#No.7:\n",mymatrix1[0])
print("#No.8:\n",mymatrix1.T[0])

mymatrix = mymatrix1.copy()
print("#No.9:\n",mymatrix)

print ("#No.10:\n",mymatrix < mymatrix.T)



