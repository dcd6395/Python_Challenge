import os
import csv

csvpath = os.path.join('budget_data.csv')
file_to_output = os.path.join("budget_analysis.txt")

# track totals
months = []
total = 0
total_change = []
change = 0
total_months = 0
total_pl = []
monthly_change = 0
prev_total = 0
increase = 0
decrease = 0


with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)

#find total months, increase and decrease, average (need to calculate total change)
    for row in csvreader:
        months.append(row[0])
        total_pl.append(int(row[1]))
        total_months+= 1
        total = total + int(row[1])
        prev_total = int(row[1])
        increase = int(row[1]) - prev_total
        

average_change = round(total_change/total_months)
greatest_inc = max(total_change)
greatest_dec = min(total_change)


output = (
    f"\nFinancial Analysis\n"
    f"-----------------\n"
    f"Total Months: {total_months}\n"
    f"Average Change: {average_change}\n"
    f"Greatest Increase in Profits: {greatest_inc}\n"
    f"Greatest Decrease in Profits: {greatest_dec}\n")

# Print all of the results (to terminal)
print(output)

# Save the results to analysis text file
with open(file_to_output, "a") as txt_file:
    txt_file.write(output)









        



