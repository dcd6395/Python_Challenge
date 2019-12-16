import os
import csv

csvpath = os.path.join('budget_data.csv')
file_to_output = os.path.join("budget_analysis.txt")

# track totals
total = 0
total_change = []
total_months = 0
monthly_change = []
prev_total = 0
increase = 0
decrease = 0


with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)

#find total months, increase and decrease, average
    for row in csvreader:
        total_months+= 1
        total = total + int(row[1])
        prev_total = int(row[1])
        total_change = int(row[1]) - prev_total
        monthly_change = monthly_change + int(row[0])

        if (total_change > increase[1]):
            increase[0] = row[0]
            increase[1] = total_change
        else:
            decrease[0] = row[0]
            decrease = total_change
    sum_total = sum(total_change)
    len_total = len(total_change)
    total_average = (sum_total / len_total)


output = (
    f"\nFinancial Analysis\n"
    f"-----------------\n"
    f"Total Months: {total_months}\n"
    f"Average Change: {total_average}\n"
    f"Greatest Increase in Profits: {increase}\n"
    f"Greatest Decrease in Profits: {decrease}\n")

# Print all of the results (to terminal)
print(output)

# Save the results to analysis text file
with open(file_to_output, "a") as txt_file:
    txt_file.write(output)









        



