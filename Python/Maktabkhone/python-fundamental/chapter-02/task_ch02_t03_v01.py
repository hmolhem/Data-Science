"""
Created on Sun Mar  1 12:52:06 2020
@author: Hossein Molhem
@Email:  hosseinmolhem@gmail.com
Title:   یافتن بزرگترین ثبت نام کننده برای مجلس شورای اسلامی
version: 1.0.0
chapter 02 - task 03
"""
x, m = 0, 0

while x != -1:
    x = input()
    x = int(x)
    if x>m:
        m = x
    
print(m)