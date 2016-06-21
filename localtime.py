__author__ = 'dell'

import time
import calendar

def ProcTime():
    time.sleep(5)

ticks = time.time()
localtime = time.asctime(time.localtime(time.time()))

print("\n Current local time: ", localtime)
print("\n Number of ticks since 1 Jan 1970: ", ticks)
print("\n Author = ", __author__)

cal = calendar.month(1994, 11)

print("\n The June 2016 calender is as below: \n", cal)

t0 = time.clock()
ProcTime()
print("\n Time to run ProcTime function: ", time.clock() - t0)

print("\n Good bye")