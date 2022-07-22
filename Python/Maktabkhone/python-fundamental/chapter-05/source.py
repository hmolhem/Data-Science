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
            average = (name, mean(these_grades))
            averages.append(average)

    with open(output_file_name, 'w', newline='') as csvfile:
        obj = csv.writer(csvfile)
        for average in averages:
            obj.writerow(average)
        csvfile.close()


# write sort data with respect to score and name
# task 02
def calculate_sorted_averages(input_file_name, output_file_name):
    averages = list()
    with open(input_file_name) as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            name = row[0]
            these_grades = list()
            for grade in row[1:]:
                these_grades.append(float(grade))
            average = (name, mean(these_grades))
            averages.append(average)

    averages = sorted(averages, key=lambda x: (x[1], x[0]))

    # write sorted average in file
    with open(output_file_name, 'w', newline='') as csvfile:
        obj = csv.writer(csvfile)
        for average in averages:
            obj.writerow(average)
        csvfile.close()


# write three best score
# task 03
def calculate_three_best(input_file_name, output_file_name):
    averages = list()
    with open(input_file_name) as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            name = row[0]
            these_grades = list()
            for grade in row[1:]:
                these_grades.append(float(grade))
            average = (name, mean(these_grades))
            averages.append(average)

        averages = sorted(averages, key=lambda x: x[1], reverse=True)
        three_best = averages[:3]

    with open(output_file_name, 'w', newline='') as csvfile:
        obj = csv.writer(csvfile)
        for ele in three_best:
            obj.writerow(ele)
        csvfile.close()


# write three worst score
# task 04
def calculate_three_worst(input_file_name, output_file_name):
    averages = list()
    with open(input_file_name) as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            name = row[0]
            these_grades = list()
            for grade in row[1:]:
                these_grades.append(float(grade))
            average = (name, mean(these_grades))
            averages.append(average)

        averages = sorted(averages, key=lambda x: x[1])
        three_worsts = averages[:3]
        three_worsts = [three_worst[1] for three_worst in three_worsts]

    with open(output_file_name, 'w', newline='') as csvfile:
        obj = csv.writer(csvfile)
        for three_worst in three_worsts:
            obj.writerow([three_worst])
        csvfile.close()


# write average of average score
# task 05
def calculate_average_of_averages(input_file_name, output_file_name):
    averages = list()
    with open(input_file_name) as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            name = row[0]
            these_grades = list()
            for grade in row[1:]:
                these_grades.append(float(grade))
            average = (name, mean(these_grades))
            averages.append(average)
        scores = [score[1] for score in averages]
        average = mean(scores)

    with open(output_file_name, 'w', newline='') as csvfile:
        obj = csv.writer(csvfile)
        obj.writerow([average])
        csvfile.close()


