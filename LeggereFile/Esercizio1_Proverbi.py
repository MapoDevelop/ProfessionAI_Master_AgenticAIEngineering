""" 
Leggi il contenuto di proverbi.txt
Scrivi un nuovo file chiamato proverbi_filtrati.txt
con solo i proverbi che iniziano con vocale
o sono più brevi di 25 caratteri.
"""
import os

# Imposto il percorso della cartella
cartella = os.path.dirname(os.path.abspath(__file__))

# Apro il file proverbi.txt - solo lettura
# il file è nella stessa cartella di questo script
with open(os.path.join(cartella, "proverbi.txt"), "r", encoding="utf-8") as file:
    proverbi = file.readlines()
    
# Apro il file proverbi_filtrati.txt - scrittura
with open(os.path.join(cartella, "proverbi_filtrati.txt"), "w", encoding="utf-8") as file:
    # Filtraggio dei proverbi
    for frase in proverbi:
        if frase[0].lower() in "aeiou" or len(frase) < 25:
            file.write(frase)