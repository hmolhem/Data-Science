# -*- coding: utf-8 -*-
"""
Created on Sun Mar  1 21:17:15 2020

@author: Hossein Molhem
@Email:  hosseinmolhem@gmail.com
Title:   عدد با بیشترین تعداد مقسوم علیه
version: 1.0.0
chapter 03 - task 01
"""
word = 'aBAcAba'
str = word.lower()
vowel = ['a', 'e', 'i', 'o','u' ,'A', 'E', 'I', 'O', 'U']

x = [ k for k,v in enumerate(str) if v in vowel]
    
for i in x:
    str = str.replace(str[i], '.')
    
print(str)
