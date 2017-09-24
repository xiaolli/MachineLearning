import pandas as pd
import os
#初始化
dish_profit = os.path.join(os.path.dirname(__file__),'data/catering_dish_profit.xls')
data = pd.read_excel(dish_profit,index_col='菜品名')
data1 = data['盈利'].copy()

print(data1)

data.sort_index(ascending =False)

import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

CHfont =fm.FontProperties(fname='/System/Library/fonts/STHeiti Light.ttc')

plt.rcParams['axes.unicode_minus'] =False

#plt.legend(property=CHfont)
plt.figure()
data1.plot(kind ='bar')
plt.ylabel('盈利（元）',fontproperties = CHfont)

p = 1.0 * data1.cumsum()/data1.sum()

plt.twinx()   #双Y轴

p.plot(color = 'r',style = '-o',linewidth = 1)

plt.annotate(format(p[6],'.4%'),xy = (6,p[6]),xytext= (6 * 0.9 ,p[6] * 0.9),
             arrowprops = dict(arrowstyle = '->',connectionstyle = 'arc3,rad=.2'))


plt.ylabel('盈利（比例）',fontproperties = CHfont)
plt.show()