import turtle
r = turtle.Turtle()
r.speed(10)

print('How many sides?')
n = input()

l = int(n) - 2
angle = (180 * int(l))/int(n)
turn = 180 - (angle / 2)
oturn = (angle / 2)

def centers(n):
    for i in range(int(n)):
        r.fd(100)
        r.lt(180)
        r.fd(100)
        r.lt(angle)

centers(n)

def border(n):
    r.fd(100)
    r.lt(turn)
    for i in range(int(n)):
        r.fd(100)
        r.lt(oturn)
        

border(n)
