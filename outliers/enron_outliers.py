#!/usr/bin/python

import pickle
import sys

import matplotlib.pyplot
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit


### read in data dictionary, convert to numpy array
data_dict = pickle.load( open("../final_project/final_project_dataset.pkl", "r") )

data_dict.pop("TOTAL",0) #remove TOTAL outlier
features = ["salary", "bonus"]
data = featureFormat(data_dict, features)


max_salary =0
bandit_outlier=[]
for salary, bonus in data:
	if salary > max_salary:
		max_salary= salary

	if bonus > 5000000 and salary > 1000000:
		bandit_outlier.append((salary,bonus))
### your code below



for key in data_dict:
	if data_dict[key]["salary"] == max_salary:
		max_salary_name=key
		

	if (data_dict[key]["salary"],data_dict[key]["bonus"]) in bandit_outlier:
		print "bandit name :{}".format(key)
	
print "the MAX salary is : {}".format(max_salary_name)


for point in data:
    salary = point[0]
    bonus = point[1]
    matplotlib.pyplot.scatter( salary, bonus )

matplotlib.pyplot.xlabel("salary")
matplotlib.pyplot.ylabel("bonus")
matplotlib.pyplot.show()