# Kenneth Reed
# Data Science T-Th HW3
# PyPoll

import os
import csv

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

	# Use list comprehension to read in voter ids and candidates
	voter_ids = [voter_ids for (voter_ids, county, candidate) in votes]
	candidates = [candidate for (voter_ids, county, candidate) in votes]

	# Use len to count rows for voter ids; assumes no duplicates
	totalVotes = len(voter_ids) 
	
	# Main block to print out results
	print("Election Results")
	print("----------------------------")
	print(f"Total Votes: {totalVotes}")
	print("----------------------------")
	

	# save the output file path
	output_file = os.path.join("output.txt")
	file = open(output_file, "w")
	
	file.write("Election Results\n")
	file.write("----------------------------\n")
	file.write(f"Total Votes: {totalVotes}\n")
	file.write("----------------------------\n")
	
	# Function code for unique values from web
	def unique(list):

	# intilize a null list
		unique_list = []

		# traverse for all elements
		for x in list:
			# check if exists in unique_list or not
			if x not in unique_list:
				unique_list.append(x)
		# print list
		#for x in unique_list:
			#print(x),
		#print(unique_list)

		summary = []
		sumB = []
		for item in unique_list:
			CandidateVotes = []
			summary.append(item)
			# Loop through looking for the votes
			for row in votes:
				if row[2] == item:
					CandidateVotes.append(1)
			totalCVotes = len(CandidateVotes)
			percentage = round(totalCVotes/totalVotes * 100, 3)

			
			print(f"{item}: {percentage}% ({totalCVotes})")
			sumB.append(totalCVotes)

			file.write(f"{item}: {percentage}% ({totalCVotes})\n")

		#print(summary)
		zipped = zip(summary, sumB)
		#map(max, zip(zipped))

		#print(max(sumB))
		for name, number in zipped:
			if number == max(sumB):
				winner = name
		print("----------------------------")
		print(f"Winner: {winner}")
		print("----------------------------")

		file.write("----------------------------\n")
		file.write(f"Winner: {winner}\n")
		file.write("----------------------------\n")

		file.close()

	list = candidates
	unique(list)
