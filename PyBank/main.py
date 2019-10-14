import csv
import os

row_count = 0
csvpath = os.path.join('Resources', 'budget_data.csv')

#loop read
for row in csvpath:
    row_count = row_count + 1


#count total rows (months)
#row_count = sum(1 for row in csvpath)
print(f"There's a total of {row_count}")
