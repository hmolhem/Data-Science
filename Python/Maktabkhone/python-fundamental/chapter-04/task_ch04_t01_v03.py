# -*- coding: utf-8 -*-
"""
Created on Fri Mar  6 12:01:00 2020

@author: Hossein Molhem
"""
import decimal
decimal.Context(4)
n = int(input()) # how many numbers you get?
# x = [abs(int(input())) for i in range(0,n)] # getting n number
x = [i for i in range(0,100)] # getting n number
y = [decimal.Decimal(v) for v in x]
for i in y:
    print(i.sqrt()) 