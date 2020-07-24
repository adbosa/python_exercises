''' Teste de funções com triangulos, precisa receber e armazenar instancias
de uma classe chamada triangulo, calcular seu perimetro e classificar o objeto
pela comparação de suas medidas.
'''
import pytest
import triangulo

class TestaTriangulo:
    @pytest.mark.parametrize('lado_a, lado_b, lado_c', [
        (2, 2, 2),
        (1, 2, 3),
        (1, 1, 2)])
        
    def test_instanciamento_de_a(self, lado_a, lado_b, lado_c):
        t = triangulo.Triangulo(lado_a, lado_b, lado_c)
        assert t.a == lado_a
        assert t.b == lado_b
        assert t.c == lado_c

    @pytest.mark.parametrize('lado_a, lado_b, lado_c, soma', [
        (2, 2, 2, 6),
        (1, 2, 3, 6),
        (1, 1, 2, 4)])
    def test_perimetro(self, lado_a, lado_b, lado_c, soma):
        t = triangulo.Triangulo(lado_a, lado_b, lado_c)
        assert t.perimetro() == soma

    @pytest.mark.parametrize('lado_a, lado_b, lado_c, tipo', [
        (2, 2, 2, 'equilátero'),
        (1, 2, 3, 'escaleno'),
        (1, 1, 2, 'isósceles')])
    def test_tipo_de_triangulo(self, lado_a, lado_b, lado_c, tipo):
        t = triangulo.Triangulo(lado_a, lado_b, lado_c)
        assert t.tipo_lado() == tipo

    def test_se_triangulo_retangulo(self):
        t = triangulo.Triangulo(3, 4, 5)
        assert t.retangulo() == True

    def test_se_triangulo_não_retangulo(self):
        t = triangulo.Triangulo(1, 3, 5)
        assert t.retangulo() == False

    def test_triangulos_semelhantes_1(self):
        t1 = triangulo.Triangulo(2, 2, 2)
        t2 = triangulo.Triangulo(4, 4, 4)
        assert t1.semelhantes(t2) == True

    def test_triangulos_semelhantes_2(self):
        t1 = triangulo.Triangulo(5, 5.83, 3)
        t2 = triangulo.Triangulo(10, 11.66, 6)
        assert t1.semelhantes(t2) == True

    def test_triangulos_não_semelhantes(self):
        t1 = triangulo.Triangulo(3, 7, 8)
        t2 = triangulo.Triangulo(2, 2, 2)
        assert t1.semelhantes(t2) == False
