# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 10:56:26 2020

@author: Hossein Molhem
"""

class Dog:
    # class Attribute
    species = 'mammal'
    
    #initialize/ instance attribute
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Determine oldest dogs
    def get_biggest_number(*args):
        return max(args)


# Instantiate dog object
philo = Dog('Philo', 7)
mikey = Dog('Mikey', 6)
william = Dog("William", 5)

#output
print("The oldest dog is {} years old.".format(philo.age, mikey.age, william.age))