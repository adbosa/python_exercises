#!/usr/bin/python
class WeekDayError(Exception):
    pass

class Weeker:
    __days_of_week = ('Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun')

    def __init__(self, day):
        if not day in Weeker.__days_of_week:
            raise WeekDayError
        self.__position_day = Weeker.__days_of_week.index(day)

    def __str__(self):
        return Weeker.__days_of_week[self.__position_day]

    def add_days(self, n):
        self.__position_day += n % 7 

    def subtract_days(self, n):
        self.__position_day -= n % 7

if __name__ == '__main__':
    try:
        weekday = Weeker('Mon')
        print(weekday)
        weekday.add_days(15)
        print(weekday)
        weekday.subtract_days(23)
        print(weekday)
        weekday = Weeker('Monday')
    except WeekDayError:
        print('Sorry, I can\'t server your resquest.')

