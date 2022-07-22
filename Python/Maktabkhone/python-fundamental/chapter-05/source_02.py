import csv
# For the average
from statistics import mean 

# read data from csv file

# write name and average in csv file
# task 01
def calculate_averages(input_file_name, output_file_name):
    averages = list()
    with open(input_file_name) as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            name = row[0]
            these_grades = list()
            for grade in row[1:]:
                these_grades.append(float(grade))
            average = (name,mean(these_grades))
            averages.append(average)
            
    with open(output_file_name, 'w', newline='') as csvfile:
        obj =  csv.writer(csvfile)
        for average in averages:
            obj.writerow(average)
        csvfile.close()
    
# write sort data with respect to score and name
# task 02
def calculate_sorted_averages(input_file_name, output_file_name):

    with open(input_file_name) as csvfile:
        reader = csv.reader(csvfile)
        averages = [ (row[0],float(row[1])) for row in reader]
    # sorted with respect to name
    averages = sorted(averages, key= lambda x: (x[1],x[0]))
    
    # write sorted average in file 
    with open(output_file_name, 'w', newline='') as csvfile:
        obj = csv.writer(csvfile)
        for average in averages:
            obj.writerow(average)
        csvfile.close()

# write three best score
def calculate_three_best(input_file_name, output_file_name):
    with open(input_file_name) as csvfile:
        reader = csv.reader(csvfile)
        averages = [ (row[0],float(row[1])) for row in reader]
        averages = sorted(averages, key=lambda x: (x[1],x[0]), reverse=True)
        three_best = averages[:3]

    with open(output_file_name, 'w', newline='') as csvfile:
        obj = csv.writer(csvfile)
        for average in three_best:
            obj.writerow(average)
        csvfile.close()

# write three worst score
def calculate_three_worst(input_file_name, output_file_name):
    with open(input_file_name) as csvfile:
        reader = csv.reader(csvfile)
        averages = [ tuple(row) for row in reader]
        three_worsts = averages[:3]
        three_worsts = [ three_worst[1] for three_worst in three_worsts]

    with open(output_file_name, 'w', newline='') as csvfile:
        obj = csv.writer(csvfile)
        for three_worst in three_worsts:
            obj.writerow([three_worst])
        csvfile.close()

# write average of average score
def calculate_average_of_averages(input_file_name, output_file_name):
    with open(input_file_name) as csvfile:
        reader = csv.reader(csvfile)
        data = [ (row[0],float(row[1])) for row in reader]
        data = sorted(data, key=lambda x: x[1], reverse=True)
        scores = [datum[1] for datum in data]
        average = mean(scores)
      
    with open(output_file_name, 'w', newline='') as csvfile:
        obj = csv.writer(csvfile)
        obj.writerow([average])
        csvfile.close()


calculate_averages('source-01.csv', 'task01.csv') #task01
calculate_sorted_averages('source-01.csv', 'task02.csv') #task02
# calculate_three_best('task02.csv','task03.csv') #task03
# calculate_three_worst('task02.csv','task04.csv') #task04
# calculate_average_of_averages('task02.csv','task05.csv') # task05
