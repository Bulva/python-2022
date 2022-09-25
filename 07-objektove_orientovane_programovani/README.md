## Objektově orientované programování (OOP)
Objektové orientované programování má celou řadu výhod oproti klasickému deklarativnímu paradigmatu. Pro větší projekty umožňuje znovupoužitelnost kódu, zaručuje větší modularitu a přehlednost kódu a při správném použití dokáže zjednodušit celý návrh.
Výhody OOP:
 * rychlejší a levnější vývoj větších aplikací
 * lepší udržitelnost kódu

Nevýhody OOP:
 * lehce komplikovaný pro začátečníky
 * výpočetně může být tento přístup o něco málo pomalejší

OOP je v Pythonu implementováno velice podobně jako v jiných jazycích, takže pokud se naučíme obecně základy OOP dokážeme psát velice podobný kód v jiných jazycích (alespoň v návrhu)

Základním stavebním kamenem OOP je **třída** (class). Třída představuje jakýsi recept pro vytvoření objektu. Pokud chceme například vytvořit aplikaci pro správu vozového parku ve firmě zcela jistě budeme potřebovat třídu, která bude představovat auto. Třída bude říkat jak vytvořit objekt auto. Musí říkat například jaký má auto výkon motoru, jakou ma SPZ, rok výroby daného automobilu apod. Těmto informacím se říká **vlastnosti** (property) dané třídy nebo objektu. Návrh těchto vlastností by měl vycházet z návrhu, tzn. že vytvoříme jen vlastnosti, které budeme potřebovat.

```python
# vytvoreni takove tridy muze vypadat takto
# definice tridy

class Car:
    pass
```
Taková definice třídy nemá žádné vlastnosti a je nám vlastně k ničemu. Pokud chceme rovnou definovat i vlastnosti dané třídy musíme vytvořit **konstruktor**. Konstruktor je funkce, která vytvoří daný objekt. Na základě definice vlastností vytvoří auto s určitými vlastnostmi. V kódu potom tento konstruktor zavoláme s danými parametry. V Pythonu se konstruktor jmenuje `__init__(self)`. Podtržítka říkají, že tato funkce patří do základních funkcí implementovaných v Pythonu a parametr self představuje samotný objekt, který vytváříme, konkrétní auto.

```python
# definice třídy včetně vlastností

class Car:

    # konstruktor kde budeme chtit nastavit vlastnosti objektu
    # vlastnosti predavame jako parametry funkce
    def __init__(self, spz, brand, color, engine):
        self.spz = spz
        self.brand = brand
        self.color = color
        self.engine = engine
```

Parametr **self** zde představuje konkrétní objekt vytvořený pomocí třídy Car. Při vstupní parametr self je prázdný, ale my do něj v konstruktoru přidáme vlastnosti, které jsme si poslali jako parametry do konstruktoru. Přístup k vlastnostem třídy (objektu) se dostaneme pomocí tečkové notace, `self.spz` vypíše SPZ auta, které vytváříme.

Když pak budeme chtít rovnou vytvořit objekty (konkrétní automobily) bude to vypadat nějak takhle. Konstrukro voláme názvem celé třídy.
```python
class Car:

    def __init__(self, spz, brand, color, engine):
        self.spz = spz
        self.brand = brand
        self.color = color
        self.engine = engine


# vytvorime dva objekty (instance tridy)
fabia = Car('6AD 7222', 'Škoda', 'blue', '1.2 TSI')
prius = Car('7AS 7345', 'Toyota', 'white', '1.4')

# nyni mame ve dvou promennych dva automobily s ruznymi parametry vytvorene podle stejne sablony (tridy)
# pokud budeme chtit vypsat nektere parametry daneho automobilu pouzijeme teckovou notaci
print(fabia.spz) # vypise 6AD 7222
```

Nyní si přidáme do třídy další vlastnost, informaci o majiteli. Rozhodli jsme se, že umožníme v aplikaci fleetové auto dát auto konkrétnímu zaměstnanci ve firmě. Tzn. vytvoříme funkci, která přepíše auto na nového majitele. Metody, které napíšeme dovnitř třídy se vztahují pouze ke konkrétní třídě a můžeme je volat jen na instance dané třídy.
```python
class Car:

    def __init__(self, spz, brand, color, engine, owner):
        self.spz = spz
        self.brand = brand
        self.color = color
        self.engine = engine
        self.owner = owner

    def change_owner(self, new_owner):
        self.owner = new_owner


fabia = Car('6AD 7222', 'Škoda', 'blue', '1.2 TSI', 'Asseco')
prius = Car('7AS 7345', 'Toyota', 'white', '1.4', 'Asseco')
print(fabia.owner) # vypise Asseco

# ted se rozhodneme, ze firma mi da sluzebni auto
fabia.change_owner('Petr')
print(fabia.owner) # vypise Petr

print(fabia) # vypise treba <__main__.Car object at 0x7f2a108fcb00>
```
Změnili jsme vlastníka pouze u jednoho auta. A to u fábie. Prius má furt stejné hodnoty. Klíčové slovo **self** ve funkci `change_owner()` představuje konkrétní objekt, v našem případě fábii. Funkce se tedy volají přes tečkovou notaci na konkrétní objekt `fabia.change_owner(parametr)`.

Pokud bychom si vypsali vytvořený objekt dostaneme výpis o umístění v paměti. Tento výpis není moc praktický a proto se dá změnit přepsáním funkce `__str__(self)`.
```python
class Car:

    def __init__(self, spz, brand, color, engine, owner):
        self.spz = spz
        self.brand = brand
        self.color = color
        self.engine = engine
        self.owner = owner

    def change_owner(self, new_owner):
        self.owner = new_owner

    def __str__(self):
        return 'SPZ auta: {} a jeho vlastník: {}'.format(self.spz, self.owner)


fabia1 = Car('6AD 7222', 'Škoda', 'blue', '1.2 TSI', 'Asseco')
fabia2 = Car('6AD 7222', 'Škoda', 'blue', '1.2 TSI', 'Asseco')
prius = Car('7AS 7345', 'Toyota', 'white', '1.4', 'Asseco')

print(fabia)
# vypise SPZ auta: 6AD 7222 a jeho vlastník: Asseco

print(fabia1 == fabia2) # vypise False - neporovnava hodnoty, ale umisteni v pameti, ktere neni stejne
```

Pokud bychom chtěli dané objekty srovnat pomocí ==, tak musíme implementovat funkci `__eq__(self)`
```python
class Car:

    def __init__(self, spz, brand, color, engine, owner):
        self.spz = spz
        self.brand = brand
        self.color = color
        self.engine = engine
        self.owner = owner

    def change_owner(self, new_owner):
        self.owner = new_owner

    def __str__(self):
        return 'SPZ auta: {} a jeho vlastník: {}'.format(self.spz, self.owner)

    # other predstavuje druhy objekt, ktery budeme porovnavat
    def __eq__(self, other):
        if isinstance(other, Car):
            return self.spz == other.spz
        return False

fabia1 = Car('6AD 7222', 'Škoda', 'blue', '1.2 TSI', 'Asseco')
fabia2 = Car('6AD 7222', 'Škoda', 'blue', '1.2 TSI', 'Asseco')
prius = Car('7AS 7345', 'Toyota', 'white', '1.4', 'Asseco')

print(fabia1 == fabia2) # vypise True - porovnava SPZ aut
```



