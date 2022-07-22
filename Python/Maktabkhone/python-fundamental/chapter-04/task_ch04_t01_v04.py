"""
Created on Tue Mar  3 20:36:09 2020

@author: Hossein Molhem
@Email:  hosseinmolhem@gmail.com
Title:   ریشه دوم
version: 4.0.0
chapter 04 - task 01

"""

import math as m # import mathematics library
n = int(input()) # how many numbers you get?
x = [abs(int(input())) for i in range(0,n)] # getting n number 
y = [ str(m.sqrt(i)) for i in x] # compute squre root
y =  list(map(lambda x: x.split('.'),y))

for i in y:
    if i[1]=='0':
        i[1] += '000'
    if len(i[1])>4:
        i[1]=i[1][0:4]
    

final = [ '.'.join(i) for i in y] 

for i in final:
    print(i)