# Teoretické otázky. Odpověď vepište rovnou do komentáře zde do souboru
# 1. Jakým indexem začíná číslování položek v listu? (1 bod)
#
# 2. Co je v Pythonu bytecode? (1 bod)
#
# 3. Co znamená ve funkci parametr *args? (1 bod)
#

# Vaším úkolem je simulovat e-shop. Jako prodejce máte velmi malý e-shop s velmi malou nabídkou. Zaměřujete se na prodej deskových her.
# Váš sklad reprezentuje list, který bude obsahovat jednotlivé hry. Ty jsou reprezentovány vždy slovníkem. Jeden slovník představuje danou hru, ale
# nepředstavuje konkrétní hru. Slovník v sobě obsahuje počet her na skladě

# proměnná představuje eshop
eshop = []

# proměnná která představuje bankovní konto vašeho eshopu
my_money = 150000

# na začátku vás eshop obsahuje pouze tyto dvě hry
successors = {
    'name': 'Successors',
    'publisher': 'Fox in the box',
    'quantity': 5,
    'categories': ['válečná', 'historická', 'pro náročné', 'konfliktní'],
    'price': 2600
}

wingspan = {
    'name': 'Wingspan',
    'publisher': 'Mindok',
    'quantity': 55,
    'categories': ['rodinná', 'příroda'],
    'price': 1500
}

eshop.append(successors)
eshop.append(wingspan)


# Doplňte funkce podle popisu
# 2 body
def sell_game(name, money):
    """
    Funkce, ktera prodá hru (sníží quantity o 1 a zvyší my_money o price) na základě názvu
    :param (str) name: nazev hry
    :param (float) money: účet eshopu
    :return (float): vrací hodnotu účtu do proměnné my_money
    """
    for game in eshop:
        if name == game['name']:
            game['quantity'] = game['quantity'] - 1
            return money + game['price']


# 2 body
def add_game(name, publisher, quantity, categories, price):
    """
    Funkce, ktera přidá hru. Na vstupu jsou parametry hry
    :param (str) name: název hry
    :param (str) publisher: název vydavatele
    :param (int) quantity: počet koupených her
    :param (list) category: kategorie, do kterých hry spadá
    :param (int) price: cena hry
    """
    eshop.append({'name': name, 'publisher': publisher,
                 'quantity': quantity, 'categories': categories, 'price': price})


# 3 body
def find_game_by_category(category):
    """
    Funkce, ktera vyhledá hru na základě kategorie
    :param (str) category: řetězec z klíče category
    :return (list): vrátí list s hrami, které spadají do dané kategorie. Pokud žádna hra nesplňuje podmínku, tak vrátí prázdný list
    """
    games = []
    for game in eshop:
        if category in game['categories']:
            games.append(game)
    return games


# 3 body
def get_most_expensive():
    """
    Funkce, která vrátí nejdražší hru v eshopu
    :return (dict): nejdražší hra v eshopu. Pokud stojí více her stejně, tak vraťte jednu z her
    """
    most = None
    for game in eshop:
        if most is None or most['price'] < game['price']:
            most = game
    return most


# 3 body
def avg_price():
    """
    Funkce, která vrátí pruměrnou cenu her v eshopu
    :return (float): průměrná cena her v eshopu zaokrouhlená na 2 destinná místa
    """
    price = 0
    for game in eshop:
        price += game['price']
    return round(price/len(eshop), 2)


# 4 body
def recommend_game(category=None, max_price=None, fav_publisher=None):
    """
    Funkce, která doporučí hru na základě kategorie, maximální ceny, kterou chce zákazník zaplatit nebo oblíbené vydavatele
    Všechny parametry funkce nemusí nutně obsahovat hodnotu. Některé uživatel nemusí zadat. Pokud jsou všechny parametry None, tak vyhoďte výjimku ValueError s nějakou vaší hláškou.
    Pokud je vyplňen parametr category, tak se pokuste najít hru s danou hodnotou category. Pokud taková hra existuje, tak zkuste nalézt z toho výběru hry, které stojí <= než max_price
    Pokud takové hry existují, tak zkuste vybrat hry i podle vydavatele. Pokud některá z hodnot je None, tak ji vynechejte a filtrujte jen podle vyplněných hodnot
    :param (str) category: řetězec z klíče category
    :param (int) max_price: maximální cena, kterou je zákazník ochotný zaplatit
    :param (str) fav_publisher: oblíbeny vydavatel her
    :return (list): doporučené hry. Pokud žádné doporučené hry nejsou, tak vraťte prádzný list
    """
    if category is None and max_price is None and fav_publisher is None:
        raise ValueError('Prázdné hodnoty')

    games = []
    for game in eshop:
        filt = []
        if category is not None:
            filt.append(category in game['categories'])
        if max_price is not None:
            filt.append(max_price >= game['price'])
        if fav_publisher is not None:
            filt.append(fav_publisher == game['publisher'])
        if False not in filt:
            games.append(game)
    return games


# Ukázky volání funkcí
print('Moje peníze před prodejem:', my_money)
my_money = sell_game('Successors', my_money)
print('Moje peníze po prodeji:', my_money)
print('Můj eshop po prodeji: ')
print(eshop)
print('\n')

add_game('Root', 'Fox in the box', 10, ['konfliktní', 'asymetrická'], 1500)
print('Můj eshop po přidání hry: ')
print(eshop)
print('\n')

print('Hra podle kategorie: ')
print(find_game_by_category('konfliktní'))
print('\n')

print('Nejdražší hra: ')
print(get_most_expensive())
print('\n')

print('Průměrná cena her: ')
print(avg_price())
print('\n')

print('Doporučená hra: ')
print(recommend_game('příroda',2000,'Mindok'))
print(recommend_game('konfliktní',2000,None))
print(recommend_game('příroda',None,'Mindok'))
print(recommend_game(None,2000,'Mindok'))
print(recommend_game('konfliktní',None, None))
print(recommend_game(None, None, 'Mindok'))
print(recommend_game(None,2000,None))
print(recommend_game(None,None,None))

