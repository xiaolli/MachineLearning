import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl

'''
N = 5
menMeans=(20,35,30,35,27)
menStd =(2,3,4,1,2)

ind = np.arange(N)
width = 0.35

fig,ax = plt.subplots()
rects1= ax.bar(ind,menMeans,width,color ='y',yerr = menStd)


womenMeans=(25,32,34,20,25)
womenStd =(3,5,2,3,3)
rects2 = ax.bar(ind+width,womenMeans,width,color='g',yerr=womenStd)

ax.set_ylabel('scores')
ax.set_title('score by group and gender')
ax.set_xticks(ind+width)
ax.set_xticklabels(('G1','G2','G3','G4','G5'))

ax.legend((rects1[0],rects2[0]),('Men','Women'))

def autolabel(rects):
    #attach some text labels
    for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x()+rect.get_width()/2.,1.05*height,'%d'%int(height),ha='center',va='bottom')

autolabel(rects1)
autolabel(rects2)

plt.show()
'''
#----------------------------------------------------
mpl.rcParams['xtick.labelsize'] = 24
mpl.rcParams['ytick.labelsize'] = 24

np.random.seed(42)

x= np.linspace(0,5,100)

y= 2*np.sin(x) + 0.8*x*2

y_data = y + np.random.normal(scale=0.5,size=100)

plt.figure('data')
plt.plot(x,y_data,'.')

plt.figure('model')
plt.plot(x,y)

plt.figure('data&model')
plt.plot(x,y,'k',lw=3)

plt.scatter(x,y_data)

plt.savefig('result.jpg')

plt.show()

