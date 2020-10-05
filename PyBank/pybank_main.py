#This will be the main file for the pybank challenge
#Imports
import os
import csv
import sys
import subprocess

#define variables to store values in
net_profit = 0.0
average_change_list = []
average_change = float(0.0)
greatest_increase = 0
greatest_decrease = 0
thismonth = 0
lastmonth = 0
current_change = 0
date1 = ""
date2 = ""

original_stdout = sys.stdout #saving a reference to original standard output


bdata_csv = os.path.join('Resources', 'budget_data.csv')

with open(bdata_csv, newline='') as csvfile:
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    #remove header
    header = next(csvfile)
     
    for row in csvreader:
        #record the total of all values in profits/losses
        net_profit = net_profit + int(row[1])
        #update thismonth
        thismonth = int(row[1])
        #calculate current_change, if statement to deal with subtracting negative numbers
        current_change = thismonth-lastmonth
        if thismonth<0 and lastmonth<0:
            current_change = thismonth+lastmonth
        #add current_change value to list to calculate average later, if statement for the first iteration (85 differences between 86 numbers)
        if lastmonth != 0:
            average_change_list.append(current_change)
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
        
    #calculate average change, confused where the example on gitlab got the average: 2315.12
    #would like to know what I did wrong if this isn't correct
    average_change = sum(average_change_list)/len(average_change_list)

    #changed stdout to create a txt file with the output I want
    with open('Financial_Analysis.txt', 'w') as o:
        sys.stdout = o
        print(' ')
        print('Financial Analysis')
        print('--------------------------------------------')
        print('Total Months: ' + str(len(average_change_list)+1))
        print('Total: ' + str(net_profit))
        print('Average change: ' + str(round(average_change, 2)))
        print('Greatest increase in profits: ' + date1 + ' ' + str(greatest_increase))
        print('Greatest decrease in profits: ' + date2 + ' ' + str(greatest_decrease))
        print(' ')
        sys.stdout = original_stdout

    #print normal output
    print(' ')
    print('Financial Analysis')
    print('--------------------------------------------')
    print('Total Months: ' + str(len(average_change_list)+1))
    print('Total: ' + str(net_profit))
    print('Average change: ' + str(round(average_change, 2)))
    print('Greatest increase in profits: ' + date1 + ' ' + str(greatest_increase))
    print('Greatest decrease in profits: ' + date2 + ' ' + str(greatest_decrease))
    print(' ')


   
    
    
