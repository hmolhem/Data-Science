import csv
# For the average
from statistics import mean 

def calculate_averages(input_file_name, output_file_name):
    with open(input_file_name) as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            name = row[0]
            these_grades = list()
            for grade in row[1:]:
                these_grades.append(float(grade))
            # print(name,mean(these_grades))
            # print([name,str(mean(these_grades))])    
            average = [name,str(mean(these_grades))]
            f = open(output_file_name,'a')
            f.writelines([name,', ',str(mean(these_grades)),'\n'])
            f.close()
    


def calculate_sorted_averages(input_file_name, output_file_name):
    


def calculate_three_best(input_file_name, output_file_name):
    


def calculate_three_worst(input_file_name, output_file_name):
    


def calculate_average_of_averages(input_file_name, output_file_name):
    


