"""
Created on Sun Mar  1 21:17:15 2020
@author: Hossein Molhem
@Email:  hosseinmolhem@gmail.com
Title:   کار با رشته ها
version: 2.0.0
chapter 03 - task 01

"""

word = input()
vowel = ['a', 'e', 'i', 'o','u' ,'A', 'E', 'I', 'O', 'U']
str = ''.join([word[k] for k,v in enumerate(word) if v not in vowel])
str = '.' + '.'.join([str[i] for i in range(0,len(str))])
print(str.lower()) 
