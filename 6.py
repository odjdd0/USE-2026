from turtle import *
screensize(5000,5000); lt(90); down(); tracer(0); f = 80
for k in range(4):
    fd(3*f); lt(270); fd(5*f); rt(90)
lt(270)
for k in range(3):
    fd(5*f); rt(90); fd(3*f); lt(270)

up()
for x in range(-50,50):
    for y in range(-50,50):
        goto(x*f,y*f)
        dot(3,'blue')
update()
