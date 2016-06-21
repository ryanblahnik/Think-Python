import turtle
r = turtle.Turtle()


def p(n):
    angle = 360/(int(n))
    for i in range(int(n)):       
        r.fd(int(side))
        r.lt(angle)
    ins = (180 - int(angle))/2
    cent = (180 - int(angle))
    for i in range(int(n)):
        r.lt(int(ins))
        r.fd(int(side))
        r.lt(int(cent))
        r.fd(int(side))
        r.lt(180)
        
        


print('How many sides?')
n = input()
print('How long are the sides?')
side = input()

p(n)
