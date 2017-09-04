#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle

STOCK='total_stock_value'

USER_PRENTICE='PRENTICE JAMES'
USER_COLWELL ='COLWELL WESLEY'
USER_SKILLING='SKILLING JEFFREY K'
USER_FASTOW='FASTOW ANDREW S'
USER_LAY='LAY KENNETH L'

FEATURE_TO_POI='from_this_person_to_poi'
FEATURE_EX_STOCK_OPTIONS='exercised_stock_options'
FEATURE_PAYMENT='total_payments'
FEATURE_EMAIL='email_address'
FEATURE_SALARY='salary'
FEATURE_POI='poi'

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))


print "number of entries in the dataset: {}".format(len(enron_data))


print "number of features: {}".format(len(enron_data[USER_PRENTICE]))
poi_count=0
salary_feature_count=0
email_feature_count=0
payment_feature_count=0
payment_feature_poi_count=0
total_number_of_users = len(enron_data)

for key in enron_data:
	if enron_data[key][FEATURE_SALARY] != 'NaN':
		salary_feature_count+=1

	if enron_data[key][FEATURE_PAYMENT] != 'NaN':
		payment_feature_count+=1
		if enron_data[key][FEATURE_POI] ==1:
			payment_feature_poi_count+=1

	if enron_data[key][FEATURE_EMAIL] != 'NaN':
		email_feature_count+=1

	if enron_data[key][FEATURE_POI]==1:
		poi_count+=1


nan_payment= total_number_of_users - payment_feature_count
nan_poi_payment = poi_count - payment_feature_poi_count

percentage_poi_NaN_payment = ((100/float(poi_count)))*nan_poi_payment
percentage_NaN_payment = ((100/float(total_number_of_users)))*nan_payment


print "percentage of payment feature valued with NaN: {}% ".format(percentage_NaN_payment)
print "percentage of poi's payment feature valued with NaN: {}% ".format(percentage_poi_NaN_payment)

print "new number of data points :{} ".format(total_number_of_users + 10) 
print "new dataset number of NaN payment {} ".format(nan_payment+10)
print "number of poi features : {}".format(poi_count)
print "number of salary features : {}".format(salary_feature_count)
print "number of email features : {}".format(email_feature_count)

with open('../final_project/poi_names.txt',"r") as poi_file:
	poi_count =0
	for line in poi_file:
		if line[0]=='(':
			poi_count+=1


print "number of poi in the txt file : {}".format(poi_count)


print "number of stock for "+USER_PRENTICE+" :{}".format(enron_data[USER_PRENTICE][STOCK])

print "number of mail from "+USER_COLWELL+" to poi :{}".format(enron_data[USER_COLWELL][FEATURE_TO_POI])

print "number of stock options execised by "+USER_SKILLING+" :{}".format(enron_data[USER_SKILLING][FEATURE_EX_STOCK_OPTIONS])


best_thief=""
best_ammount=0

thief_list=[USER_SKILLING, USER_FASTOW,USER_LAY]

for user in thief_list:
	if enron_data[user][FEATURE_PAYMENT] > best_ammount:
		best_ammount  =enron_data[user][FEATURE_PAYMENT]
		best_thief=user

print "the best thief is {} with {}".format(best_thief, best_ammount)