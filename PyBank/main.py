import os
import csv

file_to_load = os.path.join("Resources", "budget_data.csv")
file_to_output = os.path.join("PyBank", "PyBank_analysis.csv")



with open(file_to_load, newline = '') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
