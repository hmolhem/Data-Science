"""
Created on Sun Mar  1 09:43:43 2020
@author: Hossein Molhem
@Email:  hosseinmolhem@gmail.com
Title:   score of sepid rod of rasht
version: 1.0.0
chapter 02 - task 02

"""
win, lose, draw, point = 0, 0, 0, 0
for i in range(0,10):
    x = input()
    x = int(x)
    if x==3:
        win+=1
        point+=3
    elif x==1:
        draw+=1
        point+=1
    elif x==0:
        draw+=1

print(point,win)
        
    

    
