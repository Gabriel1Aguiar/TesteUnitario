import unittest
import pytest
from modularizado.fatorial import fatorial

class TestFatorial(unittest.TestCase):
    def test_fatorial_negativo(self):
        with pytest.raises(ValueError):
            fatorial(-5)

    def test_fatorial_decimal(self):
        with pytest.raises(TypeError):
            fatorial(3.5)

    def test_fatorial_zero(self):
        assert fatorial(0) == 1

    def test_fatorial_positivo(self):
        assert fatorial(5) == 120