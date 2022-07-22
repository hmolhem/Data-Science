"""
Created on Mon Mar  2 23:08:56 2020
@author: Hossein Molhem
@Email:  hosseinmolhem@gmail.com
Title:   سارا سلام می‌کند
version: 2.0.0
chapter 03 - task 04

"""

str =  input()
str = str.lower()
yes = 'YES'
no = 'NO'
hello = 'hello'

test, start = '', 0

for ch in hello:
    y = str.find(ch,start)
    if y!=-1:
        test+=str[y]
        start=y+1
    else:
        continue
        
flag = test == hello                
if flag:
    print(yes)
else:
    print(no)
    
