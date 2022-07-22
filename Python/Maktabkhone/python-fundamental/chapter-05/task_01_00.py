import csv
from statistics import mean

with open('source-01.csv') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        name = row[0]
        these_grades = list()
        for grade in row[1:]:
            these_grades.append(float(grade))
        # print(name,mean(these_grades))
        # print([name,str(mean(these_grades))])    
        average = [name,str(mean(these_grades))]
        f = open('task01.txt','a')
        f.writelines([name,', ',str(mean(these_grades)),'\n'])
        f.close()