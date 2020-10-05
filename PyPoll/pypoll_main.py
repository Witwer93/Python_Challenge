#This will be the main file for the pypoll challenge
#Imports
import os
import csv
import sys
import subprocess

#define variables
votes = 0

percent_votes_Li = 0
percent_votes_Cy = 0
percent_votes_Oy = 0
percent_votes_Kn = 0
winner = ""
Li = 0
Kn = 0
Cy = 0
Oy = 0


#saving a reference to original standard output
original_stdout = sys.stdout

edata_csv = os.path.join("Resources", "election_data.csv")

with open (edata_csv, newline='') as csvfile:
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    #remove header
    header = next(csvfile)

    for row in csvreader:
        #I decided to just count the names each time they appeared
        #I get the sense we were supposed to put a dictionary together with total votes and percentage of votes being attached to each name(key)
        #This works, but I don't know how efficient it is, especially given the final print statement
        if str(row[2]) == "Khan":
            Kn += 1
        elif str(row[2]) == "Correy":
            Cy += 1
        elif str(row[2]) == "Li":
            Li += 1
        elif str(row[2]) == "O'Tooley":
            Oy += 1
        
        if str(row[2]) != "Khan" and str(row[2]) != "Correy" and str(row[2]) != "Li" and str(row[2]) != "O'Tooley":
            print("They got you") 
    #calculate total votes
    votes = Kn+Li+Oy+Cy
    #calculate percentage of votes for each candidate
    percent_votes_Cy = (Cy/votes) * 100
    percent_votes_Kn = (Kn/votes) * 100
    percent_votes_Oy = (Oy/votes) * 100
    percent_votes_Li = (Li/votes) * 100

    #This is where i'm guessing I could use a dictionary to find the max votes
    #and then return the key instead of having a long if statement to determine the winner
    if Kn > Li and Kn > Cy and Kn > Oy:
        winner = "Khan"
    elif Li > Kn and Li > Cy and Li > Oy:
        winner = "Li"
    elif Cy > Kn and Cy > Li and Cy > Oy:
        winner = "Correy"
    elif Oy > Kn and Oy > Li and Oy > Cy:
        winner = "O'Tooley"

    #Export output to txt file
    with open('Financial_Analysis.txt', 'w') as o:
        sys.stdout = o
        print(" ")
        print("Election Results")
        print("-------------------------")
        print("Total votes: " + str(votes))
        print("-------------------------")
        print('khan: ' + str(round(percent_votes_Kn, 2)) + '% | ' + str(Kn) + ' ~ total votes')
        print('Correy: ' + str(round(percent_votes_Cy, 2)) + '% | ' + str(Cy)+ ' ~ total votes')
        print('Li: ' + str(round(percent_votes_Li, 2)) + '% | ' + str(Li)+ ' ~ total votes')
        print("O'Tooley: " + str(round(percent_votes_Oy, 2)) + "% | " + str(Oy)+ ' ~ total votes')
        print("-------------------------")
        print("WINNER: " + winner)
        print(" ")
        sys.stdout = original_stdout

    #Final print statement
    print(" ")
    print("Election Results")
    print("-------------------------")
    print("Total votes: " + str(votes))
    print("-------------------------")
    print('khan: ' + str(round(percent_votes_Kn, 2)) + '% | ' + str(Kn) + ' ~ total votes')
    print('Correy: ' + str(round(percent_votes_Cy, 2)) + '% | ' + str(Cy)+ ' ~ total votes')
    print('Li: ' + str(round(percent_votes_Li, 2)) + '% | ' + str(Li)+ ' ~ total votes')
    print("O'Tooley: " + str(round(percent_votes_Oy, 2)) + "% | " + str(Oy)+ ' ~ total votes')
    print("-------------------------")
    print("WINNER: " + winner)
    print(" ")
