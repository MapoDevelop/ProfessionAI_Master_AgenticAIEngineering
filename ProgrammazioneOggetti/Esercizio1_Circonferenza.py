# Definisci una classe Cerchio che prenda in input il raggio
# metodi: calcolo_diametro, calcolo_circonferenza, calcolo_area
import math

class Cerchio:
    def __init__(self, raggio : float):
        """raggio: float : Il raggio del cerchio"""
        self.raggio = raggio
        
    def calcolo_diametro(self):
        """Calcolo del diametro del cerchio"""
        return self.raggio*2
    
    def calcolo_circonferenza(self):
        """Calcolo della circonferenza del cerchio"""
        return round((self.calcolo_diametro() * math.pi),2)
    
    def calcolo_area(self):
        """Calcolo dell'area del cerchio"""
        return round(math.pi * (self.raggio**2), 2)
        
    def __repr__(self):
        """Rappresentazione del cerchio - restituisce il diametro, la circonferenza e l'area del cerchio"""
        return f"Il cerchio con raggio {self.raggio} ha un diametro di {self.calcolo_diametro()}, una circonferenza di {self.calcolo_circonferenza()} e un'area di {self.calcolo_area()}"
    
cerchio = Cerchio(float(5))
print(cerchio)