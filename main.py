# main.py
from ponto import Ponto
from circulo import Circulo
from cone import Cone

def main():
    # Criando instâncias de Ponto
    p1 = Ponto(0, 0)
    p2 = Ponto(3, 4)
    p3 = Ponto(1, 1)

    print(f"Ponto 1: {p1}")
    print(f"Ponto 2: {p2}")
    print(f"Distância entre p1 e p2: {p1.Dist2P(p2):.2f}")
    print(f"Distância entre p1 e p3: {p1.Dist2P(p3):.2f}")

    circulo1 = Circulo(p1, 5)
    circulo2 = Circulo(p2, 3)

    print(f"Circulo 1: {circulo1}")
    print(f"Área do circulo 1: {circulo1.calcArea():.2f}")
    print(f"Perímetro do circulo 1: {circulo1.calcPerimetro():.2f}")

    print(f"Circulo 2: {circulo2}")
    print(f"Área do circulo 2: {circulo2.calcArea():.2f}")
    print(f"Perímetro do circulo 2: {circulo2.calcPerimetro():.2f}")

    cone1 = Cone(circulo1, 10)

    print(f"Cone 1: {cone1}")
    print(f"Volume do cone 1: {cone1.calcVolume():.2f}")
    print(f"Geratriz do cone 1: {cone1.calcGeratriz():.2f}")
    print(f"Área externa do cone 1: {cone1.calcAreaExterna():.2f}")

if __name__ == "__main__":
    main()
