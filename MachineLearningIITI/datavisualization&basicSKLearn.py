#import the dataset
import pandas as pd
ad=pd.read_csv("D:\\AIML\\R (ML)\\Data Sets\\adult income.csv")

#seeing the structure of data
str(ad)

#checking null values
ad.isna()

#checking null values columnwise
ad.isna().sum()

#dropping null value
df=ad.dropna()
df
df.isna().sum()

#dealing with categories type of data
df.columns
cat=['age', 'workclass', 'fnlwgt', 'education', 'educational-num',
       'marital-status', 'occupation', 'relationship', 'race', 'gender',
       'capital-gain', 'capital-loss', 'hours-per-week', 'native-country',
       'income']
from sklearn.preprocessing import LabelEncoder #labelencoder data ko cat se con me krta h
lb=LabelEncoder()
for i in cat:
    df[i]=lb.fit_transform(df[i])
    
#dealing with continuous type of data
con=['age', 'fnlwgt', 'education', 'educational-num', 'capital-gain', 'capital-loss', 'hours-per-week', 'native-country']
from sklearn.preprocessing import MinMaxScaler
mm=MinMaxScaler()
for i in con:
    df[i]=mm.fit_transform(df[i].values.reshape(-1,1))
    
#splitting into train and test
from sklearn.model_selection import train_test_split
train,test=train_test_split(df,test_size=0.2)

trainx=train.iloc[:,:14] #all independent variables
#trainy=train.iloc[:,:-1]
trainy=train.iloc[:,14]

testx=test.iloc[:,:14] #all independent variables
#trainy=train.iloc[:,:-1]
testy=test.iloc[:,14]

#k nearest neighbour
#from sklearn.neighbors import KNearestClassifier
#knn=

#algorithms: 
    #knn 
    #naive_bayes 
    #decision tree 
    #randon forest
    #sym
    #survival
    
from sklearn.naive_bayes import GaussianNB
nv=GaussianNB().fit(trainx, trainy)
pred=nv.predict(testx)

from sklearn.metrics import accuracy_score
acc=accuracy_score(testy, pred)
acc
