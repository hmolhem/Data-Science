"""
Created on Tue Mar  3 20:36:09 2020

@author: Hossein Molhem
@Email:  hosseinmolhem@gmail.com
Title:   جهانی کبدی
version: 1.0.0
chapter 03 - task 09
"""
n = int(input()) # enter number of person
playedGame = [int(j) for j in input().split()] # data entry
f = lambda x: x<3 # function that find play less than 3
# list of all person that played less than 3 game
filterPlayGame = list(filter(f,playedGame))
print(len(filterPlayGame)//3) # number of team