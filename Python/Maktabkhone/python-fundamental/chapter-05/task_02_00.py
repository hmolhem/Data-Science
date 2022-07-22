import csv
from statistics import mean

with open('average.csv') as csvfile:
    reader = csv.reader(csvfile)
    averages = [ (row[0],float(row[1])) for row in reader]
# sorted with respect to name
averages = sorted(averages, key= lambda x: x[0])

with open('test.csv', 'w', newline='') as csvfile:
    obj = csv.writer(csvfile)
    for average in averages:
        obj.writerow(average)
    csvfile.close()


    

