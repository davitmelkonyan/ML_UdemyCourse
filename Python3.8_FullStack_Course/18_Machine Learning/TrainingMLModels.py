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
print ((titanic.Survived - predicted).abs().sum())
print ((titanic.Survived - predicted).abs().mean()) #error rate
print (1-(titanic.Survived - predicted).abs().mean()) #correct prediction rate


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
tlu_train_predicted = titanic_train.apply(table_lookup_predictor,1,table = titanic_train)#make predictions on training set
print(tlu_train_predicted)

#compute error our alg made with accuracy_score() from scikit-learn
from sklearn.metrics import accuracy_score
print (accuracy_score(y_true = titanic_train.Survived, #true vals
                      y_pred = tlu_train_predicted)  ) #predicted vals
#quite accurate ^

#when its applied to test set (should be last thing, if repetedly refer to test set, it is no longer unseen data)
tlu_test_predicted = titanic_test.apply(table_lookup_predictor,1,table = titanic_train)
ans = accuracy_score(y_true=titanic_test.Survived, y_pred=tlu_test_predicted)
print (ans)# this one overfits slightly

#CROSS-Validation
# hyperparameters- characteristic of alg itself, not underlying phenomenon, intend to improve predictions
# e.g. cutoff age - above then bin variable = 0, below then = 1

#Steps:
#1. Divide data into k approx equal size subsets
#2. For each: A: treat it as "test" data and rest as "training" data
#             B: for each possible value of hyperparam, use training data to fit the model and eval its performance on test data; track performance
#3. Aggregate perform. of alg accross diff. subsets for each possible valye of hyperparam.
#4. Use the hyperparam value taht overall yielded best performance

# ^good way to compare algs
# say, six cutoff ages -> 10,20,30,40,50,60
from sklearn.model_selection import KFold #Kfold class can split dataset into folds, cross_val_score() does entire cross-valid procedure.
import numpy as np
Kf = KFold(n_splits=10) #doing it manually but in future will use cross_val_score(), folding object
for train, test in Kf.split(titanic_train):
    print("Training Indices:")
    print(train)
    print("\nTest Indices")
    print(test)
    print("\n-----\n")

def table_lookup_predictor_2(x, table, age):
    default = table.Survived.value_counts().idxmax() #value_counts - Return a Series containing counts of unique values., idxmax - Return index of first occurrence of maximum over requested axis. both from pandas
    similar_tab = table.loc[(table["Pclass"]== x["Pclass"]) &\
                            (table["Sex"]== x["Sex"]) &\
                            (table["Siblings/Spouses Aboard"]== x["Siblings/Spouses Aboard"]) &\
                            (table["Parents/Children Aboard"]== x["Parents/Children Aboard"]) &\
                            ((table["Age"] < age)== (x["Age"] < age)),"Survived"]
    if len(similar_tab)==0:
         return default
    else:
        return similar_tab.value_counts().idxmax()

ages = [10,20,30,40,50,60]
performace = dict() #new dictionary
for age in ages:
    cv_perf = list()
    for train, test in Kf.split(titanic_train):
        predicted = titanic_train.iloc[test,:].apply(table_lookup_predictor_2,1,table = titanic_train.iloc[train,:],
                                                    age = age)
        actual = titanic_train.loc[:,"Survived"].iloc[test]
        cv_perf.append(accuracy_score(y_true=actual, y_pred=predicted)) #add performance to a list
    performace[age] = cv_perf

print (DataFrame(performace)) # Two-dimensional size-mutable, potentially heterogeneous tabular data structure with labeled axes (rows and columns). Can be thought of as a dict-like container for Series objects
print (DataFrame(performace).mean())

