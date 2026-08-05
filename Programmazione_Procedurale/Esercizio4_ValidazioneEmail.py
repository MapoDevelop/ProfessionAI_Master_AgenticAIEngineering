# Uso regex per controllare la struttura della mail

import re

# EMAIL_REGEX = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$" # Questo è il classico regex
EMAIL_REGEX = r"^[a-zA-Z0-9_-]+@[a-zA-Z0-9]+\.[a-zA-Z0-9]{1,3}$" # Questo è un regex come da esercizio per farci ipazzire

# Definisci una funzione per validare un indirizzo email

def is_valid_email(email):
    return re.match(EMAIL_REGEX, email) is not None

# Definisci una funzione per filtrare una lista di email valide
def filter_valid_emails(email_list):
    return [email for email in email_list if is_valid_email(email)]

email_list = [
    "nome@ciao.it",
    "ciao@mondo.com",
    "email@dominio.org"
]

valid_emails = filter_valid_emails(email_list)
print(valid_emails)