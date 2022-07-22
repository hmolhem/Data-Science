import random as rnd
a = 1
b = 99
flag = True
javab = 0
while flag:
    hads = rnd.randint(a,b)
    print('Is this number ?',hads)
    ch = input('enter k/d/b :')
    if ch == 'k':
        a = hads
    elif ch == 'b':
        b = hads    
    elif ch == 'd':
        flag = False
        javab = hads
        
print('That\'s Ok. my number is', hads)