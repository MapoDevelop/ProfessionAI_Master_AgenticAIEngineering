"""Quanto manca al mio compleanno?"""

from datetime import datetime

now = datetime.now()
birthday = datetime.strptime(input("Quando cade il tio compleanno? "), "%d - %m")
birthday = birthday.replace(year=now.year)

# funzione per calcolare quanto manca al compleanno
def to_birthday(birthday, now):
    if now > birthday:
        birthday = birthday.replace(year=now.year + 1)
    return birthday-now
    
print(f"Ti mancano {to_birthday(birthday, now).days} giorni al compleanno!")