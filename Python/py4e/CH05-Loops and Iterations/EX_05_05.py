str = 'X-DSPAM-Confidence:0.8475'
s = str.find(':')
print(s)
print(float(str[s+1:-1]))