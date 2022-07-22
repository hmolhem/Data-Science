"""
Created on Sun Mar  1 08:54:42 2020
@author: Hossein Molhem
@Email: hosseinmolhem@gmail.com
Determine the number prime
chapter 02 - task 01
final version
"""

import math as m
def isPrime(n):
    if n <= 1: 
         return False # one is not prime
    elif n <= 3:
        return True
    # even number is not a prime number
    # every number division to 3 is not a prime number
    elif (n % 2 == 0) or (n % 3 == 0): 
        return False
    # whether n is a multiple of any integer between 2 and sqrt(n)
    if all(n%i!=0 for i in range(3,int(m.sqrt(n))+1, 2)):
        return True
    else:
        return False
        
num = int(input())  # input integer number
if isPrime(num):
    print('prime')
else:
    print('not prime')