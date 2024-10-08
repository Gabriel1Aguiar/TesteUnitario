import unittest
import pytest
from modularizado.subt import subt

class TestSubtracao(unittest.TestCase):
    def test_subt_letra(self):
        with pytest.raises(TypeError):
            subt("a")

    def test_subt_negativo(self):
        assert subt(1,-4) == 5

    def test_subt_positivo(self):
        assert subt(5,2) == 3
    
    def test_subt_zero(self):
        assert subt(5,0) == 5

    def test_subt_zero_n1(self):
        assert subt(0,5) == -5