import time

print('t?')
t = input()
t = int(t)
one_day = 60 * 60 * 24
zone = 60 * 60 * 5
cdt = t - zone
today = cdt % one_day
dp = cdt // one_day

print(str(t))
print()

nm = today / 60
nhr = nm / 60
nmd = nm - (int(nhr) * 60)
nsd = today - (int(nm) * 60 )

if nhr > 12:
    nhr = nhr - 12

print(str(int(nhr)) + ':' + str(int(nmd)) + ':' + str(int(nsd)))
