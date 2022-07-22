"""
Created on Tue Mar  3 20:36:09 2020

@author: Hossein Molhem
@Email:  hosseinmolhem@gmail.com
Title:   شمارش آراء
version: 1.0.0
chapter 03 - task 11
"""
from collections import OrderedDict 

n = int(input()) # enter number of laptop
persons = [] # data entry
votes = OrderedDict() # votes

for i in range(n):
    persons.append(input())
    

for person in persons:
    votes[person] = persons.count(person)
   
for key in sorted(votes.keys()):
    print(key, votes[key])