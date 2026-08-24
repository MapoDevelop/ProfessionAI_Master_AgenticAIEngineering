""" 
In questo esercizio dovrai realizzare un programma in Python 
che riceve da tastiera due numeri, li converte in interi e ne calcola 
la divisione. Il programma deve gestire in modo corretto e robusto 
le diverse eccezioni che possono verificarsi durante la conversione dei dati e il calcolo. 
In particolare, devi implementare:

1. Lettura di una singola riga di input con due valori separati da spazio.
2. Conversione dei valori in interi, gestendo il caso in cui uno o entrambi 
non siano numeri validi (ValueError).
3. Verifica esplicita che siano inseriti esattamente due valori, 
altrimenti solleva un'eccezione con un messaggio personalizzato.
4. Calcolo della divisione del primo numero per il secondo, 
gestendo la divisione per zero (ZeroDivisionError).
5. Uso del blocco try-except per catturare le eccezioni specifiche e 
fornire messaggi chiari all'utente.
6. Implementazione di un blocco finally che stampa sempre un messaggio di chiusura, 
a prescindere da errori o meno.

Extra: Utilizza la keyword raise per sollevare eccezioni personalizzate nel caso 
di input di lunghezza sbagliata, con un messaggio esplicativo. 
Infine, prova ad usare assert per verificare che i valori convertiti siano positivi 
e gestisci l'eventuale AssertionError con un messaggio all'utente.

Non è richiesto usare file, moduli esterni o funzionalità non ancora studiate. 
Concentrati sull'uso di try-except-finally, raise, assert, la gestione dei messaggi 
di eccezione e la corretta indentazione per i blocchi di codice. Il programma 
deve essere robusto e non deve terminare con un crash se l'utente commette 
un errore di input.

*** Esempi Input/Output
input:
10 2
output:
Risultato della divisione: 5.0
Esecuzione terminata.

input:
ten 2
output:
Errore: Valore inserito non è un numero intero valido.
Esecuzione terminata.

input:
10 0
output:
Errore: Impossibile dividere per zero.
Esecuzione terminata.

input:
10
output:
Errore sul numero di input: sono richiesti esattamente due valori.
Esecuzione terminata.

input:
-5 3
output:
Errore: I numeri devono essere positivi.
Esecuzione terminata.
"""

# Con un programma calcolo la divisione
def divisione(n1, n2):
    return n1 / n2

def main():
    try:
        # Ricevo da tastiera due numeri separati da spazio
        numeri = input("Inserisci due numeri separati dallo spazio: ").split(" ")
        
        # Controllo se siano stati inseriti esattamente due valori
        if len(numeri) != 2:
            # Se non ci sono due valori creo l'eccezione con messaggio personalizzato
            raise ValueError("Errore sul numero di input: sono richiesti esattamente due valori.")
        
        try:
        # Converto in interi
            n1 = int(numeri[0])
            n2 = int(numeri[1])
        except ValueError:
            # Se i valori non si possono convertire in interi 
            # creo l'eccezione con messaggio personalizzato
            raise ValueError("Errore: Valore inserito non è un numero intero valido.")
        
        # Controllo che i valori siano positivi
        assert n1 > 0 and n2 > 0, "Errore: I numeri devono essere positivi."
        
        # Stampo il risultato
        print(f"Risultato della divisione: {divisione(n1, n2)}")
    
    # Gestisco il ValueError con messaggi personalizzati che mi arrivano da raise
    except ValueError as e:
        print(e)
    
    # Controllo se l'operazione è divisa per zero
    except ZeroDivisionError:
        print("Errore: Impossibile dividere per zero.")
        
    # Stampo il messaggio di errore dell'assert 
    # in questo caso controllo che i numeri siano positivi
    except AssertionError as e:
        print(e)
        
    # Alla fine stampo che il programma ha concluso
    finally:
        print("Esecuzione terminata.")
    
# Faccio partire il main   
main()