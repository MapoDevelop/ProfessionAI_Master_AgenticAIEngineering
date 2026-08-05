# Uso regex per controllare la struttura della mail

import re

# EMAIL_REGEX = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$" # Questo è il classico regex
EMAIL_REGEX = r"^[a-zA-Z0-9_-]+@[a-zA-Z0-9]+\.[a-zA-Z0-9]{1,3}$" # Questo è un regex come da esercizio per farci ipazzire

# Definisci una funzione per validare un indirizzo email

def is_valid_email(email):
    return re.match(EMAIL_REGEX, email) is not None

print(is_valid_email("nome@mail.it"))