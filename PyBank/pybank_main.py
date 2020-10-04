#This will be the main file for the pybank challenge
#Imports

import os
import csv

#define variables to store values in
months = 0
net_profit = float(0.0)
average_change = 0
greatest_increase = 0
greatest_decrease = 0
thismonth = 0
lastmonth = 0
current_change = 0
date1 = ""
date2 = ""


bdata_csv = os.path.join('Resources', 'budget_data.csv')

with open(bdata_csv, newline='') as csvfile:
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    
    #remove header
    header = next(csvfile)
    #print(header)
    
    #calculate total amount of profit/loss by using sum on the second row
    #net_profit = sum(int(r[1]) for r in csvreader)
    #print (net_profit)

     
    for row in csvreader:
        
        #count the months 1/row
        months = months + 1
        #record the total of all values in profits/losses
        net_profit = net_profit + int(row[1])
        #update thismonth
        thismonth = int(row[1])
        #calculate current_change
        current_change = lastmonth-thismonth
        #check if the change between lastmonth and thismonth is the biggest gain yet
        if current_change>0 and current_change>greatest_increase:
            greatest_increase = current_change
            date1= row[0]
        #check if the change between lastmonth and thismonth is the biggest lost yet
        elif current_change<0 and current_change<greatest_decrease:
            greatest_decrease = current_change
            date2 = row[0]

        #update lastmonth
        lastmonth = int(row[1])



    print(months)
    print (net_profit)
    print(date1)
    print(greatest_increase)
    print(date2)
    print(greatest_decrease)


   
    
    
