#!/usr/bin/python
import math

class Point:
    def __init__(self, x=0.0, y=0.0):
        self.__coord = (x, y)

    def getx(self):
        return self.__coord[0]
    
    def gety(self):
        return self.__coord[1]

    def distance_from_xy(self, x, y):
        return math.hypot(x - self.getx(),y - self.gety())

    def distance_from_point(self, point):
        return self.distance_from_xy(point.getx(), point.gety())


if __name__ == '__main__':
    point1 = Point(0, 0)
    point2 = Point(1, 1)

    def test_distance_from_point():
        if point1.distance_from_point(point2) == 1.4142135623730951:
            print('Pass')
        else:
            print('Distance from point: Failure')
    
    def test_distance_from_xy():
        if point2.distance_from_xy(2, 0) == 1.4142135623730951:
            print('Pass')
        else:
            print('Distance from xy: Failure')

    test_distance_from_point()
    test_distance_from_xy()
