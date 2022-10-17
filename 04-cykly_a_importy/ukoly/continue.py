# V cyklu vypiste vsechny cisla od 0 do 10, krome 4, 5 a 9.
# Pro vylouceni techto cisel pouzijte klicove slovo
# continue (zkuste vygooglit jak funguje).
for i in range(11):
    # i == 4 or i == 5 or i == 9: 
    if i in [4, 5, 9]:
        continue
    print(i)
