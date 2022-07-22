a = [
    ('soheila', 7.833333333333333),
    ('sara', 9.75),
    ('mandana', 11.0),
    ('sina', 11.333333333333334),
    ('ali', 12.0),
    ('sarvin', 12.0)]
# b = sorted(a , key = lambda x : x[1], reverse = True)
# three_best = b[:3]
b1 = sorted(sorted(a, key = lambda x : x[1]), key = lambda x : x[0], reverse=True)
b2 = sorted(a,key=lambda x: (x[1],x[0]))
for e in b1:
    print(e,'')

print('-----')

for e in b2:
    print(e,'')
