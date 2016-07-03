import time

t = time.time()
one_day = 60 * 60 * 24
zone = 60 * 60 * 5
cdt = t - zone
today = cdt % one_day
dp = cdt // one_day

print(str(t) + ' seconds have passed since 1970/01/01 00:00:00.')
print()

nm = today / 60
nhr = nm / 60
nmd = nm - (int(nhr) * 60)
nsd = today - (int(nm) * 60 )

if nhr > 12:
    nhr = nhr - 12

print('Current Central Daylight Time is ' + str(int(nhr)) + ':' + str(int(nmd)) + ':' + str(int(nsd)) + '.')
