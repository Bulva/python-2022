# book example
# book = {
#    'name': 'Programming with Python 3',
#    'pages': 157,
#    'read': True
# }

# = [None, None, None, None, None, None, None, None, None, None]
bookshelf = [None] * 10


def is_free(position):
    """
    Funkce zkontroluje jestli je na zadane pozici volno (tzn. jestli je hodnota False)
    :param (int) position: pozice v seznamu, ve kterem se bude zjistovat obsazenost
    :return (bool): vrati True, kdyz je pozice volna a False, kdyz pozice v knihovne volna neni
    """
    if bookshelf[position] is None:
        return True
    return False
    


def add_book(position, name, pages, read=False):
    """
    Funkce prida knihu do seznamu na zadanou pozici. Zkontrolujte zda je pozice prázdná. Pokud není, tak knihu nepřidávejte.
    :param (int) position: pozice v seznamu, na kterou novou knihu pridate
    :param (str) name: nazev knihy
    :param (int) pages: pocet stran nove knihy
    :param (bool) read: informace jestli je kniha prectena nebo ne
    :return: None
    """
    if is_free(position):
        bookshelf[position] = {
                    'name': name,
                    'pages': pages,
                    'read': read
                    }

def find_book(name):
    """
    Funkce, ktera vyhleda knihu podle nazvu a vrati index, na kterem se hledana kniha nachazi
    :param (str) name: nazev knihy
    :return (int): index na kterem se kniha nachazi, popripade False pokud se tam kniha nenachazi
    """
    for i in range(len(bookshelf)):
        if bookshelf[i] is not None:
            if bookshelf[i]['name'] == name:
                return i



def read_book(name):
    """
    Funkce, ktera nastavi knize hodnotu read na True pokud kniha v knihovne existuje
    :param (str) name: nazev knihy
    :return: None
    """
    pass


def remove_read_books():
    """
    Funkce, ktera nahradi vsechny prectene knihy (knihy s hodnotou read = True) na None (prazdne misto knihovny)
    :return: None
    """
    pass


def names_of_books():
    """
    Funkce vraci seznam se jmeny vsech knih v knihovne
    :return (list): seznam se jmeny vsech knih v knihovne
    """
    pass

def average_number_of_pages():
    """
    Funkce vraci prumerny pocet stran knih v knihovne
    :return (int): prumerny pocet stran v knihovne
    """
    pass

# testing
# add_book(0, 'A Byte of python', 120, read=True)
# add_book(1, 'Automate the boring stuff with Python', 420)
# add_book(2, 'Python for Informatics', 500, read=True)
# add_book(3, 'Learning Geospatial Analysis with Python', 155)
# add_book(4, 'Python Geospatial Development', 211)
# add_book(5, 'Python for Data Analysis', 362, read=True)
# add_book(5, 'Programming Java', 874)

# print(is_free(5))  # False
# print(is_free(6))  # True

print(find_book('A Byte of python'))  # 0
print(find_book('Python Geospatial Development'))  # 4
print(find_book('Programming Java'))  # False

# read_book('A Byte of python')
# read_book('Automate the boring stuff with Python')
# read_book('Programming Java')

# remove_read_books()
# print(is_free(1))  # True
# print(is_free(3))  # False

# print(names_of_books()) # ['Learning Geospatial Analysis with Python', 'Python Geospatial Development']

# print(average_number_of_pages())  # 183


# HINT
# print(bookshelf)
# [None, None, None, {'pages': 155, 'name': 'Learning Geospatial Analysis with Python', 'read': False}, {'pages': 211, 'name': 'Python Geospatial Development', 'read': False}, None, None, None, None, None]
