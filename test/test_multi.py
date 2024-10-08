import unittest
import pytest
from modularizado.multi import multi

class TestMultiplicacao(unittest.TestCase):
    def test_multi_letra1(self):
        with pytest.raises(TypeError):
            multi("a",2)
    def test_multi_letra2(self):
        with pytest.raises(TypeError):
            multi(2,"b")

    def test_multi_1negativo(self):
        assert multi(1,-4) == -4
    
    def test_multi_2negativo(self):
        assert multi(-1,-4) == 4

    def test_multi_positivo(self):
        assert multi(5,2) == 10
    
    def test_multi_zero(self):
        assert multi(5,0) == 0

    def test_multi_zero_n1(self):
        assert multi(0,5) == 0