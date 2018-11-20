import datetime 
from datetime import date

import os

def diff_dates(date1, date2):
    return abs(date2-date1).days

d1 = date(2016, 11, 1)
d2 = date(2017, 9, 23)

result1 = diff_dates(d2, d1)

print ('{} days between {} and {}'.format(result1, d1, d2))

now = datetime.datetime.now()

print ("CWD : " + os.getcwd())
print (now.strftime("%Y-%m-%d %H:%M"))

print ("Current date and time using isoformat:")
print (now.isoformat())
