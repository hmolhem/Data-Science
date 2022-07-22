# -*- coding: utf-8 -*-
"""
Created on Wed Mar  4 13:03:10 2020

@author: Hossein Molhem
"""
#%%
# bad way
string = 'salam. jadi is here and testing python for fun'
counter = dict()

for letter in string:
    if letter in counter:
        counter[letter] += 1
    else:
        counter[letter] = 1
for this_one in list(counter.keys()):
    print('%s appeared %s times' %(this_one, counter[this_one]))
#%%
# good way
string = 'salam. jadi is here and testing python for fun'
counter = dict()

for letter in string:
        counter[letter] = counter.get(letter,0) + 1

for this_one in list(counter.keys()):
    print('%s appeared %s times' %(this_one, counter[this_one]))