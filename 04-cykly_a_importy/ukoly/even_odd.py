# vytvorte si pole alespon s 5 cisly typu integer
# vytvore cyklus, ktery bude prochazet polem a pomoci podminek bude zjistovat
# jestli je cislo sude nebo liche. Pokud bude sude,
# tak pricte 1 do promenne, ktera bude uchovavat pocet sudych hodnot a
# naopak pro licha cisla.
# Nakonec vypiste pocty lichych a sudych cisel v poli

ls = [1, 2, 4, 5, 92, 347]
suda = 0
licha = 0

for number in ls:
    if number % 2 == 0:
        suda = suda + 1  # suda += 1
    else:
        licha = licha + 1
print('Pocet sudych: ', suda, 'Pocet lichych: ', licha)
