# Udělejte hru, kde si počítač bude myslet jedno číslo a 
# uživatel bude hádat jaké to číslo je. 
# Počítat bude odpovídat jestli je myšlené číslo větší nebo menší
# Pokud uživatel číslo uhádně, tak ho pochvalte

from random import randint

no_attempts = 0
num = randint(1, 666)
print('Myslím si číslo...')

while True:
    my_num = int(input('Zadej cislo: '))
    no_attempts += 1
    
    if my_num > num:
        print('To je moc')
    elif my_num < num:
        print('To je moc málo')
    elif my_num == num:
        print('Uhádl si')
        break

print('Počet pokusů:', no_attempts)



