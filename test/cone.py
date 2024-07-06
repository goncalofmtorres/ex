import unittest
from ponto import Ponto
from circulo import Circulo
from cone import Cone

class TestCone(unittest.TestCase):
    def test_volume_cone(self):
        p = Ponto(0, 0)
        c = Circulo(p, 3)
        cone = Cone(c, 5)
        self.assertAlmostEqual(cone.calcVolume(), 47.12388980384689, places=5)

    def test_area_externa_cone(self):
        p = Ponto(0, 0)
        c = Circulo(p, 3)
        cone = Cone(c, 5)
        self.assertAlmostEqual(cone.calcAreaExterna(), 83.22976079115259, places=5)

if __name__ == '__main__':
    unittest.main()
