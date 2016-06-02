import turtle
r = turtle.Turtle()

def square(t, h):

    for i in range(4):
        t.fd(int(h))
        t.lt(90)

print('How tall should your square be?')
h = input()

square(r, h)
