import datetime as dt 
import matplotlib.pyplot as plt 
from matplotlib import style
import pandas as pd 
import pandas_datareader.data as web
import os

style.use('ggplot')

def ls_1():
    start=dt.datetime(2000,1,1)
    end=dt.datetime(2016,12,31)

    df=web.DataReader('TSLA','yahoo',start,end)
    print(df.head())
    print(df.tail(6))

    df.to_csv('tsla.csv')

os.chdir('C:/Users/jisun/Desktop/ml')
df=pd.read_csv('tsla.csv',parse_dates=True,index_col=0)
print(df.head())

print(df[['Open','High']].head())

# df['Adj Close'].plot() #pandas plot for you
# plt.show()

df['100ma']=df['Adj Close'].rolling(window=100,min_periods=0).mean()

df.dropna(inplace=True) #entire record is dropped

# print(df.head())
ax1=plt.subplot2grid((6,1),(0,0),rowspan=5,colspan=1)
ax2=plt.subplot2grid((6,1),(5,0),rowspan=1,colspan=1,sharex=ax1)
# ax1=plt.subplot2grid((6,1),(0,0),rowspan=5,colspan=1)
# ax1=plt.subplot2grid((6,1),(0,0),rowspan=5,colspan=1)

ax1.plot(df.index,df['Adj Close'])
ax1.plot(df.index,df['100ma'])

ax2.bar(df.index,df['Volume'])
plt.legend()
plt.show()