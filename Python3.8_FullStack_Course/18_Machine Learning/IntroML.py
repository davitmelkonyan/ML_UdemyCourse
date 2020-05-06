from sklearn.datasets import load_iris
import matplotlib.pyplot as plt
import numpy as np

iris_obj = load_iris()
print (iris_obj.DESCR)
print (iris_obj.data)
print (iris_obj.feature_names)
print (iris_obj.target)
print (iris_obj.target_names)

#choosing random subset of the data
train = np.random.choice(np.arange(len(iris_obj.data)),size = 100, replace = False)
train = np.sort(train)
print (train)

#remaining treated as unlabeled
test = np.setdiff1d(np.arange(len(iris_obj.data)),train) #returns unique values in first one that aren't in second one
print (test)

marker_map = {0: 'o',1: 's', 2: '^'}
color_map = {0: 'red',1: 'green', 2: 'red'}
var1, var2 = 0,1 #sepal length & width
for length, width, species in zip(iris_obj.data[train, var1],iris_obj.data[train,var2],iris_obj.target[train]):
    plt.scatter(x=length,y=width, marker=marker_map[species], c = color_map[species])
plt.xlabel(iris_obj.feature_names[var1])
plt.xlabel(iris_obj.feature_names[var2])
plt.show()

#plot including unlabeled data
for length, width, species in zip(iris_obj.data[train, var1],iris_obj.data[train,var2],iris_obj.target[train]):
    plt.scatter(x=length,y=width, marker=marker_map[species], c = color_map[species])
for l, w in zip(iris_obj.data[test,var1],iris_obj.data[test,var2]):
    plt.scatter(x=l,y=w, marker='o', c = "black")
plt.xlabel(iris_obj.feature_names[var1])
plt.xlabel(iris_obj.feature_names[var2])
plt.show()

#plot using different variables
var1, var2 = 2, 3
for length, width, species in zip(iris_obj.data[train, var1],iris_obj.data[train,var2],iris_obj.target[train]):
    plt.scatter(x=length,y=width, marker=marker_map[species], c = color_map[species])
for l, w in zip(iris_obj.data[test,var1],iris_obj.data[test,var2]):
    plt.scatter(x=l,y=w, marker='o', c = "black")
plt.xlabel(iris_obj.feature_names[var1])
plt.xlabel(iris_obj.feature_names[var2])
plt.show()

import pandas as pd
from pandas import DataFrame
titanic = pd.read_csv('titanic.csv')
print (titanic.head())
print (titanic.Survived.value_counts()) #returns object containing counts of unique values, resulting object in descending order so that the first element is the most frequently-occurring element
#always predicts 0 = didn't survive
predicted = pd.Series([0]*len(titanic))# as in [0,0,0,...0] with size of len(titanic)
print ((titanic.Survived-predicted).abs().sum())

