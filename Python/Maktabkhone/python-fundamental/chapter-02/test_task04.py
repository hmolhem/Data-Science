# -*- coding: utf-8 -*-
"""
Created on Sun Mar  1 15:35:18 2020

@author: Hossein Molhem
"""
max1 = 0
max2 = 0
l = []
for i in range(0,5):
    x = input()
    x = int(x)
    l.append(x)
    print('x : ',x)
    if x > max1:
        max2 = max1
        max1 = x
        print('max1 : ',max1)
    if x < max1 and x > max2    :
        max2 = x
        print(max2)
        
print(max1 , max2)
        
        