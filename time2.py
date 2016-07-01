import time

t = time.time()

# garbage
#d = 16918
# on 2016/04/27
#hr = d * 24
#m = hr * 60
#s = m * 60

one_day = 60 * 60 * 24
zone = 60 * 60 * 5

cdt = t - zone

today = cdt % one_day

dp = cdt // one_day

print(str(t) + ' seconds have passed since 1970/01/01 00:00:00.')
print()
#print()
#print(d)
#print(dp)
#print(hr)
#print(m)
#print(s)

#sz = s - zone

#ts = t - s - zone
#tm = ts / 60
#th = tm / 60

#lm = int(th) * 60

#dm = tm - lm

#ls = int(tm) * 60

#ds = ts - ls

nm = today / 60
nhr = nm / 60

nmd = nm - (int(nhr) * 60)
nsd = today - (int(nm) * 60 )

print('Current Central Daylight Time is ' + str(int(nhr)) + ':' + str(int(nmd)) + ':' + str(int(nsd)) + '.')
