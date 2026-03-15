#Task1: 22
#Task2: yxwz
#for x in range(2):
#    for y in range(2):
#        for z in range(2):
#            for w in range(2):
#                if ((x and (not(y))) or (y==z) or w) == 0:
#                    print(x,y,z,w)
#Task5: 16
#a=[]
#for n in range(1000):
#    dv = bin(n)[2:]
#    sdw = dv.count('1')
#    new1 = dv + str(sdw%2)
#    snew1 = new1.count('1')
#    new2 = dv + str(snew1%2)
#    new3 = int(new2, 2)
#    if (new3>=20) and (new3<=50):
#        a.append(new3)
#print(len(a))

#Task8: 3099 
#from itertools import product
#
#counter = 0
#for word in product('ДИКМО', repeat = 5):
#    s=''
#    for b in word:
#        s+=b
#    counter+=1
#    if (s.count('М')==2) and (not('ММ' in s)):
#        print(counter,'.',s)

#Task13: 986407

#from ipaddress import *
#
#i = []
#
#net = ip_network('98.71.254.171/255.248.0.0',0)
#for ip in net.hosts():
#    ip2 = f'{ip:b}'
#    if ip2.count('1')%7==0:
#        print(ip)
#        break

#Task14: 205

#x = (6*512**180)+(7*64**181)+(3*8**184)+(5*8**125)-65
#s=''
#while x:
#    s = str(x%64) + s
#    x //= 64
#print(s.count('0'))

#Task15: 15
#def valid(x,A):
#    return ((x&17!=0)<=((x&A!=0)<=(x&58!=0))) <= ((x&8==0) and (x&A!=0) and (x&58==0))
#cnt=0
#for A in range(1,10000):
#    ok = False
#    for x in range(10000):
#        if valid(x,A):
#            ok = True
#            break
#    if not ok:
#        cnt += 1
#print(cnt)

#Task16:
#from sys import setrecursionlimit
#
#setrecursionlimit(10000)
#
#def F(n):
#    if n==1:
#        return 1
#    elif n>1:
#        return (n+1)*F(n-1)
#
#print(F(5037)/F(5034))

#Task17:
#pairs = []
#f = [int(x) for x in open('17_4267.txt')]
#maximum = max([x for x in f if int(x)%22==0])
#for i in range(len(f)-1):
#    s = [f[i], f[i+1]]
#    if (s[0]>maximum) or (s[1]>maximum):
#        pairs.append(sum(s))
#
#print(len(pairs), min(pairs))

#Task19-21:
#def f(s,m):
#    if s>=59: return m%2==0
#    if m==0: return 0
#    h = [f(s+1, m-1), f(s+3, m-1), f(s*4, m-1)]
#    return any(h) if (m-1)%2==0 else all(h)
#
#print(19, [s for s in range(1,59) if not f(s,1) and f(s,2)])
#print(20, [s for s in range(1,59) if not f(s,1) and f(s,3)])
#print(21, [s for s in range(1,59) if not f(s,2) and f(s,4)])



