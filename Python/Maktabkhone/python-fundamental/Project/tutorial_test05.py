import csv
my_dict = {'1': 'aaa', '2': 'bbb', '3': 'ccc'}

#  https://www.tutorialspoint.com/How-to-save-a-Python-Dictionary-to-CSV-file

with open('tutoral_test.csv', 'w') as f:
    f.write("{")
    for key in my_dict.keys():
        f.write("%s:%s,\n"%(key,my_dict[key]))
    f.write("}")    