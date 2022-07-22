import csv
import hashlib
from collections import OrderedDict
    
with open('values.csv', 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    
    for row in reader:
        print(row['min'], row['avg'], row['max'])
