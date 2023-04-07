# Import OS and CSV

import os
import csv

csvpath = os.path.join("PyPoll", "Resources", "election_data.csv")

# Output text file
outputtxt_path = "PyPolloutput.txt"

# Opens the csv file

with open("Resources/election_data.csv") as csvfile:

    csvreader = csv.reader(csvfile, delimiter=",")

# Skips header row

    csv_reader = next(csvreader)

    votetotal = 0
    stockham = 0
    degette = 0
    doane = 0

    for row in csv_reader:
        votetotal =+ 1
        
        if row[2] == "Charles Casper Stockham": 
            stockham +=1
        elif row[2] == "Diana DeGette":
            degette +=1
        elif row[2] == "Raymon Anthony Doane": 
            doane +=1
    candidates = ["Charles Casper Stockham", "Diana DeGette", "Raymon Anthony Doane"]
    tallies = [stockham, degette, doane]
    outcome = dict(zip(candidates, tallies))
    key = max(outcome, key=outcome.get)
 


print("Election Results")
print("------------------------")
print(f"Total Votes: {votetotal}")
print(f"Charles Casper Stockham : ({stockham})")
