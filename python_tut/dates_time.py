import pytz
import datetime

date1=datetime.date(2019,7,24)

date2=datetime.date(2019,7,28)

tdelta=datetime.timedelta(days=5)

print(date1-date2)

print(date1+tdelta)

print(date1-tdelta)


tdelta2=datetime.timedelta(days=-5)

print(date1-tdelta2)



t=datetime.time(9,30,45,100)
print(t.minute)

dt_utcnow=datetime.datetime.now(tz=pytz.UTC)



for tz in pytz.all_timezones:
        print (tz)
