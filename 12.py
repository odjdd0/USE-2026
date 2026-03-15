command = {
    (' ',0): (' ',1,1),
    (' ',1): (' ',2,1),
    ('0',0): ('1',1,1),
    ('0',1): ('1',1,0),
    ('1',0): ('0',1,1),
    ('1',1): ('0',1,0),
    ('2',0): ('1',2,0),
    ('2',1): ('0',2,1),
}

def mt(s):
    s = list(' '+s+' ')
    i = 0
    q = 0
    while True:
        write,move,new_q = command[(s[i],q)]
        s[i] = write
        q = new_q
        if move == 2: break
        i += move
    return ''.join(s).strip()

s = '0'*900 + '1'*800 + '2'
print(mt(s).count('1'))
