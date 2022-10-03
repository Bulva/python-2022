# Naprogramujte kalkulačku, která se při spuštění uživatele zeptá na dvě čísla
# Poté se uživatele zeptá na to, kterou početní operaci chce použít (sčítání, odčítání, dělení, násobení)
# Vypočítejte výsledek a vypište ho uživateli
# Pokud uživatel zadá při dělení 0 tak ho upozorněte na chybu (vyzkoušejte jakou chybu vyvolá dělení 0)

no1 = float(input('Zadejte číslo 1: '))
no2 = float(input('Zadejte číslo 2: '))

operation = input('Zadejte operaci \(+, -, /, *\): ')

if operation == '+':
    print('Výsledek: {0}'.format(no1 + no2))
elif operation == '-':
    print('Výsledek: {0}'.format(no1 - no2))
elif operation == '/':
    if no2 == 0:
        print('Nelze dělit nulou')
    else:
        print('Výsledek: {0}'.format(no1 / no2))
elif operation == '*':
    print('Výsledek: {0}'.format(no1 * no2))
else:
    print('Neznámá operace')

