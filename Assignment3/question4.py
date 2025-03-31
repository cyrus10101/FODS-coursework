# Program that read csv file and display it in tabular format.
# Importing csv to use csv.reader() method.
import csv
# Imoporting tabulate from tabulate to display output in tabular form .
from tabulate import tabulate

# Opening file in readmode.
with open('tabular.csv', 'r', newline='', encoding='utf-8') as file:
    reader = csv.reader(file)
    data = list(reader)

# Displaying ouput in tabular form.
if data: 
    print(tabulate(data[1:], headers = data[0], tablefmt="fancy_grid"))
else:
    print('file is empty!')

