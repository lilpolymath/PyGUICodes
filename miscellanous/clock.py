#Update 14/05/2018
#Code wont run yet....
#Needs the required modules to work...

from clock import Clock
from calendar import Calendar

class CalendarClock(Clock, day.month.years, hours = 0, minutes = 0, seconds = 0):
    Calendar.__init__(self, day, month, year)
    Clock.__init__(self, hours, minutes, seconds)

    def __str__(self):
        return Calendar.__str__(self) + ". " + Clock.__self__(self)

if __name__ == "__main__":
    x = CalendarClock(24, 12, 57)
    print(x)
    for i in range(1000):
        x.tick()
    for i in range(1000):
        x.advance()
    print(x)
