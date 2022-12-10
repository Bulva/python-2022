'''
V tomto cviceni si vytvorime jednoduchy system pro ukladani informaci o lidech vcetne jejich polohy.

1. Vytvorte tridu Person, ktera bude mit tyto vlastnosti:
    - id (nahodne generovane cislo)
    - name (str)
    - surname (str)
    - birthdate (datetime)
    - age (int) - vypocitany z data narozeni
    - location (Location) ve formatu latitude longitude

2. Vytvorte tridu Location, ktera bude obsahovat nasledujici parametry
    - latitude (float)
    - longitude (float)
    - wkt (str) - bude obsahovat geometrii prevedenou na wkt (wkt - https://en.wikipediawikipedia.org/wiki/Well-known_text)
    - city (str)

3. v ramci testovani funkcnosti si vytvorte objekt Person a objekt Location s hodnotami, které si vymyslíte
4. implementujte funkce na vypis informaci o person i location objektech (__repr__)
5. vytvorte funkci, ktera vypocita vek daneho cloveka podle data narozeni
6. vytvorte funkci, ktera vytvori wkt bod z latitude a longitude
7. zkuste vymyslet zpusob jak zavolat OpenStreetMap API pro ziskani mesta, kde clovek zije
    https://nominatim.openstreetmap.org/
Funkce spravne zaradte do trid.
'''
from datetime import datetime, date
from random import randint


class Person:
    def __init__(self, name, surname, birthdate, location) -> None:
        self.id = randint(1, 9999)
        self.name = name
        self.surname = surname
        self.birthdate = birthdate
        today = date.today()
        self.age = today.year - birthdate.year - \
            ((today.month, today.day) < (birthdate.month, birthdate.day))
        self.location = location

    def __repr__(self) -> str:
        return f'Person -> id: {self.id}, name: {self.name}, surname: {self.surname}, birtdate: {self.birthdate}, age: {self.age}, location: {self.location}'


class Location:
    def __init__(self, latitude, longitude) -> None:
        self.latitude = latitude
        self.longitude = longitude
        self.wkt = ''
        #self.wkt = f'POINT ({self.latitude} {self.longitude})'
        self.city = ''

    def create_wkt(self):
        return f'POINT ({self.latitude} {self.longitude})'

    def __repr__(self) -> str:
        return f'Location -> latitude: {self.latitude}, longitude: {self.longitude}, wkt: {self.wkt}, city: {self.city}'
        #'Location latitude: {0}, longitude: {1}'.format(self.latitude, self.longitude)
        # return  'Location -> latitude: ' + str(self.latitude) + ', longitude: ' + str(self.longitude) + ''


loc = Location(52.5456465, 72.5465465)
p = Person('Petr', 'Silhak', datetime(1993, 7, 5), Location(52.5456465, 72.5465465))
p2 = Person('Jan', 'Horak', datetime(1993, 7, 5), Location(52.5456465, 72.5465465))
print(loc.create_wkt())
print(Location(52.5456465, 72.5465465).create_wkt())
print(p2)
