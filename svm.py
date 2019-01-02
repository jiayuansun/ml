import numpy as np
from sklearn.model_selection import cross_validate,train_test_split
from sklearn import preprocessing,neighbors,svm
import pandas as pd
#import pickle

df=pd.read_csv('C:/Users/jisun/Desktop/python/ml_dataset/breast-cancer-wisconsin.data.txt')
df.replace('?',-99999,inplace=True) #make it outlier
df.drop(['id'],1,inplace=True)
#df.dropna

X=np.array(df.drop(['class'],1)) #feature
y=np.array(df['class']) #label

X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2)

clf=svm.SVC()
clf.fit(X_train,y_train)

# with open('kmeans_breast.pickle','wb') as f:
#     pickle.dump(clf,f)

# pickle_in=open('kmeans_breast.pickle','rb')
# clf=pickle.load(pickle_in)

accuracy=clf.score(X_test,y_test)
print(accuracy)

example_measures=np.array([4,2,1,1,1,2,3,2,1])
# example_measures=example_measures.reshape(len(example_measures),-1)
example_measures=example_measures.reshape(1,-1)
prediction=clf.predict(example_measures)

print(prediction)
