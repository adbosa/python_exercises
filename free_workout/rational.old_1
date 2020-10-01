class Racional:
    def __init__(self, n = 0, d = 1):
        self.put(n, d)

    def __str__(self):
        return "%d/%d"%(self.num, self.den)

    def get(self):
        return self.num, self.den

    def put(self, n = 0, d =1):
        self.num, self.den = n, d

    def mult(self, other):
        n = self.num * other.num
        d = self.den * other.den
        return Racional(n, d)

    def div(self, other):
        if other.num < 0: # invert signal if racioal is negative
            other.num *= -1
            other.den *= -1
        n = self.num * other.den
        d = self.den * other.num
        return Racional(n, d)

    def add(self, other):
        pass

    def sub(self, other):
        pass

    def mmc(self):
        pass

import pytest
class Testa_Racionais:

    def testa_multiplicacao_positivos(self):
        r1 = Racional(3, 4)
        r2 = Racional(2, 5)
        assert r1.mult(r2).get() == (6, 20)

    def testa_multiplicacao_com_negativos(self):
        r1 = Racional(-7, 10)
        r2 = Racional(-2, 3)
        assert r1.mult(r2).get() == (14, 30)

    def testa_divisao_positivos(self):
        r1 = Racional(3, 4)
        r2 = Racional(1, 6)
        assert r1.div(r2).get() == (18, 4)

    def testa_divisao_com_negativos(self):
        r1 = Racional(-24, 1)
        r2 = Racional(-1, 2)
        assert r1.div(r2).get() == (48, 1)

    def testa_mmc(self):
        r1 = 7
        r2 = 3
        assert mmcr1(r1, r2) == 21

    def testa_soma_de_racionais_1(self):
        r1 = Racional(-1, 5)
        r2 = Racional(-9, 5)
        assert r1.add(r2) == (-10, 5)

    def testa_soma_de_racionais_2(self):
        r1 = Racional(-4, 7)
        r2 = Racional(2, 3)
        assert r1.add(r2) == (2, 21)

    def testa_subtracao_de_racionais_1(self):
        r1 = Racional(1, 7)
        r2 = Racional(1, 3)
        assert r1.sub(r2) == (-4, 21)

    def testa_subtracao_de_racionais_2(self):
        r1 = Racional(-7, 6)
        r2 = Racional(-5, 4)
        assert r1.sub(r2) == (-29, 12)
