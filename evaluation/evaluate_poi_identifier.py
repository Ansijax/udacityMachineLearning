#!/usr/bin/python


"""
    Starter code for the evaluation mini-project.
    Start by copying your trained/tested POI identifier from
    that which you built in the validation mini-project.

    This is the second step toward building your POI identifier!

    Start by loading/formatting the data...
"""

import pickle
import sys
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit
from sklearn.model_selection import train_test_split
from sklearn import tree
from sklearn.metrics import confusion_matrix, accuracy_score, precision_score, recall_score

data_dict = pickle.load(open("../final_project/final_project_dataset.pkl", "r") )

### add more features to features_list!
features_list = ["poi", "salary"]

data = featureFormat(data_dict, features_list,sort_keys = '../tools/python2_lesson14_keys.pkl')
labels, features = targetFeatureSplit(data)

labels, features = targetFeatureSplit(data)
features_train, features_test, labels_train, labels_test = train_test_split(features,labels, random_state=42, test_size=0.3)
clf = tree.DecisionTreeClassifier()
clf.fit(features_train,labels_train)

y_label_predict=clf.predict(features_test,labels_test)
print "numer of POI {}".format(sum(labels_test))
print "the number of total people in the test set is {}".format(len(labels_test))
print "if i predict always 0.0 the accuracy of my clf is {}".format((len(labels_test)-sum(labels_test))/len(labels_test))
print confusion_matrix(labels_test, y_label_predict)
print "the precision is {}".format(precision_score(labels_test, y_label_predict))
print "the recall is {}".format(recall_score(labels_test, y_label_predict))
print "the accuracy score is {}".format(clf.score(features_test,labels_test))



