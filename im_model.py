import pandas as pd
from random import shuffle
import os
datafile = os.path.join(os.path.dirname(__file__),'data6/model.xls')
data = pd.read_excel(datafile)
data = data.as_matrix()

shuffle(data)


p = 0.8

train = data[:int(len(data)*p),:]
test = data[int(len(data)*p):,:]

from  sklearn.tree import DecisionTreeClassifier
from  sklearn.externals import joblib

treefile = os.path.join(os.path.dirname(__file__),'tmp/tree.pkl')
tree = DecisionTreeClassifier()
tree.fit(train[:,:3],train[:,3])

joblib.dump(tree,treefile)

print(train)
print(tree.predict(train[:,:3]))

from cm_plot import *
cm_plot(train[:,3],tree.predict(train[:,:3])).show()


