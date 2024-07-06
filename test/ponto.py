import unittest
from ponto import Ponto

class TestPonto(unittest.TestCase):
    def test_distancia_positiva(self):
        p1 = Ponto(0, 0)
        p2 = Ponto(3, 4)
        self.assertEqual(p1.Dist2P(p2), 5.0)

    def test_mesmo_ponto_distancia_zero(self):
        p1 = Ponto(1, 1)
        p2 = Ponto(1, 1)
        self.assertEqual(p1.Dist2P(p2), 0.0)

if __name__ == '__main__':
    unittest.main()
