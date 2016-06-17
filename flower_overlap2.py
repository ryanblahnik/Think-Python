import math, turtle
d = turtle.Turtle()

print('How many petals?')
p = input()
half = (360 + (20 * int(p))) / int(p)
turn = 160 - int(half)
dist = int(int(p)/3)

def flower(petals):
    for i in range(int(p)):
        firsth()

def firsth():
    for i in range(int(half)):
        d.fd(int(dist))
        d.lt(1)
    d.lt(int(turn))    
    for i in range(int(half)):
        d.fd(int(dist))
        d.lt(1)
    d.lt(180)


flower(p)


