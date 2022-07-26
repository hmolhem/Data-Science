"""
Created on Tue July  26 13:30:00 2022
@author: Hossein Molhem
@Email:  hosseinmolhem@gmail.com
Title:  columb law
version: 2.0.0
chapter 01 - example 1.1.1
"""

import electrostatic as es
import numpy as np

q1 = float(input('First electric charge: '))
lst1 = list(map(float,input("Position it : ").strip().split()))[:3]
x1 = np.array(lst1)

q2 = float(input('Second electric charge: '))
lst2 = list(map(float,input("Position it : ").strip().split()))[:3]
x2 = np.array(lst2)

d, s, u = es.vx2y(x1,x2)
F = es.coulombLaw(q1, q2, s, u)
print(F)