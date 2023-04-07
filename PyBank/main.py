# Import OS and CSV

import os
import csv

csvpath = os.path.join("PyBank", "Resources", "budget_data.csv")

# Output text file
outputtxt_path = "PyBankoutput.txt"

# Opens the csv file

with open("Resources/budget_data.csv") as csvfile:

    csvreader = csv.reader(csvfile, delimiter=",")
# Skips header row
    csv_reader = next(csvreader)

# Setting variables
    totalmonths = []
    totalprofit = []
    profitCHANGE = []
    month = []

# Putting row contents into lists
    for row in csvreader:
        totalmonths.append(row[0])
        totalprofit.append(int(row[1]))

# Iterating through to add profit fluctuations into list
    for i in range(len(totalprofit)-1):
        profitCHANGE.append(totalprofit[i+1]-totalprofit[i])


        #month = [month] + [row[0]] trying to get the month to appear :/
# Getting the maximum and minimum amounts from list
        increaseprof = max(profitCHANGE)
        decreaseprof = min(profitCHANGE)


        monthincrease = profitCHANGE.index(max(profitCHANGE))+1
        monthdecrease = profitCHANGE.index(min(profitCHANGE))+1

# Printing out results
    print("Financial Analysis")
    print("------------------------")
    print(f"Total Months : {len(totalmonths)}")
    print(f"Total: ${sum(totalprofit)}")
    print(f"Average Change: {round(sum(profitCHANGE)/len(profitCHANGE),2)}")
    print(f"Greatest Increase in Profits: ${max(profitCHANGE)} in ")
    print(f"Greatest Decrease in Profits: ${min(profitCHANGE)} in ")



with open(outputtxt_path, 'w') as txt:
    txt.write("Financial Analysis")
    txt.write("\n")
    txt.write("------------------------")
    txt.write("\n")
    txt.write(f"Total Months : {len(totalmonths)}")
    txt.write("\n")
    txt.write(f"Total: ${sum(totalprofit)}")
    txt.write("\n")
    txt.write(f"Average Change: {round(sum(profitCHANGE)/len(profitCHANGE),2)}")
    txt.write("\n")
    txt.write(f"Greatest Increase in Profits: ${max(profitCHANGE)} in ")
    txt.write("\n")
    txt.write(f"Greatest Decrease in Profits: ${min(profitCHANGE)} in ")
