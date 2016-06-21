__author__ = 'dell'

import time
import calendar
ticks = time.time()
localtime = time.asctime(time.localtime(time.time()))

print("\n Current local time: ", localtime)
print("\n Number of ticks since 1 Jan 1970: ", ticks)
print("\n Author = ", __author__)

cal = calendar.month(1994, 11)

print("\n The June 2016 calender is as below: \n", cal)
print("\n Good bye")