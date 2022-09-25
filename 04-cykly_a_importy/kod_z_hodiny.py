# cyklus while vyhodnocuje výraz. Pokud je výraz True, tak se spustí tělo cyklu
while True:
    x = int(input('Zadej číslo (1-10): '))
    if x >= 1 and x <= 10:
        # break vyskočí z cyklu a ukončí jeho běh
        break

i = 1
while i < 10:
    print(i)
    # přidá do proměnné +1, ekvivalent k i = i + 1
    i += 1
