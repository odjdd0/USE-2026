def pr(x):
    return x > 1 and all(x%i != 0 for i in range(2,int(x**0.5)+1))
a = [x for x in range(800,1000) if pr(x)]

k = 0
for i in range(700_000, 10**7):
    if k == 5: break
    for x in a:
        for step in range(3):
            if x**step == i:
                print(i,x)
                k += 1
