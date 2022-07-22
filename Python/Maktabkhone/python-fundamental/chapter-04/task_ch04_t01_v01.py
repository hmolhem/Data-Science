"""
Created on Tue Mar  3 20:36:09 2020

@author: Hossein Molhem
@Email:  hosseinmolhem@gmail.com
Title:   ریشه دوم
version: 1.0.0
chapter 04 - task 01

"""
import math as m # import mathematics library
n = int(input()) # how many numbers you get?
x = [abs(int(input())) for i in range(0,n)] # getting n number 
y = [ m.sqrt(i) for i in x] # compute squre root
for i in y:
    print("{:.4f}".format(i)) # print squre root of all n data with 4 decimal