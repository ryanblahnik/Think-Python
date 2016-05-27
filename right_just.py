print('?')
m = input()

def right_justify(s):
    d = len(str(s))
    space = 60 - d
    print(' '*int(space) + 'monty')

right_justify(m)
