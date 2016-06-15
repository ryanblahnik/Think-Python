import math, turtle
d = turtle.Turtle()

print('How many petals?')
p = input()
half = 180 / int(p)
turn = 180 - int(half)
dist = 100 / int(p)

def flower(petals):
    for i in range(int(p)):
        firsth()
        secondh()

def firsth():
    for i in range(int(half)):
        d.fd(1)
        d.lt(int(dist))
    d.lt(int(turn))        
    
def secondh():
    for i in range(int(half)):
        d.fd(1)
        d.lt(int(dist))


flower(p)



#petals - each petal has 360/petals angle of the circle

