# Kenneth Reed
# Data Science T-Th HW3
# PyPoll

import os
import csv
import numpy as np

# Use os library to point to csv files
poll_data_csv = os.path.join("Resources", "election_data.csv")

# Use with open to read csv
with open(poll_data_csv, newline='') as csvfile:

	# CSV reader specifies delimiter and variable that holds csv contents
	csvreader = csv.reader(csvfile, delimiter=',')
	header = next(csvreader, None)
	#poll_list = list(csvreader) 

	# Variable to create tuple from each row
	poll_list = [[row[0], row[1], row[2]] for row in csvreader]
	print(poll_list) 

