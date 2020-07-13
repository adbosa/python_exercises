''' Testa a função que retorna o quadrado de qualquer número passado. '''
import pytest
import operations

class TestSquared:
    @pytest.fixture
    def squared_test():
        return squared.Square()
    @pytest.mark.parametrize('base, result', [(0, 1), (1, 1), (2, 8), (-2, -8),
                                              (10, 1000)])
    def test_squared(self, squared_test):
        assert squared_test.main(base) == result


    
