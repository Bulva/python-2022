# v tomto ukolu budete simulovat lednici vcetne jejiho obsahu
# lednici bude predstavovat nejdrive prazdne pole (promenna fridge)
fridge = []

# jednotlive potraviny budou reprezentovany slovnikem napr.
# name: predstavuje nazev potraviny
# price: predstavuje cenu
# expired: popisuje jestli je potravina prosla nebo ne
# cheese = {'name': 'blue cheese', 'price': 40, 'expired': True}


def add_food(food):
    """
    Funkce, ktera prida do lednice potravinu (pouze kdyz neni prosla).
    Pri uspesnem naplneni vrati True, pri neuspesnem False.
    :param (dict) food: potravina, kterou budete vkladat
    :return (bool): vraci True, kdyz potravina byla pridana do lednice. Jinak vraci False
    """
    if food['expired'] is False:
        fridge.append(food)
        return True
    return False


def add_foods(*args):
    """
    Funkce prida do lednice vice potravin (pouze kdyz nejsou prosle), ktere budou zadany jako jednotlive parametry funkce
    :param (dicts) args: vice potravin zadanych jako jednotlive parametry
    :return: vrati True pokud se vsechny potraviny podari pridat. Pokud ne, tak vrati False
    """
    for arg in args:
        if arg['expired'] is True:
            return False
    for arg in args:
        fridge.append(arg)
    return True


def eat_food(name):
    """
    Funkce, ktera odstrani z lednice potravinu pokud v ni potravina byla
    :param (str) name: nazev potraviny, kterou budete odebirat
    :return (bool): vraci True, kdyz potravina byla odebrana z lednice. Jinak vraci False
    """
    for food in fridge:
        if food['name'] == name:
            del fridge[fridge.index(food)]
            return True
    return False


def get_price():
    """
    Funkce, ktera vrati sumu cen vsech potravin v lednici
    :return (int): suma cen vsech potravin v lednici
    """
    sum_price = 0
    for food in fridge:
        sum_price += food['price']
    return sum_price


def get_count():
    """
    Funkce vrati pocet vsech potravin v lednici
    :return (int): pocet vsech potravin v lednici. Stejne potraviny nemuzou byt v lednici vickrat
    """
    return len(fridge)


def get_average_price():
    """
    Funkce vrati prumernou cenu vsech potravin v lednici. Pouzijte funkce get_price() a get_count().
    :return (float): vrati prumernou cenu vsech potravin v lednici
    """
    return get_price()/get_count()


def remove_expired():
    """
    Funkce odstrani z lednice vsechny potraviny, ktere jsou prosle. Prosle potraviny funkce vrati. Pokud funkce
    zadne potraviny neodstrani tak funkce vrati prazdny seznam
    :return (list): seznam s proslymi potravinami
    """
    expired_food = []
    for food in fridge:
        if food['expired'] is True:
            expired_food.append(food)

    for food in expired_food:
        fridge.remove(food)
    return expired_food


def set_expired(name):
    """
    Funkce nastavi parametr potraviny expired na True podle jmena potraviny
    :param (str) name: nazev potraviny, ktere nastavi expired na True
    :return (bool): pokud funkce najde potravinu a nastavi ji hodnotu na True nebo jiz True mit bude vraci True.
                    pokud funkce nenajde podle nazvu zadanou potravinu, tak vrati False
    """
    for food in fridge:
        if food['name'] == name:
            food['expired'] = True
            return True
    return False


# Pokud budete chtit testovat jednotlive funkce muzete si je zavolat sami nebo muzete vyuzit volani zakomentovanych funkci nize
# Volani funkci nize neupravujte. Nakonci je odkomentujte (vymazte ''' '''). Podle vypisu poznate spravnost implementace.


# SPRAVNY VYPIS BY MEL VYPADAT TAKTO
# Pridani potraviny blue cheese: False
# Pridani potraviny milk: True
# Pridani vice potravin: True
# Snedl jsem sunku: True
# Snedl jsem hovinko: False
# Celkova cena potravin: 304
# Celkovy pocet potravin: 5
# Prumerna cena potravin: 60.8
# Nastavuji expiraci vajicku: True
# Nastavuji expiraci vinu: True
# Nastavuji expiraci hovinku: False
# Odstranene potraviny: [{'name': 'egg', 'price': 4, 'expired': True}, {'name': 'wine', 'price': 200, 'expired': True}]


print('Pridani potraviny blue cheese:', add_food({'name': 'blue cheese', 'price': 40, 'expired': True}))
print('Pridani potraviny milk:', add_food({'name': 'milk', 'price': 15, 'expired': False}))

print('Pridani vice potravin:', add_foods({'name': 'ham', 'price': 30, 'expired': False},
                                           {'name': 'salad', 'price': 45, 'expired': False},
                                           {'name': 'egg', 'price': 4, 'expired': False},
                                           {'name': 'wine', 'price': 200, 'expired': False},
                                           {'name': 'orange juice', 'price': 40, 'expired': False}))

print('Snedl jsem sunku:', eat_food('ham'))
print('Snedl jsem hovinko:', eat_food('poop'))

print('Celkova cena potravin:', get_price())
print('Celkovy pocet potravin:', get_count())
print('Prumerna cena potravin:', get_average_price())

print('Nastavuji expiraci vajicku:', set_expired('egg'))
print('Nastavuji expiraci vinu:', set_expired('wine'))
print('Nastavuji expiraci hovinku:', set_expired('poop'))

print('Odstranene potraviny:', remove_expired())



