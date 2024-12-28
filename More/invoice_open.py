import csv
import pandas as pd

# rows = []
# with open("Invoice.csv", 'r') as file:
#     csvreader = csv.reader(file)
#     header = next(csvreader)
#     for row in csvreader:
#         rows.append(row)
# print(header)
# print(rows)

data= pd.read_csv("Invoice.csv")
print(data.columns)
print(data.Purchase)