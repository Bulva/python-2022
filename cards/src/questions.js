const questions = [
    {
        "id": 1,
        "text": "Co je proměnná?",
        "answered": false,
    },
    {
        "id": 2,
        "text": "Vytvoř proměnnou typu float",
        "answered": false,
    },
    {
        "id": 3,
        "text": "Vytvoř proměnnou typu string",
        "answered": false,
    },
    {
        "id": 4,
        "text": "Vytvoř pole a přidej do něj položku pomocí funkce append()",
        "answered": false,
    },
    {
        "id": 5,
        "text": "Jakým číslem začíná číslování indexů?",
        "answered": false,
    },
    {
        "id": 6,
        "text": "Z řetezce 'Ahoj' vyber pomocí indexu znak 'o'",
        "answered": false,
    },
    {
        "id": 7,
        "text": "Z řetězce 'Ahoj' vyber pomocí slicingu znaky 'hoj'",
        "answered": false,
    },
    {
        "id": 8,
        "text": "Jakým indexem lze získat poslední znak v řetězci nebo poslední hodnotu v poli?",
        "answered": false,
    },
    {
        "id": 9,
        "text": "V čem je specifický tuple?",
        "answered": false,
    },
    {
        "id": 10,
        "text": "V čem je specifický set?",
        "answered": false,
    },
    {
        "id": 11,
        "text": "V jaké struktuře ukládá data slovník?",
        "answered": false,
    },
    {
        "id": 12,
        "text": "Vytvoř list, který bude obsahovat hodnotu typu int, float, string",
        "answered": false,
    },
    {
        "id": 13,
        "text": "Vytvoř slovník, který bude obsahovat údaje o osobě (jméno, přijmení, adresu, věk)",
        "answered": false,
    },
    {
        "id": 14,
        "text": "Odstraň duplicity ze seznamu l = ['Jirka', 'Jirka', 'Honza']",
        "answered": false,
    },
    {
        "id": 15,
        "text": "Jak se jmenuje funkce, které přetypuje hodnotu na integer?",
        "answered": false,
    },
    {
        "id": 16,
        "text": "Jak se jmenuje funkce, která přetypuje hodnotu na string?",
        "answered": false,
    },
    {
        "id": 17,
        "text": "Jak se jmenuje funkce, která přetypuje hodnotu na seznam?",
        "answered": false,
    },
    {
        "id": 18,
        "text": "Jak se jmenuje funkce, která přetypuje hodnotu na set?",
        "answered": false,
    },
    {
        "id": 19,
        "text": "Vytvoř seznam a pomocí funkce append() přidej na konec libovolnou hodnotu",
        "answered": false,
    },
    {
        "id": 20,
        "text": "K čemu slouží funkce print?",
        "answered": false,
    },
    {
        "id": 21,
        "text": "Co znamená debugging? A kde se zapíná ve Visual Studiu?",
        "answered": false,
    },
    {
        "id": 22,
        "text": "Co jsou escape sekvence?",
        "answered": false,
    },
    {
        "id": 23,
        "text": "Co dělají escape sekvence \n, \t?",
        "answered": false,
    },
    {
        "id": 24,
        "text": "Jaké uvozovky lze použít při vytváření řetězce?",
        "answered": false,
    },
    {
        "id": 25,
        "text": "Co je parametr funkce?",
        "answered": false,
    },
    {
        "id": 26,
        "text": "Kolik parametrů je možné napsat do funkce print()?",
        "answered": false,
    },
    {
        "id": 27,
        "text": "K čemu slouží funkce len?",
        "answered": false,
    },
    {
        "id": 28,
        "text": "Použij funkci lower",
        "answered": false,
    },
    {
        "id": 29,
        "text": "Jakých hodnot nabývá typ boolean?",
        "answered": false,
    },
    {
        "id": 30,
        "text": "Jakou funkcí zjistím datový typ proměnné?",
        "answered": false,
    },
    {
        "id": 31,
        "text": "Jaké klíčové slovo použiju, když chci vytvořit prázdnou proměnnou?",
        "answered": false,
    },
    {
        "id": 32,
        "text": "Jaké jsou pravidla pro jména proměnných?",
        "answered": false,
    },
    {
        "id": 33,
        "text": "Co děla operátor %?",
        "answered": false,
    },
    {
        "id": 34,
        "text": "Který balíček naimportuju, když chci vygenerovat náhodné číslo?",
        "answered": false,
    },
    {
        "id": 35,
        "text": "Co je pip a pypi.org?",
        "answered": false,
    },
    {
        "id": 36,
        "text": "Jakým příkazem (pomocí pip) nainstaluju nový balíček?",
        "answered": false,
    },
    {
        "id": 37,
        "text": "Jak naimportovat balíček?",
        "answered": false,
    },
    {
        "id": 38,
        "text": "Jak naimportovat funkci z balíčku?",
        "answered": false,
    },
    {
        "id": 39,
        "text": "K čemu slouží podmínky?",
        "answered": false,
    },
    {
        "id": 40,
        "text": "Napiš příklad podmínky if",
        "answered": false,
    },
    {
        "id": 41,
        "text": "Napiš příklad podmínky if včetně else a elif",
        "answered": false,
    },
    {
        "id": 42,
        "text": "Jaká funkce slouží pro přidání do setu?",
        "answered": false,
    },
    {
        "id": 43,
        "text": "Jaká je sekvence vykonání funkcí print(list(set(names)))?",
        "answered": false,
    },
    {
        "id": 44,
        "text": "Jaká funkce slouží pro získání hodnoty od uživatele?",
        "answered": false,
    },
    {
        "id": 45,
        "text": "Jaká je sekvence vykonání funkcí print(list(set(names)))?",
        "answered": false,
    },
    {
        "id": 46,
        "text": "Jak se říká mezikód, do kterého je přeložený python kód napsaný člověkem?",
        "answered": false,
    },
    {
        "id": 47,
        "text": "Jakým způsoben se vybírá ze slovníku?",
        "answered": false,
    },
    {
        "id": 48,
        "text": "Přidej do slovníku nový klíč a hodnotu",
        "answered": false,
    },
    {
        "id": 49,
        "text": "Vytvoř 2D pole",
        "answered": false,
    },
    {
        "id": 50,
        "text": "Napiš while cyklus",
        "answered": false,
    },
    {
        "id": 51,
        "text": "Jakými znaky se v Pythonu definuje blok kódu?",
        "answered": false,
    },
    {
        "id": 52,
        "text": "K čemu slouží blok kódu?",
        "answered": false,
    },
    {
        "id": 53,
        "text": "K čemu slouží ve výraze and?",
        "answered": false,
    },
    {
        "id": 54,
        "text": "K čemu slouží ve výraze or?",
        "answered": false,
    },
    {
        "id": 55,
        "text": "Jak se dá negovat výraz?",
        "answered": false,
    },
    {
        "id": 56,
        "text": "Jaké hodnoty musí nabývat výraz v cyklu while, aby se vykonalo tělo cyklu?",
        "answered": false,
    },
    {
        "id": 57,
        "text": "Co dělá příkaz i += 1 ? ",
        "answered": false,
    },
    {
        "id": 58,
        "text": "Napiš for cyklus",
        "answered": false,
    },
    {
        "id": 59,
        "text": "Jaká funkce slouží k iterování klíče i hodnoty ve slovníku?",
        "answered": false,
    },
    {
        "id": 60,
        "text": "Proiteruj slovník a vypiš klíče",
        "answered": false,
    },
    {
        "id": 61,
        "text": "Proiteruj slovník a vypiš hodnoty",
        "answered": false,
    },
    {
        "id": 62,
        "text": "Proiteruj slovník a vypiš klíče i hodnoty",
        "answered": false,
    },
    {
        "id": 63,
        "text": "K čemu slouží funkce range()?",
        "answered": false,
    },
    {
        "id": 64,
        "text": "K čemu slouží funkce len()?",
        "answered": false,
    },
    {
        "id": 65,
        "text": "Co udělám když něco nebudu vědět?",
        "answered": false,
    },
    {
        "id": 66,
        "text": "K čemu slouží list?",
        "answered": false,
    },
    {
        "id": 67,
        "text": "K čemu slouží set?",
        "answered": false,
    },
    {
        "id": 68,
        "text": "Kdy použít tuple?",
        "answered": false,
    },
    {
        "id": 69,
        "text": "Kterým klíčovým slovem ve výrazu můžu zjistit jestli se hodnota nachází v seznamu?",
        "answered": false,
    },
    {
        "id": 70,
        "text": "",
        "answered": false,
    },
    {
        "id": 71,
        "text": "K čemu slouží operátor = ?",
        "answered": false,
    },
    {
        "id": 72,
        "text": "K čemu slouží operátor == ?",
        "answered": false,
    },
    {
        "id": 73,
        "text": "K čemu slouží operátor != ? ",
        "answered": false,
    },
    {
        "id": 74,
        "text": "Proč je nebezpečné používat float pro porovnání?",
        "answered": false,
    },
    {
        "id": 75,
        "text": "Jak spojit dva řetězce?",
        "answered": false,
    },
    {
        "id": 76,
        "text": "Jak vypsat na standardní výstup více hodnot v jednom příkaze?",
        "answered": false,
    },
    {
        "id": 77,
        "text": "V jaké situaci použiju cyklus?",
        "answered": false,
    },
    {
        "id": 78,
        "text": "Jaký je rozdíl mezi while a for cyklem?",
        "answered": false,
    },
    {
        "id": 79,
        "text": "K čemu je klíčové slovo pass?",
        "answered": false,
    },
    {
        "id": 80,
        "text": "Co jsou klíčová slova v pythonu?",
        "answered": false,
    },
    {
        "id": 81,
        "text": "Podle čeho vznikl název Python?",
        "answered": false,
    },
    {
        "id": 82,
        "text": "Jakou koncovku musí mít soubor spustitelný v Pythonu?",
        "answered": false,
    },
    {
        "id": 83,
        "text": "Jak spustím v cmd interaktivní konzoli?",
        "answered": false,
    },
    {
        "id": 84,
        "text": "Jak spustím python soubor v cmd?",
        "answered": false,
    },
    {
        "id": 85,
        "text": "Jaký datový typ bývá použit jako klíč ve slovnících?",
        "answered": false,
    },
    {
        "id": 86,
        "text": "Co je IDE?",
        "answered": false,
    },
    {
        "id": 87,
        "text": "K čemu slouží příkazový řádek?",
        "answered": false,
    },
    {
        "id": 88,
        "text": "Kolik mezer se používá při vytvoření nového bloku kódu v pythonu?",
        "answered": false,
    }
]

export default questions;