from bhaskara import Bhaskara
import pytest

class TestBhaskara:
    '''Test program to find the unknown in a second degree equation. '''

    @pytest.fixture
    def b(self):
        return Bhaskara()

    @pytest.mark.parametrize("x, y", [
        (2, 4), (5, 2), (2, 6)
        ])
    
    def test_unique_root(self, b):
        ''' Testing an unique root. '''
        assert b.get_roots(x) == y



        '''((1, 0, 0), (1, 0)),
        ((10, 10, 10), 0),
        ((1, -5, 6), (2, 3, 2)),
        ((10, 20, 10), (1, -1)),
        '''
        
