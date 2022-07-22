import csv
persons = [('Lata',22,45),('Anil',21,56),('John',20,60)]

csvfile = open('persons.csv','w', newline='')
obj = csv.writer(csvfile)
obj.writerows(persons)
obj.close()