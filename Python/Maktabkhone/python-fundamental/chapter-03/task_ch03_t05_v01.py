"""
Created on Mon Mar  2 23:08:56 2020
@author: Hossein Molhem
@Email:  hosseinmolhem@gmail.com
Title:   حروف کوچیک حروف بزرگ
version: 1.0.0
chapter 03 - task 05

"""

def uchrs(s):
    c = 0
    for chr in s:
        if chr.isupper():
            c+=1
    return c

string =  input()

upper = uchrs(string)
lower = len(string) - upper

flag = upper > lower

if flag:
    print(string.upper())
else:
    print(string.lower())
    
