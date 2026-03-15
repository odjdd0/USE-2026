a = [int(x) for x in open('17_4267.txt')]
mx = max(x for x in a if x%22==0)
cnt, mnsum = 0,100_000
for i in range(len(a)-1):
    s = [a[i],a[i+1]]
    if s[0] > mx or s[1] > mx:
        cnt += 1
        if sum(s) < mnsum:
            mnsum = sum(s)

print(cnt,mnsum)
