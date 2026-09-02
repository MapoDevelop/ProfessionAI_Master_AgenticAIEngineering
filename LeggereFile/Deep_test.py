""" 
1. Lettura di un file di testo (file.txt):
   - Apri il file "proverbi.txt" in modalità lettura.
   - Leggi tutte le righe del file e memorizzale in una lista.
   - Stampa il numero totale di proverbi presenti (una riga corrisponde a un proverbio).

2. Scrittura su file di testo:
   - Crea o sovrascrivi il file "output_proverbi.txt".
   - Scrivi tutti i proverbi che contengono la parola "a" in maniera case insensitive, uno per riga.

3. Lettura di un file CSV:
   - Apri il file "magazzino.csv" che contiene le colonne: prodotto, quantità, prezzo.
   - Calcola il valore totale in magazzino per ogni prodotto (quantità × prezzo).
   - Stampa a video il prodotto con il valore totale più alto e il relativo valore.

4. Scrittura di un file CSV:
   - Crea un nuovo file "magazzino_valore.csv".
   - Scrivi le colonne: prodotto, valore_totale.
   - Inserisci per ogni prodotto nel file originale la riga corrispondente 
   con il valore totale calcolato.

5. Operazioni su file JSON:
   - Data la struttura di un file "inventory.json" simile a un dizionario Python 
     con chiavi di magazzino e liste di prodotti,leggi il contenuto in un dizionario Python.
   - Aggiungi un nuovo prodotto con dati a scelta alla lista di un magazzino esistente 
     o a un nuovo magazzino.
   - Salva nuovamente il dizionario modificato in un file JSON 
     "inventory_modificato.json" usando una formattazione leggibile (indent).

Durante tutto il programma, utilizza il context manager "with" per l'apertura dei file 
e presta attenzione a codifiche e newline per evitare errori o doppie righe.

Non utilizzare argomenti, funzioni o tecniche non ancora studiate nei moduli precedenti.

Esempi Input/Output

input:
(proverbi.txt contiene 4 righe, ad esempio)
Chi va piano va sano e va lontano.
Meglio un uovo oggi che una gallina domani.
Chi fa da sé fa per tre.
Tutte le cose hanno bisogno del loro tempo.

(magazzino.csv contiene)
prodotto,quantita,prezzo
bicicletta,3,300
casco,10,50
lucchetto,15,20

(inventory.json contiene)
{
    "magazzino1": [
        {"nome": "bicicletta", "quantita": 3},
        {"nome": "casco", "quantita": 10}
    ],
    "magazzino2": [
        {"nome": "lucchetto", "quantita": 15}
    ]
}

output:
Numero totale di proverbi: 4
Prodotto con valore più alto: bicicletta, valore: 900

(output_proverbi.txt contiene i proverbi con la lettera 'a')
Chi va piano va sano e va lontano.
Meglio un uovo oggi che una gallina domani.
Tutte le cose hanno bisogno del loro tempo.

(magazzino_valore.csv contiene)
prodotto,valore_totale
bicicletta,900
casco,500
lucchetto,300

(inventory_modificato.json contiene il JSON aggiornato con il nuovo prodotto aggiunto nel magazzino1 o magazzino2, con indentazione chiara)
"""

# Importo le librerie che mi servono
import os # per impostare la cartella
cartella = os.path.dirname(os.path.abspath(__file__)) # Imposto il percorso della cartella

import csv # per leggere il magazzino
import json # per i dati in json

# Presta attenzione a codifiche e newline per evitare errori o doppie righe.
# Creo la lista proverbi
proverbi = []

# Apro il file "proverbi.txt" in modalità lettura
with open(os.path.join(cartella, "proverbi.txt"), "r", encoding="utf-8") as file:
    proverbi = file.readlines()
    
    proverbi = [proverbio.strip(" \n") for proverbio in proverbi]
    
# Stampa il numero totale di proverbi presenti (lunghezza della lista)
print(f"Ci sono: {len(proverbi)} proverbi")

