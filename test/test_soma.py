import unittest
import pytest
from modularizado.soma import soma

class TestSoma(unittest.TestCase):
    def test_soma_letra(self):
        with pytest.raises(TypeError):
            soma("a")

    def test_soma_negativo(self):
        assert soma(1,-4) == -3

    def test_soma_positivo(self):
        assert soma(5,2) == 7