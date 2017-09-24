# from pandas  import series, dataframe

import pandas as pd

#1:传入data不传入索引列表，那么自动创建索引（0～N-1）
data=[1,2,3,4]

S = pd.Series(data)
print("#No.1:")
print("S:\n",S)

#2:传入索引列表
index = ['a','b','c','d']
S2 = pd.Series(data,index)
print("#No.2:")
print("S2:\n",S2)
print(S2.index)

#通过索引访问值
print(S2['b'])
print(S2[['a','c','d']])

#3：通过字典创建
dict={'leo':24,'kate':23,'mat':11}
S3 = pd.Series(dict)

print("#No.3:")
print('S3:\n',S3)

#4：即使传入字典，也可传入索引，如果和字典索引相同就并入，否则就找不到值，相应的Value 就会返回NaN
idx = ['leo','kate','pig','cat']
S4 = pd.Series(dict,idx)
print("#No.4:")
print("S4:\n",S4)