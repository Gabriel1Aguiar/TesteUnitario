import unittest
import pytest
from modularizado.div import div

class TestDivisao(unittest.TestCase):
    def test_div_zero(self):
        with pytest.raises(ValueError):
            div(1,0)

    def test_div_letra1(self):
        with pytest.raises(TypeError):
            div("a",2)

    def test_div_letra2(self):
        with pytest.raises(TypeError):
            div(2,"b")

    def test_div_1negativo(self):
        assert div(4,-1) == -4
    
    def test_div_2negativo(self):
        assert div(-4, -1) == 4  

    def test_div_positivo(self):
        assert div(50,2) == 25