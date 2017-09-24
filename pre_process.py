import pandas as pd
import numpy as np
from numpy import set_printoptions
import matplotlib.pyplot as plt
from pandas.plotting import scatter_matrix
from sklearn.cross_validation import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.linear_model import SGDClassifier
from sklearn.preprocessing import MinMaxScaler

column_names = ['Sample code number','Clump Thickness','Uniformity of Cell Size','Uniformity of Cell Shape','Marginal Adhesion',
               'Single Epithelial Cell Size','Bare Nuclei','Bland Chromatin','Normal Nucleoli','Mitoses','Class']
data = pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/breast-cancer-wisconsin/breast-cancer-wisconsin.data',
                   names=column_names)

data= data.replace(to_replace='?',value=np.nan)
data=data.dropna(how='any')
#print(data.shape)
#print (data.dtypes)
data.shape
#data.hist()
#data.plot(kind='density',subplots =True,layout =(3,4),sharex=False)
data.plot(kind='box', subplots=True, layout=(3,4), sharex=False)
#scatter_matrix(data)
#plt.show()

array = data.values

X = array[:,0:8]
Y = array[:,8]
transformer = MinMaxScaler(feature_range=(0,1))

newX = transformer.fit_transform(X)

set_printoptions(precision=3)

print(newX)




pd.set_option('display.width',300)
pd.set_option('precision',4)
print(data.describe())

print(data.head(10))
print(data.groupby('Class').size())

print(data.corr(method='pearson'))
print(data.skew(),"%%%%%%%%%%%%")

X_train,X_test,y_train,y_text = train_test_split(data[column_names[1:10]],data[column_names[10]],test_size=0.25,random_state=33)

#print(y_train.value_counts())

#print(y_text.value_counts())

ss = StandardScaler()
X_train = ss.fit_transform(X_train)
X_test = ss.transform(X_test)

lr = LogisticRegression()
sgdc = SGDClassifier()
lr.fit(X_train,y_train)
lr_y_predict = lr.predict(X_test)
print(lr_y_predict)

sgdc.fit(X_train,y_train)
sgdc_y_predict = sgdc.predict(X_test)
print(sgdc_y_predict)

if lr_y_predict.all() == sgdc_y_predict.all():
    print('equal')
else:
    print('not equal')


