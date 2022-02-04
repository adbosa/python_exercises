from bhaskara import Bhaskara
import pytest

class TestBhaskara:
    '''Test program to find the unknown in a second degree equation. '''

    @pytest.fixture
    def b(self):
        return Bhaskara()

    @pytest.mark.parametrize("x,y", [(1, 2), (2, 3), (3, 4)])
    def test_test(self, b):
        assert b.get_roots(x) == y
