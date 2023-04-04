# Import OS and CSV

import os
import csv

csvpath = os.path.join("Resources", "budget_data.csv")
with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=",")

    for row in csvreader: 
        print (row) 


#[float(row["Date"]) for row in csvfile]

#Total_Months = len(list)
#print(Total_Months)

#copy above code for listing profit/loss and create a function that adds the entire list together
#print list


