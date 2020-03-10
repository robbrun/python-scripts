#get datetime function from datetime library.
from datetime import datetime, timedelta, timezone

today = datetime.now()
current_date = datetime.now()
#the now function returns a datetime object
print('Today is: ' + str(current_date))

#timedelta is used to define a period of time

one_day = timedelta(days=1)
yesterday = today - one_day
print('Yesterday was: ' + str(yesterday))

#date formatting
print('Day: ' + str(current_date.day))
print('Month: ' + str(current_date.month))
print('Year: ' + str(current_date.year))
