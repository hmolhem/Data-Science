# -*- coding: utf-8 -*-
"""
Created on Sun Mar  1 16:08:38 2020

@author: Hossein Molhem
@Email:  hosseinmolhem@gmail.com
Title:   یافتن سن بزرگترین کاندیدا و دومین بزرگترین کاندیدا
version: 1.0.0
chapter 02 - task 04
"""

max1 = 0 # first maximum
max2 = 0 # second maximum
x = 0 # 
while x != -1:
    x = input() # entry number
    x = int(x) # convert str to int

    if x > max1:
        max2 = max1
        max1 = x

    if x < max1 and x > max2    :
        max2 = x

        
print(max1 , max2)