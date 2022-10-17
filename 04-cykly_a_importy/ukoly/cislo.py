# Udělejte hru, kde si počítač bude myslet jedno číslo a
# uživatel bude hádat jaké to číslo je.
# Pokud uživatel číslo uhádně, tak ho pochvalte

from random import randint

num = randint(1, 6)
# my_num = -999
# while num != my_num:
    # my_num = int(input('Zadej cislo: '))
    # if num == my_num:
    #     print('Uhadl si')
    #     break
    # else:
    #     print('Smula')
while True:
    my_num = int(input('Zadej cislo: '))
    if num == my_num:
        print('Uhadl si')
        break
    else:
        print('Smula')
