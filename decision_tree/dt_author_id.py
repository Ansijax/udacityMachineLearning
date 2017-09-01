#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 3 (decision tree) mini-project.

    Use a Decision Tree to identify emails from the Enron corpus by author:    
    Sara has label 0
    Chris has label 1
"""
    
import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess
from sklearn import tree


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()


clf = tree.DecisionTreeClassifier(min_samples_split=50)

print "number of features {}".format(len(features_train[0]))

t0= time()
clf.fit(features_train,labels_train)
t1 = time()

print "fit time {}".format(round(t1-t0,3))
accuracy =clf.score(features_test,labels_test)

print "accuracy {}".format(accuracy)



#########################################################
### your code goes here ###


#########################################################


