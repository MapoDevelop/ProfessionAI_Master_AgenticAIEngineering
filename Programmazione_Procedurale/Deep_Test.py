# Definisci una funzione chiamata `media_lista`
# che riceve una lista di numeri (interi o float) come parametro
# e ritorna la media aritmetica (somma divisa per il numero di elementi)

def media_lista(numeri):
    somma = sum(numeri)
    media = somma/len(numeri)
    return media

# Definisci una funzione chiamata `maximum` 
# che riceve una lista di numeri 
# e ritorna il valore massimo presente.

def maximum(numeri):
    return max(numeri)

# Definisci una funzione chiamata `stampa_lista_indicizzata` 
# che riceve una lista di elementi e stampa ogni elemento 
# preceduto dal suo indice partendo da 1 (es. "1. elemento").

def stampa_lista_indicizzata(lista):
    for indice, elemento in enumerate(lista, start=1):
        print(f"{indice}. {elemento}")
   
# Nel programma principale (main), 
# leggi dall'utente una serie di numeri separati da spazi 
# e convertili in una lista di numeri float. 
numeri_input = list(map(float, input("Inserisci una lista di numeri: ").split()))
lista_spesa = ["pane", "latte", "uova", "burro", "formaggio"]

# Utilizza le funzioni definite per:
# - Calcolare e stampare la media della lista.
# - Calcolare e stampare il massimo valore della lista.
# - Stampare la lista indicizzata.

# Gestisci il caso in cui la lista sia vuota, 
# stampando messaggi appropriati e evitando errori di esecuzione.
if not lista_spesa:
    print("La lista è vuota.")  
else:
    print(f"Lista della spesa:")

    stampa_lista_indicizzata(lista_spesa)
    
if not numeri_input:
    print("La lista è vuota.")  
else:
    media_input = media_lista(numeri_input)
    max_input = maximum(numeri_input)
    print(f"La media di {numeri_input} è: {media_input}")
    print(f"Il valore massimo di {numeri_input} è: {max_input}")