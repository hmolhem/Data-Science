# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 21:37:46 2020

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

pc1 = computer(6, 4, 8)
print(pc1.value())
