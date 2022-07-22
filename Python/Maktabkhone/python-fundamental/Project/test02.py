import csv
import hashlib
from collections import OrderedDict

hash_dict = OrderedDict()

def c2h(str):
    result = hashlib.sha256(str.encode())
    return result.hexdigest()

hash_list = [(c2h(str(n)),str(n)) for n in range(1000,10000)]
hash_dict = OrderedDict(hash_list)

# for k,v in hash_dict.items():
#     print(k,v)

# with open('out.csv','w', newline='') as csvfile:
#     writer = csv.writer(csvfile, delimiter=',')
#     for k,v in hash_dict.items():
#         writer.writerow([k,v])

with open('out.csv', 'w', newline='') as f:
    f.write("{")
    for key in hash_dict.keys():
        f.write("\'%s\':\'%s\',\n"%(key, hash_dict[key]))
    f.write("}")
    f.close()