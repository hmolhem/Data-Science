# -*- coding: utf-8 -*-
"""
Created on Tue Mar 10 20:11:49 2020

@author: Hossein Molhem
@Email:  hosseinmolhem@gmail.com
Title:   زیر رشته
version: 1.0.0
chapter 03 - task 07
"""

def how_many_substring(string, sub):
    count = start = 0
    p=[]
    while True:
        # print('places : ',string.find(sub,start))
        if string.find(sub,start) !=-1:
            p.append(string.find(sub,start))
        start = string.find(sub, start) + 1
        
        if start > 0:
            
            count+=1
        else:
            return count,p
def listdif(lis1,lis2):
    return [abs(j-i) for i in lis1 for j in lis2 if lis1.index(i)==lis2.index(j)]

def reversestr(s):
    r = ''.join(reversed(s))
    return r

def there_is(string,substring):
    return string.find(substring) != -1
    
    
sstr = input() # enter string
# substr = input('Input Sub-Stirng : ')
#sstr = 'baab'
sstr.upper() # convert upper string

substr = 'ab'  # find substring 
substr.upper() # convert upper string
rsubstr = reversestr(substr)

there_is_substring = there_is(sstr,substr)
there_is_rsubstring = there_is(sstr,rsubstr)

if (not there_is_substring or not there_is_rsubstring):
    print('NO')
elif (there_is_substring and there_is_rsubstring):
    x,p1 = how_many_substring(sstr,substr)
    y,p2 = how_many_substring(sstr,rsubstr)
    if x!=y:
        if x<y:
            p1 = p1+[0]*abs(y-x)
        if x>y:
            p2 = p2+[0]*abs(y-x)
            
    z = listdif(p1,p2)
    flag =  z.count(1) == 0
    if flag:
        print('YES')
    else:
        print('NO')

