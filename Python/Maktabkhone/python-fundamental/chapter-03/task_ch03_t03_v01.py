"""
Created on Mon Mar  2 23:08:56 2020
@author: Hossein Molhem
@Email:  hosseinmolhem@gmail.com
Title:   استانداردسازی اسامی
version: 1.0.0
chapter 03 - task 03

"""
def str2std(x):
    x = x.lower()
    str =  x[0]
    x = x.replace(str, str.upper(),1)
    return x

persons = [input() for i in range(0,10)]
standard_persons = list(map(str2std,persons))   
for person in standard_persons:
    print(person)
