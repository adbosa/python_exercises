from bhaskara import Bhaskara
import pytest

class TestBhaskara:
    '''Test program to find the unknown in a second degree equation. '''

    @pytest.fixture
    def bhaskara(self):
        return Bhaskara()

    @pytest.mark.parametrize("a, b, c, roots", [
        (1, 0, 0, (1, 0)),
        (10, 10, 10, 0),
        (1, -5, 6, (2, 3, 2)),
        (10, 20, 10, (1, -1)),
        (1, 8, -9, (2, 1, -9)),
        (1, 12, -13, (2, 1, -13))
        ])
    
    def test_unique_root(self, bhaskara, a, b, c, roots):
        ''' Testing an unique root. '''
        assert bhaskara.get_roots(a, b, c) == roots
