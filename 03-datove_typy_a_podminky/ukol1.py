# Zapisujte jména lidí, které uživatel zadá do list. Poté list vypište.
# Pokud uživatel bude chtít list vypsat bez duplicitních jmen, tak ho vypište bez duplicit
names = ['Katka', 'Katka']
name = input('Zadejte jméno: ')
names.append(name)

print(list(set(names)))