# Creo il file "output_proverbi.txt"
with open(os.path.join(cartella, "output_proverbi.txt"), "w", encoding="utf-8") as file:
    
    # Filtro i proverbi che contengono la parola "a" (case sensitive)
    for frase in proverbi: # selezioni ogni frase
        parole = frase.split(" ") # divido la frase in parole
        for parola in parole: # seleziono ogni parola
            if parola.lower() == "a": # seleziono quando una parola corisponde ad "a" minuscola (case sensitive)
                file.write(frase + "\n") # scrivo la frase nel file
                print(f'Proverbio filtrato: "{frase}"') # Stampo se la frase è stata inserita
    
# creo le variabili per le statistiche
prodotti = [] # lista dei prodotti su cui lavorare
prodotti_originali = [] # lista dei prodotti originali
prodotti_totale = 0 # numero dei prodotti in magazzino
prodotto_totale_max = {"prodotto" : "", "prezzo": 0}

# creo una funzione che calcoli il totale (prezzo * quantità)
def calcola_totale(prezzo, quantita):
    return prezzo * quantita

# Apro "magazzino.csv"
with open(os.path.join(cartella,  "magazzino.csv"), "r", encoding="utf-8") as file:

    prodotti = list(csv.DictReader(file)) # creo la lista che utilizzerò nel programma
    prodotti_originali = prodotti.copy() # creo una copia dei prodotti
    
    for item in prodotti: # per ogni iterazione
        # Calcolo il valore totale in magazzino (quantità × prezzo)
        prodotti_totale += calcola_totale(float(item['prezzo']), float(item['quantita'])) # sommo il prezzo dell'item
        # Cerco il prodotto con prezzo più alto
        if float(item['prezzo']) > prodotto_totale_max['prezzo']: # se il prezzo del prodotto iterato è maggiore di quello salvato
            # Aggiungo il prodotto e il prezzo al dizionario
            prodotto_totale_max['prodotto'] = item['prodotto'] # definisco il nome         
            prodotto_totale_max['prezzo'] = float(item['prezzo']) # definisco il prezzo

# Stampo il valore del magazzino
print(f'Valore totale del magazzino: {prodotti_totale:.2f}')

# Stampo a video il prodotto con il valore totale più alto e il relativo valore.
print(f'Prodotto più costoso: {prodotto_totale_max["prodotto"]}, valore: {prodotto_totale_max["prezzo"]}')
   
# Scrivo nel file "magazzino_valore.csv"
with open(os.path.join(cartella,  "magazzino_valore.csv"), "w", encoding="utf-8") as file:
    # Aggiungo le colonne "prodotto" e "valore_totale"
    colonne = ['id','prodotto','valore_totale']
    # Gli dico quali sono le colonne
    prodotti_writer = csv.DictWriter(file, fieldnames=colonne)
    # scrivo l'intestazione
    prodotti_writer.writeheader()
    for prodotto in prodotti: # per ogni prodotto
        #Calcolo il valore totale per ogni prodotto
        prodotto['valore_totale'] = calcola_totale(float(prodotto['prezzo']),float(prodotto['quantita']))
        # scrivo la riga nel file
        prodotti_writer.writerow({'id': prodotto['id'], 'prodotto': prodotto['prodotto'], 'valore_totale': prodotto['valore_totale']})

# Aggiungo ad ogni prodotto il totale (prezzo * quantità) nel file originale
# con scrittura di aggiunta e non sovrascrittura
with open(os.path.join(cartella,  "magazzino.csv"), "w", encoding="utf-8", newline='') as file:
    
    # Ricreo il file da prodotti
    # aggiungo le colonne con la nuova 'valore_totale'
    colonne = ['id','taglia','colore','prezzo','prodotto','quantita','valore_totale'] 
    prodotti_writer = csv.DictWriter(file, fieldnames=colonne)
    prodotti_writer.writeheader()
    prodotti_writer.writerows(prodotti_originali) # scrivo tutti i prodotti con il nuovo valore totale
    print(f'File "magazzino.csv" aggiornato con il valore totale per ogni prodotto.')

with open(os.path.join(cartella, "inventory.json"), "r", encoding="utf-8") as file:
    inventory = json.load(file)
    print(inventory)
    
inventory["magazzino2"].append({"nome":"cassaforte","quantita":"5"})
print(inventory)

with open(os.path.join(cartella, "inventory_modificato.json"), "w", encoding="utf-8") as file:
    json.dump(inventory, file, indent=4)
    print("File aggiornato!")