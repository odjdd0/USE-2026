f = 96_000
t = 3*60 + 33
i = 2
for k in range(100000):
    I = k*i*f*t
    I2 = 0.6 * I
    if I2 <= 25*1024*1024*8:
        print(k)
