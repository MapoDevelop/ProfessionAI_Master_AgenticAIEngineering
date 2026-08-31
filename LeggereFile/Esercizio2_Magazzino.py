"""
Dal file  shirts.csv calcola:
 -  il numero totale dei prodotti
 - il valore totale del magazzino (somma del prezzo di tutti i prodotti)
 - prezzo medio
 - numero di prodotti per colore
 - numero di prodotti per taglia

 Salva le statistiche in un file JSON shirts_stats.json
"""

import csv
import json
import os  # importo os per mettere il file dove voglio e non sulla cartella iniziale


def prezzo_medio(prodotti_count, prodotti_total_price):
    return prodotti_total_price / prodotti_count if prodotti_count else 0.0


def calcola_statistiche(percorso_csv):
    prodotti_count = 0
    prodotti_total_price = 0.0
    lab_colore = {}
    lab_taglia = {}

    with open(percorso_csv, "r", encoding="utf-8") as file:
        for prodotto in csv.DictReader(file):
            prodotti_count += 1
            prodotti_total_price += float(prodotto['prezzo'])
            colore = prodotto['colore']
            lab_colore[colore] = lab_colore.get(colore, 0) + 1
            taglia = prodotto['taglia']
            lab_taglia[taglia] = lab_taglia.get(taglia, 0) + 1

    return {
        "prodotti_count": prodotti_count,
        "prodotti_total_price": round(prodotti_total_price, 2),
        "prezzo_medio": round(prezzo_medio(prodotti_count, prodotti_total_price), 2),
        "lab_colore": lab_colore,
        "lab_taglia": lab_taglia
    }


def salva_statistiche(statistiche, percorso_json):
    with open(percorso_json, "w", encoding="utf-8") as newfile:
        json.dump(statistiche, newfile, indent=4)


def main():
    cartella = os.path.dirname(os.path.abspath(__file__))
    statistiche = calcola_statistiche(os.path.join(cartella, "shirts.csv"))
    salva_statistiche(statistiche, os.path.join(cartella, "shirts_stats.json"))
    print(statistiche)


if __name__ == "__main__":
    main()
