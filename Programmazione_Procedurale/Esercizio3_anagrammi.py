# Definisci una funzione che prendendo in input due parole,
# verifica se sono anagrammi.

# Funizone che verifica se due parole sono anagrammi
def anagrammi(parola1, parola2):
    return sorted(parola1) == sorted(parola2) # ordina le lettere e confronta le parole

# pulisco le parole rimuovendo spazi e convertendo in minuscolo
def pulisci_parola(parola):
    return parola.replace(" ", "").lower()

# Inserisco le parole in input
parola1 = pulisci_parola(input("Inserisci la prima parola: "))
parola2 = pulisci_parola(input("Inserisci la seconda parola: "))

# Chiamo la funzione e stampo il risultato
if anagrammi(parola1, parola2):
    print(f"{parola1} e {parola2} sono anagrammi.")
else:
    print(f"{parola1} e {parola2} non sono anagrammi.")