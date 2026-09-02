# Creo un classe Shape con un metodo vuoto (usa pass) chiamato area 
class Shape:
    """
    Classe di base per le forme geometriche.    
    """
    def area(self):
        pass

# Creo una classe Rectangle derivata da Shape, con costruttore __init__ 
# che accetta base e altezza. Implementa il metodo area che calcola 
# e restituisce base * altezza.
class Rectangle(Shape):
    """
    Classe che rappresenta un rettangolo, derivata dalla classe Shape.
    """
    def __init__(self, base, altezza):
        """
        Inizializza un nuovo oggetto Rectangle.

        Args:
            base (int): la base del rettangolo.
            altezza (int): l'altezza del rettangolo.
        """
        self.base = base
        self.altezza = altezza

    def area(self):
        """
        Calcolo dell'area del rettangolo

        Returns:
            float: l'area del rettangolo.
        """
        return self.base * self.altezza