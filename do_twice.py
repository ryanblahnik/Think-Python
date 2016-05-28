def do_twice(f, v):
    f(v)
    f(v)

def print_spam():
    print('spam')

def printx(x):
    print(x)

def print_twice(b):
    print(b)
    print(b)

def do_four(f, v):
    do_twice(f, v)
    do_twice(f, v)

print('1.')
print(' ')
do_twice(print_twice, 'spam')
print(' ')
print('2.')
print(' ')
do_four(printx, 'spam')
