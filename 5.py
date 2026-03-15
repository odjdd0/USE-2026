cnt = 0
for n in range(1,1000):
    b = bin(n)[2:]
    s1 = sum(int(x) for x in b)
    b = b + f'{s1%2}'
    s2 = sum(int(x) for x in b)
    b = b + f'{s2%2}'
    r = int(b,2)
    if 20 <= r <= 50:
        cnt += 1
print(cnt)
