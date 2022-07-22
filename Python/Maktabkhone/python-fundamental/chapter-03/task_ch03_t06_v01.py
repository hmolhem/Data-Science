"""
Created on Mon Mar  2 23:08:56 2020
@author: Hossein Molhem
@Email:  hosseinmolhem@gmail.com
Title:    آیا Palindrome است؟
version: 1.0.0
chapter 03 - task 06

"""

def reverse(s): 
    s = s[::-1] 
    return s

def campare(s,rs):
    return s==rs

def display(f):
    if f:
        print('palindrome')
    else:
        print('not palindrome')

str =  input()
rstr = reverse(str)
flag = campare(str.lower(),rstr.lower())
display(flag)
    
