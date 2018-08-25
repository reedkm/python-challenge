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

	# Save the output file path
	output_file = os.path.join("election_results.txt")
	file = open(output_file, "w")

	# Main block to save results to text
	file.write("Election Results\n")
	file.write("----------------------------\n")
	file.write(f"Total Votes: {totalVotes}\n")
	file.write("----------------------------\n")

	# Function code for unique values from web; use to find distinct candidates
	def unique(list):

	# Set empty list
		unique_list = []

		# Loop to check all items in list
		for x in list:
			# check if candidate already exists; if not append
			if x not in unique_list:
				unique_list.append(x)

		# Set empty list to contain distinct candidates
		summary = []
		# Set empty list to contain candidate vote totals
		sumB = []
		for item in unique_list:
			# Set empty list to contain votes to count
			CandidateVotes = []
			summary.append(item)
	
			# Loop through looking for the votes
			for row in votes:
				if row[2] == item:
					CandidateVotes.append(1)
			totalCVotes = len(CandidateVotes)
			percentage = round(totalCVotes/totalVotes * 100, 3)

			# Print out each candidate, percentage, and their vote totals
			print(f"{item}: {percentage}% ({totalCVotes})")
			sumB.append(totalCVotes)

			# Write out each candidate results to text
			file.write(f"{item}: {percentage}% ({totalCVotes})\n")

		# zip candidate and their votes together to look for winner
		zipped = zip(summary, sumB)

		# For loop to check for winner
		for name, number in zipped:
			if number == max(sumB):
				winner = name
		
		# Print out winner
		print("----------------------------")
		print(f"Winner: {winner}")
		print("----------------------------")

		# Write out winner to file
		file.write("----------------------------\n")
		file.write(f"Winner: {winner}\n")
		file.write("----------------------------\n")

		# Close file
		file.close()

	unique(candidates)
