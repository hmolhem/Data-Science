# -*- coding: utf-8 -*-
"""
Created on Tue Jan 21 16:58:42 2020

@author: Hossein Molhem
"""
gameTable =[
            ('Iran','Spain'), 
            ('Iran', 'Portugal'),
            ('Iran', 'Morocco'),
            ('Spain','Portugal'),
            ('Spain','Morocco'),
            ('Portugal','Morocco')
            ]



result = {'wins':0, 
          'loses':0, 
          'draws':0, 
          'goal difference':0, 
          'points':0 
          }

countries = {'Iran' : result, 
             'Spain': result, 
             'Portugal': result, 
             'Morocco': result
            }



# Python code to convert string to list 
def Convert(string): 
    li = list(string.split("-")) 
    return li 

resultTable = []
for i in range(6):
    resultTable.append(input())
    
    
b=[]
for ele in resultTable:
    b.append(Convert(ele))
    


for r in range(len(b)):
    for c in range(len(b[r])):
        b[r][c] = int(b[r][c])

#for r in range(len(b)):
#       b[r]=tuple(b[r])

# msk = [[j=='Portugal' for j in gameTable[i]] for i in range(len(gameTable))]

tempTeam = []
tempIndex = []
dic_scored_goal = {}
dic_nscored_goal = {}

for i,ele in enumerate(gameTable):
    if 'Spain' in ele:
        # print(i,ele)
        tempIndex.append(i)
        tempTeam.append(ele)
        dic_scored_goal.update({i:ele.index('Spain')})


# for r in tempIndex:
#    print(b[r])
        
[b[r] for r in tempIndex ]

# python code for socred and no-socred goal for every country
def socred_goal(country, gt):
    dsg = {}
    ti, tt = [], []
    
    for i,ele in enumerate(gt):
        if country in ele:
            ti.append(i)
            tt.append(ele)
            dsg.update({i:ele.index(country)})
    return ti, tt, dsg
