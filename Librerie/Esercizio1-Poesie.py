"""
Leggi tutte le poesie dalla directory poesie e savale all'interno di un unico file 
chiamato *raccolta_poesie.txt che si dovrà trovare all'interno di una nuova directory 
chiamata raccolta. Prima di una poesia inserisci un contatore (es. POESIA 1).
"""

from os import listdir, makedirs, path
cartella = path.dirname(path.abspath(__file__)) + "\\" # Imposto il percorso della cartella

# creazione delle costanti per i percorsi dei file
PATH = cartella + "poesie\\" # percorso principale
NEW_DIR = PATH +"raccolta\\" # percorso della nuova cartella
NEW_FILE = NEW_DIR + "raccolta_poesie.txt" # percorso del nuovo file

# Creo la cartella
makedirs(NEW_DIR, exist_ok=True) 

# faccio la lista dei file nella cartella poesie
poesie_files = listdir(PATH)

counter = 1 # contatore per le poesie

try:
# ciclo i file
    for file in poesie_files:
        # controllo che sia un file di testo
        if file.endswith(".txt"):
            # apro il file in lettura
            with open(PATH + file, "r", encoding="utf-8") as content_file:
                # leggo il contenuto del file
                content = content_file.read()
                # apro il nuovo file in scrittura (append)
                with open(NEW_FILE, "a", encoding="utf-8") as new_file:
                    # scrivo il contatore
                    new_file.write(f"POESIA {counter}\n")
                    # scrivo il contenuto della poesia
                    new_file.write(content + "\n\n")
                    counter += 1 # incremento il contatore
        else:
            print(f"Il file {file} non è un file di testo e verrà ignorato.")
            continue
except Exception as e:
    print(f"Si è verificato un errore: {e}")
finally:
    print(f"Tutte le poesie sono state salvate in {NEW_FILE}")