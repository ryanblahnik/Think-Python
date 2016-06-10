import math, turtle
d = turtle.Turtle()

def p(n):
    for i in range(int(n)):
        angle = 360/(int(n))
        d.fd(int(side))
        d.lt(angle)
        
def arc(t, r, angle):
    d.pu()
    d.fd(int(r))
    d.pd()
    d.lt(90)
    for i in range(int(angle)):
        d.lt(1)
        d.fd(int(math.pi*int(r))/180)


print('Please enter radius.')
r = input()
print('Please enter degrees.')
angle = input()
arc(d, r, angle)
