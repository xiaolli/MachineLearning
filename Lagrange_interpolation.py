import pandas as pd
import os
from scipy.interpolate import lagrange

inputfile = os.path.join(os.path.dirname(__file__),'data6/missing_data.xls')
outfile = os.path.join(os.path.dirname(__file__),'data6/missing_data_processed.xls')

data= pd.read_excel(inputfile,header=None)

def ployinterp_column(s,n,k=5):         #s为列向量，n为被插入的位置， k为取前后的数据个数
    #print (s[list(range(n-k,n))])
    y = s[list(range(n-k,n)) + list(range(n+1,n+1+k))]
    #print ("-------",y)

    y =y[y.notnull()]                   #过滤出前后为非空的参考值

    #print("######",y)
    return lagrange(y.index,list(y))(n)

for i in data.columns:
    for j in range(len(data)):          #len(*args,*kwargs)  返回 在容器中的项目位置Number
        if (data[i].isnull())[j]:       #如果为Null
        #if data[i][j].isnull():
            data[i][j] = ployinterp_column(data[i],j)      #插入

data.to_excel(outfile,header=None,index = False)