#get datetime function from datetime library.
from datetime import datetime, timedelta, timezone

current_date = datetime.now()
#the now function returns a datetime object
today = datetime.now()
print('Today is: ' + str(current_date))


one_day = timedelta(days=1)
yesterday = today - one_day
print('Yesterday was: ' + str(yesterday))

one_week = timedelta(weeks=1)
last_week = today - one_week
print('One week ago was: ' + str(last_week))

print('Day of the month: ' + str(today.day))
print('Month of the year: ' + str(today.month))
print('Year: ' + str(today.year))
print('Current hour: ' + str(today.hour))
print('Current minute: ' + str(today.minute))