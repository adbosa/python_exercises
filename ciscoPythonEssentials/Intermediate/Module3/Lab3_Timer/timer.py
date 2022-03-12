#!/usr/bin/python

def two_digits(val):
    time = str(val)
    if len(time) < 2:
        time = '0' + time
    return time

class Timer:
    def __init__(self, hh, mm, ss):
        self.__hour   = hh
        self.__minute = mm
        self.__second = ss

    def __str__(self):
        return  two_digits(self.__hour)   + ':' + \
                two_digits(self.__minute) + ':' + \
                two_digits(self.__second)

    def next_second(self):
        self.__second += 1
        if self.__second > 59:
            self.__second = 00
            self.__minute += 1
            if self.__minute > 59:
                self.__minute = 00
                self.__hour += 1
                if self.__hour > 23:
                    self.__hour = 00

    def prev_second(self):
        self.__second -= 1
        if self.__second < 00:
            self.__second = 59
            self.__minute -= 1
            if self.__minute < 00:
                self.__minute = 59
                self.__hour -= 1
                if self.__hour < 00:
                    self.__hour = 23


if __name__ == '__main__':
    timer = Timer(23, 59, 59)
    print(timer)
    timer.next_second()
    print(timer)
    timer.prev_second()
    print(timer)
