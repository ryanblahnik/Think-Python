print('+ - - - - + - - - - +')
print('|         |         |')
print('|         |         |')
print('|         |         |')
print('|         |         |')
print('+ - - -Welcome- - - +')
print('|         |         |')
print('|         |         |')
print('|         |         |')
print('|         |         |')
print('+ - - - - + - - - - +')

print(' ')
print('How many rows?')
r = input()
print('How many columns?')
c = input()
print(' ')

def xgrid(r, c):
    for i in range(int(r)):
        print('+ - - - - '*int(c) + '+')
        print('|         '*int(c) + '|')
        print('|         '*int(c) + '|')
        print('|         '*int(c) + '|')
        print('|         '*int(c) + '|')
    print('+ - - - - '*int(c) + '+')
    print(' ')
    print('Thank you!')
        

xgrid(r, c)
