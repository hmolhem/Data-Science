# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 23:21:03 2020

@author: Hossein Molhem
"""

array = [(1,4,5), (3,2,7), (8,3,6), (9,2,3)]
array.sort(key = lambda a:a[2])
print(array)


mylist = [2,3,5,8,11,14,17,102,44]
print(list(map(lambda x:'Yes' if  x%2==1 else 'No',mylist)))

mylist = [2,15,26,8,11,14,17,102,44]
map_list = map(lambda x:x%10,mylist)
filter_list = list(filter(lambda x: x<=4,map_list))
print(filter_list)

mylist = [2,15,26,8,11,14,17,102,44]
map_list = list(map(lambda x:x%10,mylist))
filter_list = filter(lambda x: x<=4,map_list)
print(filter_list)

mylist = [2,15,26,8,11,14,17,102,44]
map_list = list(map(lambda x:x%10,mylist))
filter_list = list(filter(lambda x: x<=4,map_list))
print(filter_list)

mylist = [2,15,26,8,11,14,17,102,44]
map_list = list(map(lambda x:x%5,mylist))
filter_list = list(filter(lambda x: x<4,map_list))
print(filter_list)

ylist = ['yellow', 'red', 'blue','red','yellow','red','blue','purple']
mylist.sort()
mylist = list(map(lambda x: 'color' if x=='red' else x,mylist))
output = list(filter(lambda x: x=='red',mylist))
print(output)