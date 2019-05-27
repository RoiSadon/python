# datetime module in python:
date, time, timezone,delta
naive date: don't have enough information, easier to work with. 

## datetime.date()
works with year , month , day
```python
import datetime 

# datetime.date() - gives the year,month,day
d = datetime.date(2019,1,23)
print(d)

#  datetime.date.today() - gives the current dade today:
tday = datetime.date.today()
print(tday)

# specifiy which part of the date is wanted. 
print("Current year: ",tday.year)
print("Current month: ",tday.month)

# get the current day of the week:
# weekday() - Monday starts from 0. isoweekday() - Monday starts from 1.
print("weekday() function: ",tday.weekday())
print("isoweekday() function: ",tday.isoweekday())

# timedelta() 
tdelta = datetime.timedelta(days=7)
print("one week from now: ", tday + tdelta)
print("one week ago: ", tday - tdelta)


# calculate time till my bu=irthday this year: 
bday = datetime.date(2019,7,31)
till_bday = bday - tday
print("Days till my birthday: ", till_bday)
# or print(till_bday(days)) - gets only the days. 
# gets the time in seconds: 
print(till_bday.total_seconds())
```

## datetime.time()
works with hours , minutes , seconds , microseconds
```python
import datetime 

# by default it doesnt have time info, so it is naive. 
t = datetime.time(9,30,45,100000)
print(t)

# access individualy:
print(t.hour)
print(t.minute)
print(t.microsecond)
```

## datetime.datetime()
works with year,month,day,hours,minutes,seconds,microseconds.
we can use diffrent methods to call only date / only time. 
```python
import datetime 

dt = datetime.datetime(2019,1,23,12,30,54,10000)
print(dt) #2019-01-23 12:30:54.010000

# we can still access each parameter individualy.
# get only date: (it is a function)
print("Date only: " ,dt.date())

# get only time: (it is a function)
print("Time only: " ,dt.time())

# will give result in date + time: 
tdelta = datetime.timedelta(days = 7)
print("7 days from now: ", dt+tdelta)

tdelta = datetime.timedelta(hours = 12)
print("12 hours fron now: ", dt + tdelta)

# return the current local datetime, with a timezone of None
dt_today = datetime.datetime.today()
# gives option to insert timezone. (if emppty- identical to today())
dt_now = datetime.datetime.now()
dt_utcnow = datetime.datetime.utcnow()

print(dt_today)     #2019-01-06 14:00:15.285363
print(dt_now)       #2019-01-06 14:00:15.285363
print(dt_utcnow)    #2019-01-06 12:00:15.285363
```
## pytz: library for UTC
universal time zone, converion of string-datetime etc. 
```python
import datetime 
import pytz

# UTC - universal time coordinates.
dt = datetime.datetime(2019,7,1,12,30,45, tzinfo = pytz.UTC)
print(dt)

# we use now() for declaring utc
dt_utcnow = datetime.datetime.now(tz=pytz.UTC)
print(dt_utcnow)

dt_mtn= dt_utcnow.astimezone(pytz.timezone('US/Mountain'))
print(dt_mtn)

# will print the date in diffrent format:
print(dt_mtn.strftime('%B %d, %Y'))

# see all the timezones of pytz module: 
for tz in pytz.all_timezones:
    print(tz)

# change naive datetime to timezone aware:
dt = datetime.datetime.now()
dt_hebron = dt.astimezone(pytz.timezone('Asia/Hebron'))
print(dt_hebron)

# strftime- convert datetime to string.
# strptime- convert string to datetime:
dt_str = 'July 26, 2019'
dt=datetime.datetime.strptime(dt_str,'%B %d, %Y')
print(dt)

```