'''
V tomto cviceni si vytvorime jednoduchy system pro ukladani informaci o lidech vcetne jejich polohy.

1. Vytvorte tridu Person, ktera bude mit tyto vlastnosti:
    - id (nahodne generovane cislo)
    - name (str)
    - surname (str)
    - birthdate (str) ve formátu DD.MM.RRRR
    - age (int) - vypocitany z data narozeni
    - location (Location) ve formatu latitude longitude
pokud uzivatel zada hodnotu se spatnym datovym typem, tak vyhodite vyjimku

2. Vytvorte tridu Location, ktera bude obsahovat nasledujici parametry
    - latitude (float)
    - longitude (float)
    - wkt (str) - bude obsahovat geometrii prevedenou na wkt (wkt - https://en.wikipedia.org/wiki/Well-known_text)
    - city

3. ziskejte od uzivatelu hodnoty pomoci input() a vytvorte jednotlive objekty
4. implementujte funkce na vypis informaci o person i location objektech
5. vytvorte funkci, ktera vypocita vek daneho cloveka podle data narozeni
6. vytvorte funkci, ktera vytvori wkt bod z latitude a longitude
7. napiste funkci na zmenu prijmeni urcite osoby
8. zkuste vymyslet zpusob jak zavolat OpenStreetMap API pro ziskani mesta, kde clovek zije
    https://nominatim.openstreetmap.org/

'''


