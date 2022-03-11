#!/usr/bin/python
class Timer:
    def __init__(self, hh, mm, ss):
        self.__hour = hh
        self.__minute = mm
        self.__second = ss

    def __str__(self):
        __display = self.__formatTime(self.__hour, self.__minute, self.__second)
        return __display 

    def next_second(self):
        if self.__second + 1 > 59:
            self.__next_minute()
            self.__second = 00
        else:
            self.__second += 1

    def __next_minute(self):
        if self.__minute + 1 > 59:
            self.__next_hour()
            self.__minute = 00
        else:
            self.__minute += 1

    def __next_hour(self):
        if self.__hour + 1 > 23:
            self.__hour = 00
        else:
            self.__hour += 1

    def prev_second(self):
        if self.__second - 1 < 0:
            self.__prev_minute()
            self.__second = 59
        else:
            self.__second -= 1

    def __prev_minute(self):
        if self.__minute - 1 < 0:
            self.__prev_hour()
            self.__minute = 59
        else:
            self.__minute -= 1

    def __prev_hour(self):
        if self.__hour - 1 < 0:
            self.__hour = 23
        else:
            self.__hour -= 1

    def __formatTime(self, hh, mm, ss):
        formatted = ''
        time = [hh, mm, ss]
        for elem in time:
            if elem < 10:
                formatted += '0'
            formatted += str(elem)
            if len(formatted) < 7: formatted += ':'

        return formatted

if __name__ == '__main__':
    timer = Timer(23, 59, 59)
    print(timer)
    timer.next_second()
    print(timer)
    timer.prev_second()
    print(timer)
