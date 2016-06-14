import math, turtle
d = turtle.Turtle()

print('How many petals?')
p = input()
half = 180 - int(p)

def flower(petals):
    for i in range(int(p)):
        firsth()
        secondh()
        d.lt(180)


def firsth():
    for i in range(int(half)):
        d.fd(1)
        d.lt(1)
    
def secondh():
    d.lt(int(half))
    for i in range(int(half)):
        d.lt(1)
        d.fd(1)

flower(p)
