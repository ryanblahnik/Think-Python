import math, turtle
d = turtle.Turtle()

def p(n):
    for i in range(int(n)):
        angle = 360/(int(n))
        d.fd(int(side))
        d.lt(angle)
        
def arc(t, r, angle):
    t.pu()
    t.fd(int(r))
    t.pd()
    t.lt(90)
    for i in range(int(angle)):
        t.lt(1)
        t.fd(int(math.pi*int(r))/180)

def cw(r, angle):
    d.lt(90)
    d.fd(int(r))
    if int(angle) <= 180:
        leftt = 180 - int(angle)
        d.lt(int(leftt))
        d.fd(int(r))
    else:
        rightt = int(angle) - 180
        d.rt(int(rightt))
        d.fd(int(r))

print('Please enter radius.')
r = input()
print('Please enter degrees.')
angle = input()
arc(d, r, angle)
cw(r, angle)

