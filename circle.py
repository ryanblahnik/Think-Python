import math, turtle
d = turtle.Turtle()

def p(n):
    for i in range(int(n)):
        angle = 360/(int(n))
        d.fd(int(side))
        d.lt(angle)
        
def circle(t, r):
    t.pu()
    t.fd(int(r))
    t.pd()
    for i in range(360):
        d.lt(1)
        d.fd(int(math.pi*int(r))/180)


print('Please enter radius.')
r = input()
circle(d, r)
