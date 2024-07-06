import math

class Ponto:
    """
    x : float
        Coordenada x do ponto.
    y : float
        Coordenada y do ponto.
    """
    def __init__(self, x: float, y: float):
        """
        x : float
            Coordenada x do ponto.
        y : float
            Coordenada y do ponto.
        """
        self.x = x
        self.y = y

    def Dist2P(self, p: 'Ponto') -> float:
        """
        p : Ponto
            Outro ponto para calcular a distância.

        Retorna
        float
            Distância até o outro ponto.
        """
        return math.sqrt((self.x - p.x)**2 + (self.y - p.y)**2)

    def __repr__(self):
        """
        Retorna
        str
            Representação da instância.
        """
        return f"Ponto(x={self.x}, y={self.y})"
