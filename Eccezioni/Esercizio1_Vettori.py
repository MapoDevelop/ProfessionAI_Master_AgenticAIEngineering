"""
Esercizio della programmazione ad oggetti ripensato con le eccezioni.

"""

import math


class Vector:
    
    def __init__(self, values):
        self.values = values
    
    def __getitem__(self, i): # metodo per supportare l'indexing
        """Ritorna l'elemento alla posizione i del vettore"""
        return self.values[i]
    
    # Stampando un'oggetto Vector il risultato sarà la lista dei suoi valori
    def __repr__(self):
        """Ritorna la rappresentazione del vettore"""
        return f"Vector({self.values})"
    
    # Sommando due oggetti Vector il risultato sarà un nuovo oggetto Vector
    def __add__(self, vector): # metodo per la somma di due vettori
        """Ritorna un nuovo oggetto Vector composto dalla somma dei valori dei due vettori alle posizioni corrispondenti"""
        return Vector([a + b for a, b in zip(self.values, vector.values)])
    
    # Sottraendo un'oggetto Vector ad un'altro oggetto Vector
    def __sub__(self, vector):
        """Ritorna un nuovo oggetto Vector composto dalla differenza dei valori dei due vettori alle posizioni corrispondenti"""
        return Vector([a - b for a, b in zip(self.values, vector.values)])
    
    # Un confronto di uguaglianza tra due vettori
    def __eq__(self, vector):
        """Ritorna True se i vettori hanno esattamente gli stessi elementi, altrimenti ritorna False"""
        return self.values == vector.values

    # Moltiplicando due oggetti Vector il risultato dovrà essere il prodotto scalare dei due vettori
    # (es. Vector([1,2,3]) * Vector([2,4,6]) = 28. -> 1*2 + 2*4 + 3*6
    def __mul__(self, vector):
        """Ritorna il prodotto scalare dei due vettori"""
        return sum(a * b for a, b in zip(self.values, vector.values))
    
    def sum(self):
        """Ritorna la somma di tutti gli elementi del vettore"""
        return sum(self.values)
    
    # ritorna la norma del vettore, cioè la radice quadrata del prodotto scalare 
    # tra il vettore e se stesso 
    def norm(self):
        """Ritorna la norma del vettore"""
        return math.sqrt(sum(a * a for a in self.values))
    
vettore1 = Vector([1,2,3]) 
vettore2 = Vector([2,4,6]) 
vettore4 = Vector([10, 20, 30, 40])

print(vettore1)

# if len(vettore1.values) == len(vettore2.values):
try:
    assert len(vettore1.values) == len(vettore2.values), "I vettori devono avere lo stesso numero di elementi"
        
    print(f"I vettori hanno la stessa dimensione")
    # Sommando due oggetti Vector il risultato sarà un nuovo oggetto Vector
    vettore3 = vettore1.__add__(vettore2)
    print(f"Somma di {vettore1} e {vettore2} = {vettore3}")

    # Sottraendo un'oggetto Vector ad un'altro oggetto Vector
    vettore5 = vettore1.__sub__(vettore2)
    print(f"Sottrazione di {vettore1} meno {vettore2} = {vettore5}")

    # Moltiplicando due oggetti Vector il risultato dovrà essere il prodotto scalare dei due vettori
    vettore3 = vettore1.__mul__(vettore2)
    print(f"Moltiplicazione di {vettore1} per {vettore2} = {vettore3}")

    # Un confronto di uguaglianza tra due vettori
    print(f"Confronto di uguaglianza tra {vettore1} e {vettore2} = {vettore1.__eq__(vettore1)}")
# Stampo il messaggio di errore dell'assert 
# in questo caso controllo che i numeri siano positivi
except AssertionError as e:
    print(e)

print(f"Somma di {vettore1} = {vettore1.sum()}")
print(f"Norma di {vettore1} = {vettore1.norm()}")
print(vettore1[1])

print(f"Norma di {vettore4} = {vettore4.norm()}")