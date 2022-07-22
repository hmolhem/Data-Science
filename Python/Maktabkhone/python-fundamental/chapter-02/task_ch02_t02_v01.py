"""
Created on Sun Mar  1 09:43:43 2020
@author: Hossein Molhem
@Email:  hosseinmolhem@gmail.com
Title:   score of sepid rod of rasht
version: 1.0.0
chapter 02 - task 02

"""
# input 30 nuber 0, 1, 3
# 0, 1 and 3 is score of sepid rod rasht team that means lose, draw and win
win, lose, draw, score = 0, 0, 0, 0
for i in range(0,30):
    x = input()
    x = int(x)
    if x==3:
        win+=1
        score+=3
    elif x==1:
        draw+=1
        score+=1
    elif x==0:
        draw+=1

print(score,win)
        
    

    
