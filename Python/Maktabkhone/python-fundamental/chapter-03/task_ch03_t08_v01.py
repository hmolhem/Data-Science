"""
Created on Tue Mar  3 20:36:09 2020

@author: Hossein Molhem
@Email:  hosseinmolhem@gmail.com
Title:   ملاقات نوروزی
version: 1.0.0
chapter 03 - task 08

"""
x = [int(s) for s in input().split()]
x.sort()
y = sum([x[1]-x[0], x[2]-x[1]])
print(y)