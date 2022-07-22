# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 21:43:21 2020

@author: Hossein Molhem
"""

class computer:
    count = 0
    def __init__(self, ram, hard, cpu):
        self.ram = ram
        self.hard = hard
        self.cpu = cpu
        
    def value(self):
        return self.cpu + self.hard + self.ram
    
class laptop(computer):
    pass


pc1 = computer(6, 4, 8)
print(pc1.value())

lp1 = laptop(10, 4, 8)
print(lp1.value())
