import pandas as pd
import os
import numpy as np

catering_sale = os.path.join(os.path.dirname(__file__),"data/catering_sale_all.xls")

data = pd.read_excel(catering_sale,index_col='日期')

print("#No.1:",data.corr())

print ("#No.2:",data.corr()['百合酱蒸凤爪'])

print("#No.3:",data['百合酱蒸凤爪'].corr(data['翡翠蒸香茜饺']))


D=pd.DataFrame(np.random.randn(6,5))
print(D.describe())

M=pd.Series(range(0,20))

print(M.cumsum())
print(M.cumprod())
print(M.cummax())
print(M.cummin())

print(pd.rolling_sum(M,2))
#print(pd.Series.rolling(window = 2, center = False).sum())

x = np.linspace(0,2*np.pi,50)
y = np.sin(x)

import matplotlib.pyplot as plt

plt.plot(x,y,'bp--')
plt.show()

import matplotlib.pyplot as plt2

labels = 'Frogs','Hogs','Dogs','Logs'
sizes = [15,30,45,10]

colors = ['yellowgreen','gold','lightskyblue','lightcoral']

explode =(0,0.1,0,0)

plt2.pie(sizes,explode=explode,labels=labels,colors=colors,autopct='%1.1f%%',shadow=True,startangle=90)
plt2.axis('equal')
plt2.show()
