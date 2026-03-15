def valid(x,A):
    return ((x&17!=0)<=((x&A!=0)<=(x&58!=0))) <= ((x&8==0) and (x&A!=0) and (x&58==0))
cnt = 0
for A in range(1,10000):
    ok = False
    for x in range(10000):
        if valid(x,A):
            ok = True
            break
    if not ok:
        cnt += 1
print(cnt)
