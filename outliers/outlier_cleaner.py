#!/usr/bin/python


def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error).
    """
    
    data_len = len(predictions)
    data=[]    
    
    for pred,age, net  in zip(predictions, ages, net_worths):
        data.append((age, net, pred - net)) #error = pred-net 

    sorted_data= sorted(data, key=lambda tup:tup[2]) #sort by error
    new_data_len = int(round(data_len*0.9))

    cleaned_data = sorted_data[:new_data_len]
    
    return cleaned_data

