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

class Triangle:
    def __init__(self, vertice1, vertice2, vertice3):
        self.__vertices = (vertice1, vertice2, vertice3)

    def perimeter(self):
        perimeter = 0

        for i in range(3):
            perimeter += self.__vertices[i].distance_from_point(self.__vertices[(i + 1) % 3])
        
        return perimeter
    


if __name__ == '__main__':
    triangle = Triangle(Point(0, 0), Point(1, 0), Point(0, 1))
    if triangle.perimeter() == 3.414213562373095:
        print('Pass')
    else:
        print('Failure')
