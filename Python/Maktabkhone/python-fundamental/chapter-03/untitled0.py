# -*- coding: utf-8 -*-
"""
Created on Sun Mar  8 20:29:48 2020

@author: Hossein Molhem
"""

def occurrences(string, sub):
    count = start = 0
    p=[]
    while True:
        print('places : ',string.find(sub,start))
        p.append(string.find(sub,start))
        start = string.find(sub, start) + 1
        if start > 0:
            count+=1
        else:
            return count,p

sstr = 'ABACAB'
substr = 'AB'

x,p1 = occurrences(sstr,substr)
print('Numbers occurrences :',x)

import re
text = 'ABHAAB'
len(re.findall('(?=AB)', text))


str = 'Python' #initial string
reversed =''.join(reversed(str)) # .join() method merges all of the characters resulting from the reversed iteration into a new string
print(reversed) #print the reversed string

