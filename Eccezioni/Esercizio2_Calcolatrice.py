""" 
Definisci una funzione per eseguire dei semplici calcoli, 
la funzione prende in ingresso due valori numerici 
ed una stringa contenente un'operazione aritmetica (+, -, *, /) 
ed esegue tale operazione tra i due numeri. 
Acquisisci in input i parametri della funzione

1- utilizza il try/except per gestire l'eccezione che si causa 
nel caso in cui viene inserito un valore non numerico.
2- utilizza l'assert per assicurarti che l'operatore aritmetico sia valido, 
cioè sia un carattere tra +,-,*,/.
3- utilizza il try/except per gestire il caso di divisioni per 0, 
in tal caso stampa semplicemente un messaggio 'Non puoi dividere per 0'.

"""

# Funzione per eseguire operazioni (+, -, *, /)
def calcolatrice(n1, n2, operazione):
    """ Calcolatrice - input di due numeri e stringa dell'operazione """
    if operazione == "+":
        return n1 + n2
    if operazione == "-":
        return n1 - n2
    if operazione == "*":
        return n1 * n2
    if operazione == "/":
        return n1 / n2
    

while True:
    try:
        # Prendo l'input di due numeri e una stringa
        input_values = input("Inserisci un numero, l'operazione da calcolare (+, -, *, /) e un secondo numero: ").split()

        if len(input_values) != 3:
            raise ValueError("Errore sul numero di input: sono richiesti esattamente due valori e un'operazione.")

        try:
            # Converto in interi
            n1 = int(input_values[0])
            n2 = int(input_values[2])
        except ValueError:
            # Se i valori non si possono convertire in interi 
            # creo l'eccezione con messaggio personalizzato
            raise ValueError("Errore: Valore inserito non è un numero intero valido.")

        operazione = input_values[1]
        assert operazione == "+" or operazione == "-" or operazione == "*" or operazione == "/", "L'operazione deve essere scelta tra questi simboli: +, -, *, /"

        risultato = calcolatrice(n1, n2, operazione)
        print(f"Risultato dell'operazione: {risultato}")
        break # Esco dal ciclo se tutto OK

    except ValueError as e:
        print(e)

    except AssertionError as e:
        print(e)

    except ZeroDivisionError:
        print("Non puoi dividere per zero!")
        
