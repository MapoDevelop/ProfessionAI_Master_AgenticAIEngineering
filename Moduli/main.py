"""Crea un file main.py che:
   - Importa Rectangle da geometry.py usando from ... import ...
   - Importa la funzione greet da utilities.py
   - Nel main, istanzia un rettangolo con dimensioni scelte e stampa 
   l’area utilizzando il metodo area.
   - Chiama greet passando un nome a scelta."""
   
import mypackage.geometry as geometry # importo il modulo geometry
from mypackage.utilities import greet # importo la funzione greet dal modulo utilities

rettangolo = geometry.Rectangle(4,5) # Inizializzo il rettangolo

print(rettangolo.area()) # Stampo l'area

greet("Elisa") # chiamo la funzione greet