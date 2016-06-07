import turtle
r = turtle.Turtle()

def p(n):
    for i in range(int(n)):
        angle = 360/(int(n))
        r.fd(int(side))
        r.lt(angle)

        


print('How many sides?')
n = input()
print('How long are the sides?')
side = input()

p(n)
