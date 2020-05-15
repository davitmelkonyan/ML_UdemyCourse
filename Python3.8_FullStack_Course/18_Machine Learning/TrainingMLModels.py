#Underfitting and overfitting
import pandas as pd
from pandas import DataFrame
titanic = pd.read_csv('titanic.csv')
titanic.head()#top rows (5 by default)
titanic.Survived.value_counts()

#predict most common value (underfitting)
if titanic.Survived.value_counts()[0]>titanic.Survived.value_counts()[1]:
    guess=0
else:
    guess=1
predicted = pd.Series([guess]*len(titanic))
#print ((titanic.Survived - predicted).abs().sum())
#print ((titanic.Survived - predicted).abs().mean()) #error rate
#print (1-(titanic.Survived - predicted).abs().mean()) #correct prediction rate


#overfiting - predict training data well but not new data
#train/ testing split

from sklearn.model_selection import train_test_split
titanic_train, titanic_test = train_test_split(titanic,test_size=0.1)#how large test set should be = 10%
print(titanic_train)
print(titanic_train.shape)
print(titanic_test)
print(titanic_test.shape)

def table_lookup_predictor(x, table):
    default = table.Survived.value_counts().idxmax()
    similar_tab = table.loc[(table["Pclass"]== x["Pclass"]) &\
                            (table["Sex"]== x["Sex"]) &\
                            (table["Siblings/Spouses Aboard"]== x["Siblings/Spouses Aboard"]) &\
                            (table["Parents/Children Aboard"]== x["Parents/Children Aboard"]),"Survived"]
    if len(similar_tab) == 0:
        return default
    else:
        return similar_tab.value_counts().idxmax()

print (titanic_train.iloc[0,:])#iloc from pandas - Purely integer-location based indexing for selection by position
print (table_lookup_predictor(titanic_train.iloc[0,:],titanic_train))