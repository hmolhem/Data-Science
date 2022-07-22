import csv
from statistics import mean

with open('sorted_averages.csv') as csvfile:
    reader = csv.reader(csvfile)
    averages = [ (row[0],float(row[1])) for row in reader]
    averages = sorted(averages, key=lambda x: x[1], reverse=True)
    three_best = averages[:3]


with open('three.csv', 'w', newline='') as csvfile:
    obj = csv.writer(csvfile)
    for average in three_best:
        obj.writerow(average)
    csvfile.close()


    

