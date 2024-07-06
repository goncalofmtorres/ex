import math
from circulo import Circulo

class Cone:
    """
    base : Circulo
        Base do cone.
    _altura : float
        Altura do cone.
    """
    def __init__(self, base: Circulo, altura: float):
        """
        base : Circulo
            Base do cone.
        altura : float
            Altura do cone.
        """
        self.base = base
        self._altura = altura

    def calcVolume(self) -> float:
        """
        float
            Volume do cone.
        """
        areaBase = self.base.calcArea()
        return (areaBase * self._altura) / 3

    def calcGeratriz(self) -> float:
        """
        float
            Geratriz do cone.
        """
        return math.sqrt(self._altura**2 + self.base._raio**2)

    def calcAreaExterna(self) -> float:
        """
        Retorna
        float
            Área externa do cone.
        """
        areaBase = self.base.calcArea()
        areaLateral = math.pi * self.base._raio * self.calcGeratriz()
        return areaBase + areaLateral

    def __repr__(self):
        """
        Retorna
        str
            Representação da instância.
        """
        return f"Cone(base={self.base}, altura={self._altura})"
