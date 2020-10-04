#This will be the main file for the pybank challenge
#Imports

import os
import csv

#define variables to store values in
#months = 0
net_profit = 0
average_change = 0
greatest_increase = 0
greatest_decrease = 0

bdata_csv = os.path.join('Resources', 'budget_data.csv')

with open(bdata_csv, newline='') as csvfile:
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    
    #create a list for each row in the csv file, which can then be counted easily
    # -1 because of the headers
    months = len(list(csvreader))-1
    print (months)
    for row in csvreader:
        