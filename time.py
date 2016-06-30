import time

secs = time.time()

mins = secs / 60

hrs = mins / 60

days = hrs / 24

years = days / 365.25

print(secs)
print(mins)
print(hrs)
print(days)
print(years)
print(1970 + years)

current = 1970 + years

into = current - 2016

idays = into * 365

print()
print(idays)

today = idays - 117
ihrs = today * 24

print(ihrs)

thishr = ihrs - 11
imins = thishr * 60

print(imins)
