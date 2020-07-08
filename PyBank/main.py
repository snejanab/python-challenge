# Import modules
import csv
import os
import numpy as np

# Files to load from and output to
load_file = os.path.join("Resources", "budget_data.csv")
output_file = os.path.join("analysis", "budget_analysis.txt")

# Read csv file
with open(load_file) as budget_data:
    reader = csv.reader(budget_data)
    #print(reader)

    # Read header
    header = next(reader)
    

    total_months = 0
    total_profit = 0

    months = []
    profit = []
        
    for row in reader:

        months.append(row[0])
        profit.append(float(row[1]))

        total_months = total_months + 1
        total_profit += int(row [1])
        
       
change_in_profit = np.diff(profit)
list_maxindex = np.where(change_in_profit == max(change_in_profit))
list_minindex = np.where(change_in_profit == min(change_in_profit))


max_value = change_in_profit[int(list_maxindex[0])]
max_month = months[int(list_maxindex[0])+1]

min_value = change_in_profit[int(list_minindex[0])]
min_month = months[int(list_minindex[0])+1]


output_header= (f"Financial Analysis\n"
f"-------------------------\n"
f"Total Months: {len(months)}\n"
f"Total Profit: ${total_profit}\n"
f"Greatest Increase In Profits: {max_month} (${int(max_value)})\n"
f"Greatest Decrease In Profits: {min_month} (${int(min_value)})\n")

with open(output_file, "w") as output_data:

    output_data.write(output_header) 

print(f"Total Months: {len(months)}")
print(f"Total Profit: ${total_profit}")
print(f"Greatest Increase In Profits: {max_month} (${int(max_value)})")
print(f"Greatest Decrease In Profits: {min_month} (${int(min_value)})")


