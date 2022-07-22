"""
Created on Fri Mar  6 20:47:55 2020

@author: Hossein Molhem
@Gmail: hosseinmolhem@gmail.com
"""

# string function
# Python program to convert a list of character to string
def lis2str(lis): 
    check1 = type(lis) == list 
    check2 =  all([ i.isalpha() for i in lis])
    check = check1 and check2
    if check:
        return("".join(lis)) 
    else:
        print('list is not alphabetic')
        
# print(lis2str(['a','l','i']))
    