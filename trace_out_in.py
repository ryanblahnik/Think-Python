import turtle
r = turtle.Turtle()

print('How many sides?')
n = input()

angle = 360/(int(n))
ins = (180 - int(angle))/2


r.fd(100)
r.lt(ins)
