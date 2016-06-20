import math, turtle
d = turtle.Turtle()
d.shape("turtle")
d.speed(10)
d.color("orange")

print('How many petals?')
p = input()
half = 360 / int(p)
turn = 180 - int(half)
dist = int(int(p)/2)

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


