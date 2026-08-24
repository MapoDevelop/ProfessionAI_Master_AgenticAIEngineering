# Crea una classe base chiamata Shape, 
# che rappresenta una figura geometrica generica. 
# Il suo costruttore deve accettare una tupla di lati 
# e un valore di altezza (che può essere None se non applicabile). 
# Salva questi come attributi dell'istanza.

class Shape:
    """
    Rappresenta una figura geometrica
    """
    
    def __init__(self, lati, altezza = None):
        """Inizializzazione con la tupla dei lati e l'altezza"""
        self.lati = lati
        self.altezza = altezza
        
    # Definisci nella classe Shape due metodi chiamati perimetro e area, 
    # che al momento non dovranno calcolare nulla ma solo usare la keyword pass 
    # (così la Shape resta generica).
    
    def perimetro(self):
        """Calcolo del perimetro"""
        pass
    
    def area(self):
        """Calcolo dell'area"""
        pass
    
# Crea una classe derivata Triangle che erediti da Shape. 
# Nel costruttore dovrai richiamare quello della superclasse 
# passando la tupla di tre lati e l'altezza.
class Triangle(Shape):
    
    def __init__(self, lati, altezza=None):
        super().__init__(lati, altezza)
        self.lati = lati
        self.altezza = altezza
        
        
    # Sovrascrivi (override) nella classe Triangle i metodi perimetro e area 
    # il perimetro è la somma dei lati, 
    # l'area è base * altezza / 2 (assumendo che la base sia il primo lato della tupla dei lati).
    
    def perimetro(self):
        """Calcolo del perimetro del triangolo"""
        return self.lati[0]+self.lati[1]+self.lati[2]
        
    def area(self):
        """Calcolo dell'area del triangolo"""
        return self.lati[0]*self.altezza/2
    
    def __repr__(self):
        """Stampa delle informazioni del triangolo"""
        return f"Il triangolo con lati {self.lati} e altezza {self.altezza} \n ha un perimetro di {self.perimetro()} e un'area di  {self.area()}"
    
# Crea una classe derivata Square che erediti da Shape. 
# Nel costruttore richiamate quello della superclasse 
# con la tupla contenente quattro lati uguali // è errato, il lato è solo uno (la base)
# e l'altezza (che può coincidere con il lato). // è errato, non si calcola l'altezza perché è uguale alla base

class Square(Shape):
    def __init__(self, lati):
            super().__init__(lati)
            self.lati = lati
            
    # Sovrascrivi nella classe Square 
    # il metodo perimetro calcolandolo come 4 * lato. 
    # Implementa l'area come lato * lato.
    
    def perimetro(self):
        """Calcolo del perimetro del quadrato"""
        return self.lati * 4
    
    def area(self):
        """Calcolo dell'area del quadrato"""
        return self.lati**2
    
    def __repr__(self):
        """Stampa delle informazioni del quadrato"""
        return f"Il quadrato con lato {self.lati} \n ha un perimetro di {self.perimetro()} e un'area di {self.area()}"
    
    
triangolo = Triangle((2,3,4),3)
print(triangolo.perimetro())
print(triangolo.area())
print(triangolo)

quadrato = Square(5)
print(quadrato.perimetro())
print(quadrato.area())
print(quadrato)