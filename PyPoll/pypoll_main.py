#This will be the main file for the pypoll challenge
#Imports
import os
import csv
import sys
import subprocess

#define variables
""" You will be give a set of poll data called election_data.csv. 
The dataset is composed of three columns: Voter ID, County, and Candidate. 
Your task is to create a Python script that analyzes the votes and calculates each of the following:
The total number of votes cast
A complete list of candidates who received votes
The percentage of votes each candidate won
The total number of votes each candidate won
The winner of the election based on popular vote.
As an example, your analysis should look similar to the one below:
Election Results
-------------------------
Total Votes: 3521001
-------------------------
Khan: 63.000% (2218231)
Correy: 20.000% (704200)
Li: 14.000% (492940)
O'Tooley: 3.000% (105630)
-------------------------
Winner: Khan """
#saving a reference to original standard output
original_stdout = sys.stdout

edata_csv = os.path.join("Resources", "election_data.csv")

with open (edata_csv, newline='') as csvfile:
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    #remove header
    header = next(csvfile)



# make dictionaries with names as the key, and the number of times that name appears in the dataset? or something like that
