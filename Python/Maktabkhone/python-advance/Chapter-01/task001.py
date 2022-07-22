# -*- coding: utf-8 -*-
"""
Created on Mon Jan 20 10:07:14 2020

@author: Hossein Molhem
"""

import math
def isPrime(n):
    if n <= 1: 
         return False
    elif n <= 3:
        return True
    elif (n % 2 == 0) or (n % 3 == 0):
        return False
    if all(n%i!=0 for i in range(3,int(math.sqrt(n))+1, 2)):
        return True
    else:
        return False
    
def divisors(x):
    div=[]
    for i in range(1,x+1):
        if (x % i) == 0:
            div.append(i)
    return div

def primeDivisors(x):
    pdiv=[]
    for i in x:
        if isPrime(i):
            pdiv.append(i)
    return pdiv        

def intRead(n):
    a = []
    for i in range(int(n)):
        a.append(int(input()))
    return a    
    

numbers = intRead(10)
d = []
pd = []
lpd = []
for i in range(len(numbers)):
    d.append(divisors(numbers[i]))

for i in range(len(d)):
    pd.append(primeDivisors(d[i]))

for i in range(len(numbers)):
    lpd.append(len(pd[i]))
      

lpd_max_index_list = [i for i,e in enumerate(lpd) if e==max(lpd)]
# print(lpd_max_index_list)

res_list = [numbers[i] for i in lpd_max_index_list]

print(max(res_list), max(lpd))

