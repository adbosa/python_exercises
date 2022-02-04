import math
import pytest

class Point:
    ''' Point class for representing and manipulating x,y coordinates. '''

    def __init__(self, initX, initY):
        ''' Create a new point at the origin. '''
        self.x = initX
        self.y = initY

    def __str__(self):
        return 'x=' + str(self.x) + ', y=' + str(self.y)

    def distance(self, target1, target2):
        return 

    def distanceFromOrigin(self):
        return ((self.x**2) + (self.y**2))**0.5

    def halfway(self, target):
        mx = (self.x + target.x)/2
        my = (self.y + target.y)/2
        return Point(mx, my)

class TestPoint:

    def test_distance_from_origin(self):
        p = Point(7,6)
        assert p.distanceFromOrigin() == 9.219544457292887

    def test_halfway(self):
        p = Point(3,4)
        q = Point(5,12)
        assert p.halfway(q) == 'x=4.0, y=8.0'
