# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 23:43:43 2020

@author: Hossein Molhem
"""

class maktabkhooneh:

    def _init_(self, name, age):
        self.name = name
        self.age = age

    def get_name(self):

        print ("my name is %s and my age is %i" % (self.name,self.age))

 

Maktabkhooneh = maktabkhooneh('maktabkhooneh',7)

Maktabkhooneh.get_name()