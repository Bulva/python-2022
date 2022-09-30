# Program se vykonává odshora dolů, zleva doprava a v případě zanoření funkcí zevnitř ven
# Data v rámci programu se ukládají do proměnných, které představují místo v paměti (RAM), které je alokované pro určitý datový typ
# Proměnná má vždy nějaký název, který se nachází na levé části definice. Je nutné dodržet předepsané pravidla pro názvy proměnných (viz prezentace)
# Po názvu proměnné následuje operátor přiřazení = a hodnota (literál - neměnná hodnota)
var1 = 100

# proměnnou je možné v rámci běhu programu změnit
var1 = 200

# je možné zapsat i hodnotu jiného datového typu
var1 = 'Honza'

# Datový typ integer (zkratka int), představuje záporné nebo kladné celé číslo
my_var = 1234

# Datový typ float, představuje číslo s desetinnou částí
my_var = 1.234

# Datový typ boolean (zkratka bool), nabývá jen hodnota pravda nebo nepravda
is_True = True
liar = False

# Pro boolean je možné nahradit použitím integeru, který nabývá hodnot 0 nebo 1
1 == True   # vrací True
0 == False  # vrací True

# Pro porovnávání hodnot je možné použít další operátory
# == rovná se
# < menší než
# > větší než
# <= menší nebo rovno než
# >= větší nebo rovno než
# != nerovná se
# Výsledek porovnání hodnot vrací vždy datový typ boolean
5 < 10  # vrátí True

# Volání funkcí v Pythonu
# Každé volání funkce musí obsahovat název funkce a parametry uvnitř závorek. Funkce print může mít 1..n parametrů
# význam funkcí a parametry je potřeba najít na internetu nebo pomocí VSCode
print('Ahoj Honzo')

# Některé funkce vrací také hodnotu, např. funkce len vrací délku listu (v tomto případě řetězce)
# vrátí hodnotu 5 a uloží jí do proměnné len_of_str. Nevypíše ji na výstup.
len_of_str = len('Honza')

# Funkce lze v Pythonu volat dvěma způsoby. Každá funkce je volatelná určitým způsobem
# 1. volání funkce pouze jejím názvem, např. funkce print, len, type...
# 2. volání funkce pomocí tečkové notace na datovém typu nebo objektu, lowercase...
# v tomto případě funkce nemá parametr, ale řetězec se bere rovnou z objektu v proměnné před tečkou
s = 'HONZA'
print(s.lower())     # vypíše honza

# Funkce lze do sebe zanořovat, pak se vykonávají odprostředku. U funkce na řádku 50 se nejdřív vykoná s.lowercase() a hodnota z této funkce se použije do printu
# Alternativně lze zapsat i takto:
s = 'HONZA'
s_lower = s.lower()
print(s_lower)

# Zjištění datového typu lze provést pomocí funkce type
type(10)    # vrátí <class int>
type(s)     # vrátí <class str>

# Přetypování datových typů je možné pomocí funkcí str(), int(), bool(), float()
# Vždy se daný typ přetypuje na typ, který je v názvu funkce. Řetězec musí být vždy obalen v jednoduchých nebo dvojitých uvozovkách
int('10')   # vrátí 10

# funkce input počká než uživatel zadá nějaký vstup do konzole. Poté tento vstup předá proměnné. Jako parametr může obsahovat text, který se uživateli zobrazí
s = input('Zadejte řetězec: ')
print(s)    # vypíše řetězec zadaný uživatelem

# Datový typ z funkce input je vždy řetězec. Pokud chceme následně počítat, tak je nutné přetypovat
my_number = float(input('Zadejte číslo: '))

# U řetězců je také možné použít indexing a slicing. Indexing a slicing je možné udělat pomocí hranatých závorek přímo za řetězcem, případně proměnnou
# Každý znak v řetěci (i včetně mezer) je očíslován od 0 do n
# 0123456789
# Ahoj Honzo
s = 'Ahoj Honzo'
print(s[0])     # vrátí A
print(s[-1])    # vrátí o
print(s[1:5])   # vrátí hoj
print(s[-5:])   # vrátí Honzo

# Dva způsoby vyřešení úkolu č. 3
# escape sekvence v řetězci reprezentují znaky, které není možné jinak do řětezce dostat. Uvozují se zpětným lomítkem
print('\'Beautiful is better than ugly.\'\n \"Explicit is better than implicit.\"\n \\Simple is better than complex.\\\n \tComplex is better than complicated.')

# trojité uvozovky vytvoří víceřádkový řetězec
print('''\'Beautiful is better than ugly.\'
\"Explicit is better than implicit.\"
\\Simple is better than complex.\\
\tComplex is better than complicated.
''')
