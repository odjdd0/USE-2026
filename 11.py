from math import *
k = 16
N = 26 + 20
i = ceil(log2(N))
I = ceil((k*i)/8)
for idop in range(1000000):
    if 128 * (I + idop) == 25 * 1024:
        print(idop)
