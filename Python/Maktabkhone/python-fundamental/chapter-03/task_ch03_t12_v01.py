"""
Created on Tue Mar  3 20:36:09 2020

@author: Hossein Molhem
@Email:  hosseinmolhem@gmail.com
Title:   مترجم آنلاین
version: 1.0.0
chapter 03 - task 11
"""
from collections import OrderedDict 

n = int(input()) # enter number of laptop
data = list(tuple(map(str,input().split())) for r in range(n))

mydict = OrderedDict()
mydict = { ele[0]:ele[1] for ele in data}

mystr = input().split()
for s in mystr:
    if s in mydict:
        print(mydict[s],end=' ')
    else:
        print(s,end=' ')