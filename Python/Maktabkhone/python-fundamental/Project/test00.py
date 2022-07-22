# convert data password file to data hash password file
import csv
import hashlib
from collections import OrderedDict

def c2h(str):
    result = hashlib.sha256(str.encode())
    return result.hexdigest()

with open('passwords.csv') as csvfile:
    reader = csv.reader(csvfile)
    passwords =  OrderedDict([ (row[0].strip(), row[1].strip()) for row in reader])
    
for k,v in passwords.items():
    passwords[k] = c2h(passwords[k])

# for k,v in users.items():
#     print(k,v)

with open('hash_file.csv','w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    for k,v in passwords.items():
        writer.writerow([k,v])
    
csvfile.close()