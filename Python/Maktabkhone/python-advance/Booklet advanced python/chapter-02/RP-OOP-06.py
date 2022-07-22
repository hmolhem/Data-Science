# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 11:59:10 2020

@author: Hossein Molhem
"""

# parent class
class Dog:
    # class attribute
    species = 'mammal'
    
    # Initializer / Instance Attribute
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
        
    # Instance Method: content
    def description(self)    :
        return "{} is {} years old.".format(self.name, self.age)
    
    # Instance Method: behavior
    def speak(self, sound):
        return "{} says {}.".format(self.name, sound)
    
class Bulldog(Dog):
    def run(self, speed):
        return "{} runs {}".format(self.name, speed)
        
class RussellTerrior(Dog):
    def run(self, speed):
        return "".format(self.name, speed)
    
Jim = Bulldog("Jim",12)
print(Jim.description())

print(Jim.run("slowly"))

print(Jim.speak("GUff Guff"))
















