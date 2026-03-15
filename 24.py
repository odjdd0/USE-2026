s = open('24_23381.txt').readline().strip()
from re import *
alph = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
res = []
for x in alph:
    reg = rf'(?=([02468]{x}*[02468]))'
    m = max([x.group(1) for x in finditer(reg,s)],key = len)
    res.append([len(m),m])
print(max(res)[0])
