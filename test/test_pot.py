import unittest
import pytest
from modularizado.pot import pot

class TestPotencia(unittest.TestCase):
    def test_pot_zero(self):
        with pytest.raises(ValueError):
            pot(0,2)
    
    def test_pot_zero_n2(self):
        assert pot(8,0) == 1

    def test_pot_letra1(self):
        with pytest.raises(TypeError):
            pot("a",2)
    
    def test_pot_letra2(self):
        with pytest.raises(TypeError):
            pot(2,"b")

    def test_pot_1negativo(self):
        assert pot(8,-1) == 0.125
    
    def test_pot_2negativo(self):
        assert pot(-1,-4) == 1

    def test_pot_positivo(self):
        assert pot(5,2) == 25