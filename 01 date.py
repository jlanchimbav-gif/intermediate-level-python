## date ##

from datetime import datetime 
now = datetime.now()

print(now.year)
print(now.month)
print(now.day)
print(now.hour)
print(now.minute)
print(now.second)

timestamp = now.timestamp()
print(timestamp)

year2026= datetime(2026,2,15,23)
print(year2026)

from datetime import time
curren_time=time(20,41,25)

print(curren_time.hour)
print(curren_time.minute)
print(curren_time.second)

from datetime import date
curren_date=date(2026,2,15)


print(curren_date.year)
print(curren_date.month)
print(curren_date.day)

curren_date=date(curren_date.year+1,curren_date.month,curren_date.day)
print(curren_date)

diff=year2026-now
print(diff)