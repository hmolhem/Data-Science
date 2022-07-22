import hashlib

def c2h(str):
    result = hashlib.sha256(str.encode())
    return result.hexdigest()

strings = ['123','345','678']

for string in strings:
    print(c2h(string))

hash_list = list(map(c2h,strings))
print(hash_list)
