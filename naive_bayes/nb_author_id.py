#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 1 (Naive Bayes) mini-project. 

    Use a Naive Bayes Classifier to identify emails by their authors
    
    authors and labels:
    Sara has label 0
    Chris has label 1
"""
    
import sys
from time import time
import sklearn as sk
from sklearn.naive_bayes import GaussianNB
sys.path.append("../tools/")
from email_preprocess import preprocess


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()

t0 = time()
clf = GaussianNB()
clf.fit(features_train,labels_train)
t1 =time()
print "fit time {}".format(round(t1-t0,3))
t1=time()
clf.predict(features_train)
t2 = time()
print "predict time {}".format(round(t2-t1,3))

print "score :{}".format(clf.score(features_test,labels_test))
t3=time()
print "score time {}".format(round(t3-t2),3)


#########################################################
### your code goes here ###


#########################################################


