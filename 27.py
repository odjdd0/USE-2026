cla = [[],[]]
for s in open('27A_22625.txt'):
    x,y = [float(c) for c in s.split()]
    if y < 15:
        cla[0].append([x,y])
    else:
        cla[1].append([x,y])


clb = [[],[],[]]
for s in open('27B_22625.txt'):
    x,y = [float(c) for c in s.split()]
    if x < 10:
        clb[0].append([x,y])
    if 10 < x < 20:
        clb[1].append([x,y])
    if x > 20:
        clb[2].append([x,y])
from math import dist
def cent(cl):
    m = []
    for p in cl:
        mn = sum(dist(p,p1) for p1 in cl)
        m.append([mn,p])
    return min(m)[1]

def anticent(cl):
    m = []
    for p in cl:
        mn = sum(dist(p,p1) for p1 in cl)
        m.append([mn,p])
    return max(m)[1]

centersA = [cent(cl) for cl in cla]
centersB = [cent(cl) for cl in clb]

anticentersA = [anticent(cl) for cl in cla]
anticentersB = [anticent(cl) for cl in clb]


pxa = sum(x for x,y in centersA)/len(centersA)
sya = sum(y for x,y in anticentersA)/len(anticentersA)

pxb = sum(x for x,y in centersB)/len(centersB)
syb = sum(y for x,y in anticentersB)/len(anticentersB)


print(int(abs(pxa*10_000)), int(abs(sya*10_000)))
print(int(abs(pxb*10_000)), int(abs(syb*10_000)))
