from ipaddress import *
net = ip_network('98.71.254.171/255.248.0.0',0)
for ip in net.hosts():
    ip2 = f'{ip:b}'
    if ip2.count('1')%7 == 0:
        print(*[int(x) for x in str(ip).split('.')])
        break
