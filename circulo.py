import math
from ponto import Ponto

class Circulo:
    """
    centro : Ponto
        Centro do círculo.
    _raio : float
        Raio do círculo.
    """
    def __init__(self, centro: Ponto, raio: float):
        """
        centro : Ponto
            Centro do círculo.
        raio : float
            Raio do círculo.
        """
        self.centro = centro
        self._raio = raio

    def calcArea(self) -> float:
        """
        float
            Área do círculo.
        """
        return math.pi * self._raio**2

    def calcPerimetro(self) -> float:
        """
        float
            Perímetro do círculo.
        """
        return 2 * math.pi * self._raio

    def __repr__(self):
        """
        str
            Representação da instância.
        """
        return f"Circulo(centro={self.centro}, raio={self._raio})"
