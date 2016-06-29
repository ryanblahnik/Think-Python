import turtle, math
r = turtle.Turtle()
r.speed(0)
r.pencolor('#3c56ff')
r.ht()
turtle.bgcolor("#ffcd25")
r.width(10)

#ffcd25
#c640ff

print('How many sides?')
n = input()
print('Radius?')
ra = input()

l = int(n) - 2
angle = (180 * int(l))/int(n)
turn = 180 - (angle / 2)
iturn = 180 - float(angle)
#oturn = (angle / 2)
# old attempt
# side = int(math.sqrt((math.sin(int(angle)/100)**2 + (100 - (math.cos(int(angle))/100))**2)))
side = (2 * int(ra) * (math.sin(math.pi/int(n))))

#hept only
r.lt(12.857)

def centers(n):
    for i in range(int(n)):
        r.fd(int(ra))
        r.lt(180)
        r.fd(int(ra))
        r.lt(angle)

centers(n)

def border(n):
    r.fd(int(ra))
    r.lt(turn)
    for i in range(int(n)):
        r.fd(side)
        r.lt(iturn)
        

border(n)

# math.sqrt((math.sin(int(angle))**2 + (1 - math.cos(int(angle)))**2)
# 2r * sin(pi/n) = a
# angle = radians
# radians to degrees 2pi = 360, pi = 180

