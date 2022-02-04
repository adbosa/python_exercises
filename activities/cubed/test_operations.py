''' Test various arguments for test a function.'''
import pytest
import operations

class TestCubed:
    @pytest.fixture
    def cubed(self):
        return operations.Cubed()
    @pytest.mark.parametrize('num_in, num_out', [
        (0,0),
        (1,1),
        (2,8),
        (-2,-8),
        (10,1000)
        ])
    
    def test_mult(self, cubed, num_in, num_out):
        assert cubed.main(num_in) == num_out
