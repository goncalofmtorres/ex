import unittest
from ponto import Ponto
from circulo import Circulo

class TestCirculo(unittest.TestCase):
    def test_area_circulo(self):
        p = Ponto(0, 0)
        c = Circulo(p, 3)
        self.assertAlmostEqual(c.calcArea(), 28.274333882308138, places=5)

    def test_perimetro_circulo(self):
        p = Ponto(0, 0)
        c = Circulo(p, 3)
        self.assertAlmostEqual(c.calcPerimetro(), 18.84955592153876, places=5)

if __name__ == '__main__':
    unittest.main()