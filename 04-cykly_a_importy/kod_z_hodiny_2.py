# for cyklus funguje i pro řetězce
for c in 'Ahoj':
   print(c)

# for cyklus pro seznam
for name in ['Jirka', 'Marie', 'Honza']:
   print(name)

# for cyklus pro tuple
for name in ('Jirka', 'Marie', 'Honza'):
    print(name)

# for cyklus pro slovník iteruje jen přes klíče.
person = {'name': 'Honza', 'age': 20, 'city': 'Zlín'}
for k in person:
   print(person[k])

# for cyklus pro klíč i hodnotu zároveň pomocí funkce items().
# Používá se unpacking (items vrací tuple a ten se rozbalí do dvou proměnných)
for k, v in person.items():
   print(k, '->', v)

# import funkce sleep z balíčku time
from time import sleep

for i in range(5, 10):
    sleep(1)
    print(i)

names = ['Jirka', 'Marie', 'Honza']

# funkce range vrací objekt, který představuje rozsah, len vrací délku pole
for i in range(len(names)):
    print(names[i])

smer = input('Zadejte směr (doleva, doprava...)')
if not smer in ['doleva', 'doprava']:
    print('Chybný směr')
