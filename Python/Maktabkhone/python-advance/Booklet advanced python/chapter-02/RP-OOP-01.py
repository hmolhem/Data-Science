# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 08:53:12 2020

@author: Hossein Molhem
"""

class Dog:
    # class Attribute
    species = 'mammal'
    
    #initialize/ instance attribute
    def __init__(self, name, age):
        self.name = name
        self.age = age

# Instantiate dog object
philo = Dog('Philo', 7)
mikey = Dog('Mikey', 6)


# Access the instance attributes
print("{} is {} and {} is {}.".format(
    philo.name, philo.age, mikey.name, mikey.age))

# Is Philo a mammal?
if philo.species == "mammal":
    print("{0} is a {1}!".format(philo.name, philo.species))