import pandas as pd
import os
catering_sale = os.path.join(os.path.dirname(__file__),'data/catering_sale.xls')
data = pd.read_excel(catering_sale,index_col='日期')
data =  data[(data['销量'] > 400 ) & (data['销量'] < 5000)]

statistics = data.describe()

statistics.loc['range']= statistics.loc['max'] -statistics.loc['min']
statistics.loc['var'] = statistics.loc['std'] / statistics.loc['mean']
statistics.loc['dis'] = statistics.loc['75%'] - statistics.loc['25%']

print (statistics)

