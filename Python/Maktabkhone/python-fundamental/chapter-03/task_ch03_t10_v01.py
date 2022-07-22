"""
Created on Tue Mar  3 20:36:09 2020

@author: Hossein Molhem
@Email:  hosseinmolhem@gmail.com
Title:   قیمت لپ‌تاب‌ها
version: 1.0.0
chapter 03 - task 10
"""
n = int(input()) # enter number of laptop
data = [[int(j) for j in input().split()] for i in range(n)] # data entry
check1 = lambda x: x[0] > x[1] # compare first item with second item 
check2 = lambda x,y: x[0]<y[0] and x[1]>y[1]
r = list(map(check1,data)) # compare all first and second item in list data 
flag = any(r) # Is there any True? if not poor irsa

if not flag:
    print('poor irsa')
else:
    j = r.index(True)
    x = [check2(i,data[j]) for i in data if  data.index(i)!=j]    
    if any(x):
        print('happy irsa')