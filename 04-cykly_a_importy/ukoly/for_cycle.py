# vytvorte list, kde budou nejake libovolne retezce
# pomoci funkce input() zjistete ¨
# od uzivatele hodnotu, kterou chce v listu vyhledat
# vyhledejte pomoci cyklu a podminky hodnotu a 
# pokud hodnotu najdete tak ukoncete prochazeni cyklu a 
# hodnotu vypiste na obrazovku

ls = ['Hana', 'Monika', 'Jirka']
input_name = input('Zadej jmeno: ')
for name in ls:
    if name == input_name:
        print('Našel jsem jméno')
        break

# if input_name in ls:
#     print('Našel jsem jméno')


