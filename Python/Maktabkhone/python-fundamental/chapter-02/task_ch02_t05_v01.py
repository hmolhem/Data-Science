"""
Created on Sun Mar  1 13:41:37 2020
@author: Hossein Molhem
@Email:  hosseinmolhem@gmail.com
Title:   عدد با بیشترین تعداد مقسوم علیه
version: 2.0.0
chapter 02 - task 05
"""

# return number of divisors x
def ndivisor(x):
    d = [i for i in range(1,x+1) if x%i==0]
    return len(d), x


ns = [int(input()) for i in range(0,20)]
ds = [ndivisor(x) for x in ns]
sd = sorted(ds, key=lambda tup: (tup[0], tup[1]), reverse=True)
print(sd[0][1], sd[0][0])
