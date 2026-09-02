"""

In questa esercitazione intermedia lavorerai sulla modularizzazione 
del codice Python, pratica fondamentale per mantenere un progetto leggibile, 
organizzato e facilmente manutenibile. Dovrai creare più file (.py) 
contenenti funzioni e classi, importarle correttamente nei file principali 
e combinare il tutto in un semplice package.

1. Crea un modulo chiamato geometry.py che contenga:
   - Una classe Shape con un metodo vuoto (usa pass) chiamato area.
   - Una classe Rectangle derivata da Shape, con costruttore __init__ 
   che accetta base e altezza. Implementa il metodo area che calcola 
   e restituisce base * altezza.

2. Crea un modulo utilities.py che contenga:
   - Una funzione greet(name) che riceve una stringa 
   e stampa un messaggio di benvenuto (es. "Ciao, {name}!").

3. Crea un file main.py che:
   - Importa Rectangle da geometry.py usando from ... import ...
   - Importa la funzione greet da utilities.py
   - Nel main, istanzia un rettangolo con dimensioni scelte e stampa 
   l’area utilizzando il metodo area.
   - Chiama greet passando un nome a scelta.

4. Organizza questi moduli in un package chiamato mypackage. Per farlo:
   - Crea una cartella mypackage
   - Sposta geometry.py e utilities.py dentro mypackage
   - All’interno della cartella mypackage crea un file __init__.py (può essere vuoto).

5. Modifica main.py per importare da mypackage.geometry e mypackage.utilities, 
e verifica che tutto funzioni correttamente.

Obiettivo: ottenere un codice suddiviso e organizzato in moduli e package, 
usando importazioni corrette e rispettando le convenzioni di Python. 
Potrai così utilizzare lo stesso package mypackage in altri programmi 
senza riscrivere il codice.

Per questa esercitazione non serve scrivere codice complesso, ma assicurati 
di gestire correttamente i nomi di file, le importazioni, l’uso della keyword pass 
e la definizione di metodi e classi. Ricordati l’uso di self nei metodi d’istanza.

Alla fine, esegui main.py e verifica che venga stampato il messaggio di benvenuto 
e l’area calcolata correttamente.

Esempi Input/Output
input:
# Nessun input da tastiera necessario

output:
Ciao, Maria!
Area del rettangolo: 20

input:
# Nessun input da tastiera necessario

output:
Ciao, Luca!
Area del rettangolo: 50

"""