f = open('26_18621.txt')
n = int(f.readline())
data = [[int(x) for x in s.split()] for s in f.readlines()]
res = []
for i in data:
    summa = sum(i[1:])
    pluses = sum(x for x in i[1:] if x > 0)
    k_otv = sum(1 for x in i[1:] if x != 0)
    res.append([summa,pluses,k_otv,i[0]])
res.sort(key = lambda x: [-x[0],-x[1],-x[2],x[3]])

proshli = []

for i in range(n//4):
    proshli.append(res[i])


for i in res:
    if i[:3] == proshli[-1][:3]:
        proshli.append(i)

cnt = 1
for x in res:
    if x[:3] == proshli[1699][:3]:
        cnt += 1

for x in res:
    if x not in proshli:
        print(x[3])
        break
print(cnt)

        
