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
	votes = [[row[0], row[1], row[2]] for row in csvreader]
	#print(votes) 

	# Use list comprehension to read in voter ids
	voter_ids = [voter_ids for (voter_ids, county, candidate) in votes]

	# Use len to count rows for voter ids; assumes no duplicates
	totalVotes = len(voter_ids) 
	print(totalVotes)
	
	CorreyVotes = []
	# Loop through looking for the votes
	for row in votes:
		if row[2] == "Correy":
				CorreyVotes.append(1)
		totalCVotes = len(CorreyVotes)
	print(totalCVotes)
	
	KhanVotes = []
	# Loop through looking for the votes
	for row in votes:
		if row[2] == "Khan":
				KhanVotes.append(1)
		totalKVotes = len(KhanVotes)
	print(totalKVotes)
	
	LiVotes = []
	# Loop through looking for the votes
	for row in votes:
		if row[2] == "Li":
				LiVotes.append(1)
		totalLVotes = len(LiVotes)
	print(totalLVotes)

	OTooleyVotes = []
	# Loop through looking for the votes
	for row in votes:
		if row[2] == "O'Tooley":
				OTooleyVotes.append(1)
		totalOVotes = len(OTooleyVotes)
	print(totalOVotes)

# save the output file path
#output_file = os.path.join("output.csv")

#with open(output_file, "w", newline="") as datafile:
	#writer = csv.writer(datafile)

	#writer.writerow(["Voter ID", "County", "Candidate"])

	#writer.writerows(poll_list)


