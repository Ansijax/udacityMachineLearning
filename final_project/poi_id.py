#!/usr/bin/python

import sys
import pickle
sys.path.append("../tools/")

from feature_format import featureFormat, targetFeatureSplit
from tester import dump_classifier_and_data
from sklearn import preprocessing
import matplotlib.pyplot as plt
import math



axis_x=5
axis_y=4
def Draw(pred, features, poi, mark_poi=True, name="image.png", f1_name="feature 1", f2_name="feature 2"):
    """ some plotting code designed to help you visualize your clusters """

    ### plot each cluster with a different color--add more colors for
    ### drawing more than five clusters
    colors = ["b", "c", "k", "m", "g"]
    for ii, pp in enumerate(pred):
    	if not poi[int(ii)]:
       		plt.scatter(features[int(ii)][axis_x], features[int(ii)][axis_y], color = colors[int(pred[int(ii)])])

	### if you like, place red stars over points that are POIs (just for funsies)
	if mark_poi:
		for ii, pp in enumerate(pred):

			if poi[int(ii)]:
				plt.scatter(features[int(ii)][axis_x], features[int(ii)][axis_y], color="r", marker="*")
    plt.xlabel(f1_name)
    plt.ylabel(f2_name)
    plt.savefig(name)
    plt.show()

### Task 1: Select what features you'll use.
### features_list is a list of strings, each of which is a feature name.
### The first feature must be "poi".
#Feature list
#['salary','to_messages','deferral_payments','total_payments', 'exercised_stock_options', 'bonus', 'restricted_stock', 'shared_receipt_with_poi', 'restricted_stock_deferred', 'total_stock_value', 'expenses', 'loan_advances',
# 'from_messages', 'other', 'from_this_person_to_poi', 'poi', 'director_fees', 'deferred_income', 'long_term_incentive', 'email_address', 'from_poi_to_this_person']
#features_list = ['poi','salary','total_payments','expenses','bonus','total_stock_value','from_this_person_to_poi', 'director_fees', 'deferred_income', 'long_term_incentive','deferral_payments', 'exercised_stock_options', 'bonus', 'restricted_stock', 'shared_receipt_with_poi', 'restricted_stock_deferred', 'total_stock_value', 'expenses' ] # You will need to use more features
features_list=['poi', 'bonus', 'expenses', 'from_messages']
#, 'total_stock_value','deferred_income', 'from_poi_to_this_person'
outliers=['TOTAL','LAY KENNETH L']
### Load the dictionary containing the dataset
with open("final_project_dataset.pkl", "r") as data_file:
    data_dict = pickle.load(data_file)

### Task 2: Remove outliers
### Task 3: Create new feature(s)
### Store to my_dataset for easy export below.
my_dataset = data_dict
maximal =0 
for item in outliers:
	del my_dataset[item]

feature_analyzed='salary'
for elem in my_dataset:
	#if my_dataset[elem]['poi']:
	#	print my_dataset[elem]
	salary = float(my_dataset[elem][feature_analyzed])
	if my_dataset[elem][feature_analyzed]> maximal and not math.isnan(salary) :
		maximal= my_dataset[elem][feature_analyzed]
		elem_remove=elem
print elem_remove
print maximal
print my_dataset[elem_remove]
#my_dataset[elem_remove][feature_analyzed]=0
from sklearn.feature_selection import SelectPercentile
from sklearn.feature_selection import chi2

from sklearn.linear_model import LinearRegression
### Extract features and labels from dataset for local testing

data = featureFormat(my_dataset, features_list, sort_keys = True)
print data
scaler = preprocessing.MinMaxScaler()
data = scaler.fit_transform(data)


labels, features = targetFeatureSplit(data)

### Task 4: Try a varity of classifiers
### Please name your classifier clf for easy export below.
### Note that if you want to do PCA or other multi-stage operations,
### you'll need to use Pipelines. For more info:
### http://scikit-learn.org/stable/modules/pipeline.html

# Provided to give you a starting point. Try a variety of classifiers.


from sklearn.naive_bayes import GaussianNB
from sklearn.svm import LinearSVC, SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report
from sklearn.model_selection import GridSearchCV

param_grid = [
  #{'C': [0.2,0.4,0.6,0.8,1, 10, 100, 1000], 'class_weight':[None,'balanced'] },
  {'class_weight':[None,'balanced'],"max_depth":[1,2,3,5,10,15,20,30,50,20,None] ,"min_samples_leaf":[1,2,3,4,5,6,10],'max_features':[None,"auto","log2"]}
 
 ]

clf = GaussianNB()



### Task 5: Tune your classifier to achieve better than .3 precision and recall 
### using our testing script. Check the tester.py script in the final project
### folder for details on the evaluation method, especially the test_classifier
### function. Because of the small size of the dataset, the script uses
### stratified shuffle split cross validation. For more info: 
### http://scikit-learn.org/stable/modules/generated/sklearn.cross_validation.StratifiedShuffleSplit.html

# Example starting point. Try investigating other evaluation techniques!
from sklearn.model_selection import train_test_split
features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size=0.33, random_state=42)
sel_per=SelectPercentile(chi2,50)
features_train= sel_per.fit_transform(features_train,labels_train)
features_test=sel_per.transform(features_test)
print features_test
grid = GridSearchCV(DecisionTreeClassifier(),param_grid, n_jobs=-1)
grid.fit(features_train,labels_train)
print grid.best_estimator_
clf = LinearSVC(C=0.2, class_weight=None,random_state=65)
clf = DecisionTreeClassifier(max_depth=3,min_samples_leaf=2)

#clf=LinearRegression()
clf.fit(features_train, labels_train)
print clf.score(features_test,labels_test)
preditced_labels = clf.predict(features_test)
print preditced_labels

poi, feature =targetFeatureSplit( data )

#Draw(labels_train, features_train, poi, mark_poi=True, name="image.png", f1_name="feature 1", f2_name="feature 2")
print classification_report(labels_test,preditced_labels)
### Task 6: Dump your classifier, dataset, and features_list so anyone can
### check your results. You do not need to change anything below, but make sure
### that the version of poi_id.py that you submit can be run on its own and
### generates the necessary .pkl files for validating your results.

dump_classifier_and_data(clf, my_dataset, features_list)