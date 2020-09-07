class Rational:
    def __init__(self, n = 0, d = 1):
        self.put(n, d)

    def __str__(self):
        if(self.den == 1): # If denominator is equal to one print only numerator
            return f'{self.num}'
        else:
            return f'{self.num}/{self.den}'

    def get(self):
        return self.num, self.den

    def put(self, n = 0, d =1):
        self.num, self.den = n, d

    def mult(self, other):
        n = self.num * other.num
        d = self.den * other.den
        return Rational(n, d)

    def div(self, other):
        if other.num < 0: # invert signal if racioal is negative
            other.num *= -1
            other.den *= -1
        n = self.num * other.den
        d = self.den * other.num
        return Rational(n, d)

    def add(self, other):
        if(self.den == other.den): # if the demominators are equal
            n = self.num + other.num
            d = self.den
        else:                      # if don't  
            d = Rational.lcm(self.den, other.den)
            n = ((d/self.den) * self.num + (d/other.den) * other.num)
        return Rational(n, d)

    def sub(self, other):
        if(self.den == other.den):
            n = self.num - other.num
            d = self.den
        else:
            d = Rational.lcm(self.den, other.den)
            n = ((d/self.den) * self.num + (d/other.den) * other.num)
        return Rational(n, d)

    def lcm(x, y):
        '''Receives two integers and returns LCM between them.'''
        if x > y :
            greater = x
        else:
            greater = y

        while(True):
            if(( greater % x == 0 ) and ( greater % y ==0)):
                lcm = greater
                break
            greater += 1

        return lcm

import pytest
class Tests_Rational_Operations:

### Multiplications tests ###
    def test_multiplication_with_positives(self):
        r1 = Rational(3, 4)
        r2 = Rational(2, 5)
        assert r1.mult(r2).get() == (6, 20)

    def test_multiplication_with_negatives(self):
        r1 = Rational(-7, 10)
        r2 = Rational(-2, 3)
        assert r1.mult(r2).get() == (14, 30)

### Divisions tests ###
    def test_divisao_positivos(self):
        r1 = Rational(3, 4)
        r2 = Rational(1, 6)
        assert r1.div(r2).get() == (18, 4)

    def test_divisao_com_negativos(self):
        r1 = Rational(-24, 1)
        r2 = Rational(-1, 2)
        assert r1.div(r2).get() == (48, 1)

### LCM tests ###
    def test_lcm_one(self):
        den1 = 3
        den2 = 7
        assert Rational.lcm(den1, den2) == 21

    def test_lcm_two(self):
        den1 = 18
        den2 = 60
        assert Rational.lcm(den1, den2) == 180

    def test_lcm_three(self):
        den1 = 10
        den2 = 5
        assert Rational.lcm(den1, den2) == 10

### Additions tests ###
    def test_sum_of_rationals_1(self):
        r1 = Rational(-1, 5)
        r2 = Rational(-9, 5)
        assert r1.add(r2).get() == (-10, 5)

    def test_sum_of_rationals_2(self):
        r1 = Rational(-4, 7)
        r2 = Rational(2, 3)
        assert r1.add(r2).get() == (2, 21)

### Subtractions tests ###
    def test_subtraction_of_rationals_1(self):
        r1 = Rational(-7, 6)
        r2 = Rational(-5, 4)
        assert r1.sub(r2).get() == (-29, 12)

    def test_subtraction_of_rationals_2(self):
        r1 = Rational(8, 5)
        r2 = Rational(3, 5)
        assert r1.sub(r2).get() == (5, 5)
