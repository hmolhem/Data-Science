import csv
from statistics import mean

averages = list()
with open('source-01.csv') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        name = row[0]
        these_grades = list()
        for grade in row[1:]:
            these_grades.append(float(grade))
        average = (name,mean(these_grades))
        averages.append(average)

with open('averages.csv', 'w', newline='') as csvfile:
    obj =  csv.writer(csvfile)
    for average in averages:
        obj.writerow(average)
    csvfile.close()




