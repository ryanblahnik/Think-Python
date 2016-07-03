import math, turtle
d = turtle.Turtle()
y = turtle.Turtle()
pp = turtle.Turtle()
d.shape("turtle")
d.speed(0)
d.color("orange")
y.shape("turtle")
y.speed(0)
y.color("yellow")
pp.shape("turtle")
pp.speed(0)
pp.color("purple")

print('How many orange petals?')
p = input()
print('How many yellow petals?')
pye = input()
print('How many purple petals?')
ppp = input()
halfo = 360 / int(p)
turno = 180 - int(halfo)
disto = int(int(p)/2)
halfy = 360 / int(pye)
turny = 180 - int(halfy)
disty = int(int(pye)/2)
halfp = 360 / int(ppp)
turnp = 180 - int(halfp)
distp = int(int(ppp)/2)

def flower(turtle, petals, half, dist, turn):
    for i in range(int(petals)):
        firsth(turtle, half, dist, turn)

def firsth(d, half, dist, turn):
    for i in range(int(half)):
        d.fd(int(dist))
        d.lt(1)
    d.lt(int(turn))    
    for i in range(int(half)):
        d.fd(int(dist))
        d.lt(1)
    d.lt(180)


flower(d, p, halfo, disto, turno)
flower(y, pye, halfy, disty, turny)
flower(pp, ppp, halfp, distp, turnp)


