"""
Created on Mon Mar  2 23:08:56 2020
@author: Hossein Molhem
@Email:  hosseinmolhem@gmail.com
Title:   سارا سلام می‌کند
version: 1.0.0
chapter 03 - task 04

"""
def list2str(s):
    r = ''.join(s)
    return r


string =  input()
string = string.lower()
yes = 'YES'
no = 'NO'
hello = 'hello'

#refin_string = [ch for ch in string if any(ch in a for a in hello)]
#x = list2str(refin_string)
# del  refin_string

test=''
start = 0
for ch in hello:
    y = string.find(ch,start)
    print(ch,y,start)
    if y!=-1:
        test+=string[y]
        start+=y
    else:
        continue
        
flag = test == hello                
if flag:
    print(yes)
else:
    print(no)
    
