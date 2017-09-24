import pandas as pd
import os
from pylab import mpl

catering_sale =os.path.join(os.path.dirname(__file__),'data/catering_sale.xls')
data = pd.read_excel(catering_sale,index_col='日期')


import matplotlib.pyplot as plt
#zhfont = fm.FontProperties(fname = '/System/Library/fonts/Arial Unicode.ttf')

#plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['font.sans-serif'] = ['']
plt.rcParams['axes.unicode_minus'] =False


plt.figure()

p = data.boxplot(return_type = 'dict')



x = p['fliers'][0].get_xdata()
y = p['fliers'][0].get_ydata()
y.sort()


for i in range(len(x)):
    if i > 0 :
        plt.annotate(y[i],xy = (x[i],y[i]),xytext = (x[i]+0.05 - 0.8 /(y[i]-y[i-1]),y[i]))

    else:
        plt.annotate(y[i],xy = (x[i],y[i]),xytext = (x[i]+0.08,y[i]))

plt.show()