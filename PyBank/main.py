# Kenneth Reed
# Data Science T-Th HW3
# PyBank

import os
import csv
import numpy as np

# Use os library to point to csv files
budget_data_csv = os.path.join("Resources", "budget_data.csv")

# Use with open to read csv
with open(budget_data_csv, newline='') as csvfile:

	# CSV reader specifies delimiter and variable that holds csv contents
	csvreader = csv.reader(csvfile, delimiter=',')
	header = next(csvreader, None)
	#budget_list = list(csvreader) 

	# Variable to create tuple from each row
	budget_list = [[row[0], int(row[1])] for row in csvreader]
	#print(budget_list) 

	# Use list comprehension to read in budget list
	profits = [profit for (month, profit) in budget_list]
	#print("----------------------------")
	#print(profits) 

	# Use len to count rows for total months
	totalMonths = len(budget_list) 

	# Sum the rows for total profit
	total = sum(profits) 
	
	# Added new code to find average change using numpy; 
	# numpy.diff calculates difference between profit elements
	monthlyChange = np.diff(profits)
	#print(monthlyChange)
	
	# Total the monthly change
	totalChange = sum(monthlyChange)
	#print(totalChange)
	
	# Calculate the number of monthly change items
	changeMonths = len(monthlyChange) 
	#print(changeMonths)
	
	# Calculate the average of monthly change, rounded to 2 places
	averageChange = round(totalChange/changeMonths, 2)
	#print(averageChange)
	
	# Check max and min increase to compare for testing
	#maxIncrease = max(profits)
	#minDecrease = min(profits) 

	# Use one-line function to get the max of the second index value
	maxMonth = max(budget_list, key=lambda x: x[1])

	# Use one-line function to get the min of the second index value
	minMonth = min(budget_list, key=lambda x: x[1])
	 
# Main block to print out results
print("Financial Analysis")
print("----------------------------")

# Use string on variable, concatenate with text
print(f"Total Months: {totalMonths}")

# Use f-string to simplify with total
print(f"Total: ${total}")

# Use f-string again for average change
print(f"Average Change: ${averageChange}")

# Use f-string again for increase; pull out indexes of variable to display as needed
print(f"Greatest Increase in Profits: {maxMonth[0]} (${maxMonth[1]})")

# Use f-string again for decrease; pull out indexes of variable to display as needed
print(f"Greatest Decrease in Profits: {minMonth[0]} (${minMonth[1]})")

