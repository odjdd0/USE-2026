from itertools import *
for i,w in enumerate(product(sorted('КОДИМ'),repeat = 5), start = 1):
    j = ''.join(w)
    if j.count('М') == 2 and 'ММ' not in j:
        print(i)
