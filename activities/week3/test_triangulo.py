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
