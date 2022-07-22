"""
Created on Mon Mar  2 23:08:56 2020
@author: Hossein Molhem
@Email:  hosseinmolhem@gmail.com
Title:   جمع اعداد
version: 1.0.0
chapter 03 - task 02

"""

word = input()
digit = list(filter(lambda x: x.isdigit(), word))
digit.sort(key=int)
digit = '+'.join([digit[i] for i in range(0,len(digit))])
print(digit)