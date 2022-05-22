#!/usr/bin/python
from calendar import Calendar

class MyCalendar(Calendar):
    def count_weekday_in_year(self, year, weekday):
        self.year = year
        self.weekday = weekday
        for month in range(1, 13):
            print(self.monthdays2calendar(self.year, month))

if __name__ == '__main__':
    first_test = MyCalendar()
    first_test.count_weekday_in_year(2019, 0)
