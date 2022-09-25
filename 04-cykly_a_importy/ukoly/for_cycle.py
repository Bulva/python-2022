# vytvorte pole, kde budou nejake libovolne retezce
# pomoci funkce input() zjistete od uzivatele hodnotu, kterou chce v poli vyhledat
# vyhledejte pomoci cyklu a podminky hodnotu a pokud hodnotu najdete tak ukoncete prochazeni cyklu a hodnotu vypiste na obrazovku

names = ['Jirka', 'Marie', 'Honza']
input_name = input('Zadej jméno: ')

for name in names:
    if name == input_name:
        print('Jméno nalezeno:', name)
        break
