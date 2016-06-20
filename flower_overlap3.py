import math, turtle
d = turtle.Turtle()
d.shape("turtle")
d.speed(10)
d.pencolor("orange")

print('How many petals?')
p = input()
half = (360 + (60 * int(p)))/ int(p)
turn = 180 - int(half)
dist = int(int(p)/8)

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
    d.lt(120)


flower(p)


