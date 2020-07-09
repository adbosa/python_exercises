from bhaskara import Bhaskara

class TestBhaskara:
    '''Test program to find the unknown in a second degree equation. '''

    def test_unique_root():
        ''' Testing an unique root. '''
        b = Bhaskara( )
        assert b.get_roots(1, 0, 0) == (1, 0)
