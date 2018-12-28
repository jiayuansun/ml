import pandas as pd
import quandl
import math,datetime
import numpy as np
from sklearn import preprocessing,svm
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import cross_validate,train_test_split
import matplotlib.pyplot as plt
from matplotlib import style
import pickle

style.use('ggplot')
#svm is for regression

df=quandl.get('WIKI/GOOGL')
# print(df.head())
#feature the attribte makes up the lable, the lable is the 
df=df[['Adj. Open','Adj. High','Adj. Low','Adj. Close','Adj. Volume']]
df['HL_PCT']=(df['Adj. High']-df['Adj. Close'])/df['Adj. Close']*100.00
df['PCT_Change']=(df['Adj. Close']-df['Adj. Open'])/df['Adj. Open']*100.00
df=df[['Adj. Close','HL_PCT','PCT_Change','Adj. Volume']]
# print(df.head())

forecast_col='Adj. Close'
df.fillna(-9999,inplace=True)

forecast_out=int(math.ceil(0.01*len(df)))
print(forecast_out)
df['label']=df[forecast_col].shift(-forecast_out) 

#35 days after , this lable is the actrual Close price after a certain tables and is the is the label
# df.dropna(inplace=True)
# print(df.head())

#x feature
#y lable

x=np.array(df.drop(['label'],1))

#y=np.array(df['label'])
x=preprocessing.scale(x)
x_lately=x[-forecast_out:]
x=x[:-forecast_out]

# x=x[:-forecast_out+1]
df.dropna(inplace=True)
y=np.array(df['label'])


x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2)
clf=LinearRegression()
clf=svm.SVR(kernel='poly')
clf=LinearRegression(n_jobs=1)
clf.fit(x_train,y_train)#<--this is basicialy the training

#saving the classifier is to avoid the training
with open('linearregression.pickle','wb') as f:
    pickle.dump(clf,f)

    
pickle_in=open('linearregression.pickle','rb')
clf=pickle.load(pickle_in)

accuracy=clf.score(x_test,y_test)
# print(accuracy)

# print(len(x),len(y))

forecast_set=clf.predict(x_lately)
print(forecast_set,accuracy,forecast_out)
df['Forecast']=np.nan

last_date=df.iloc[-1].name
last_unix=last_date.timestamp()
one_day=86400
next_unix=last_unix+one_day


for i in forecast_set:
    next_date=datetime.datetime.fromtimestamp(next_unix)
    next_unix+=one_day
    df.loc[next_date]=[np.nan for _ in range(len(df.columns)-1)]+[i]

df['Adj. Close'].plot()
df['Forecast'].plot()
plt.xlabel('Date')
plt.ylabel('Price')

plt.show()