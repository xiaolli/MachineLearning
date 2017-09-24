import pandas as pd

#等长列表组成字典
data = {
    "name":['leo','tom','kate','pig'],
    "age":[10,20,30,40],
    "weight":[50,50,40,200]
}

frame = pd.DataFrame(data)
print("#No.1:")
print(frame)

#指定列顺序

frame2 = pd.DataFrame(data,columns=['name','weight','age'])
print("#No.2:")
print(frame2)

#指定索引，其中columns参数没有的，会被设成NaN

frame3 =pd.DataFrame(data,columns=['name','age','weight','height'],index=['one','two','three','four'])
print("#No.3:\n",frame3)


#索引一列
print("name:\n",frame3['name'])
print('weight:\n',frame3.weight)

#改变一列的值
frame3.height = 100
print("#No.4:\n",frame3)

#转秩
print(frame3.T)

#print(frame3.at('three','weight'))

print(frame3.iat[1,2])

print(frame3.shape)

print(frame3.size)

print(frame3.values)

print(frame3.ndim)


print(frame3._ix)