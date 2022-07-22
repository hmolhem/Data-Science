# -*- coding: utf-8 -*-
"""
Created on Sat Feb 22 23:38:08 2020

@author: Hossein Molhem
"""

# python code for input result game
def readResult(x):
    for i in range(6):
        x.append(input())
    return x

# Python code to convert string to list 
def Convert(string): 
    li = list(string.split("-")) 
    return li 