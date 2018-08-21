# Kenneth Reed
# Data Science T-Th HW3
# PyBank

import os
import csv
import functools


budget_data_csv = os.path.join("Resources", "budget_data.csv")

with open(budget_data_csv, newline='') as csvfile:

	# CSV reader specifies delimiter and variable that holds contents
	csvreader = csv.reader(csvfile, delimiter=',')
	header = next(csvreader, None)
	#budget_list = list(csvreader)
	budget_list = [[row[0], int(row[1])] for row in csvreader]
	#print(budget_list)
	
	profits = [profit for (month, profit) in budget_list]
	print("----------------------------")
	print(profits)
	total = sum(profits)
	totalMonths = len(budget_list)
	avgChange = round(total/totalMonths, 2)
	
	# Check max and min increase to compare
	maxIncrease = max(profits)
	minDecrease = min(profits)
	print(maxIncrease)
	print(minDecrease)
	
	maxMonth = max(budget_list, key=lambda x: x[1])
	#print(maxMonth)
	minMonth = min(budget_list, key=lambda x: x[1])
	#print(minMonth)
	
	print(*maxMonth[0], maxMonth[1], sep="")
	print(''.join(str(maxMonth)))
	

	
		
print("Financial Analysis")
print("----------------------------")
print("Total Months: " + str(totalMonths))
print("Total: $" + str(total))
print("Average Change: $" + str(avgChange))
print("Greatest Increase in Profits: " + str(maxMonth))
print("Greatest Decrease in Profits: " + str(minMonth))

