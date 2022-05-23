#!/usr/bin/python
from calendar import Calendar

class MyCalendar(Calendar):
    def count_weekday_in_year(self, year, weekday):
        self.year = year
        self.weekday = weekday
        counter = 0
        for month in range(1, 13):
            for week in self.monthdays2calendar(self.year, month):
                for day, weekday in week:
                    if day != 0 and weekday == self.weekday:
                        counter += 1
        return counter

if __name__ == '__main__':
    first_test = MyCalendar()
    print(first_test.count_weekday_in_year(2019, 0)) # Must be 52
    print(first_test.count_weekday_in_year(2000, 6)) # Must be 53
