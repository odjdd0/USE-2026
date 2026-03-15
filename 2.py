from itertools import *
def F(x,y,w,z):
    return (x and (not y)) or (y == z) or w
values = [0,0,0]
for a,b,c,d,e,f,g,h in product([0,1],repeat = 8):
    t = [(a,b,c,1),
         (1,d,e,f),
         (1,1,g,h)]
    if len(t)!= len(set(t)): continue
    for p in permutations('xywz'):
        valp = [F(**dict(zip(p,row))) for row in t]
        if valp == values:
            print(''.join(p))
